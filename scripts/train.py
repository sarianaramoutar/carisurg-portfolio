"""
Main training pipeline for the Emergency Department triage prediction project.

Runs the complete machine learning workflow by coordinating the
modular functions provided in the src/ package.
"""

import os
import sys
from pathlib import Path
from sklearn.model_selection import train_test_split

# Allow imports from the project's src/ package.
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from src.data import load_data, clean_data
from src.features import add_clinical_features, select_features, impute_features
from src.model import build_model, train_model, evaluate_model, save_model
from src.utils import parse_args, load_config, create_folder, format_time


def main():
    print("\n" + "=" * 60)
    print("      STARTING CARISURG ED TRIAGE TRAINING PIPELINE      ")
    print("=" * 60 + "\n")

    # 1. Parse Arguments & Load Configuration (using src/utils.py)
    args = parse_args()
    cfg = load_config(args.config)

    seed = cfg.get("seed", 42)
    print(f"✓ Configuration successfully loaded from '{args.config}' (Seed: {seed})")

    # 2. Create output folders if required (using src/utils.py)
    for _, folder_path in cfg.get("paths", {}).items():
        create_folder(folder_path)

    # 3. Load & Clean Raw Data
    raw_data_path = cfg["data"]["raw_path"]
    print(f"\n[Step 1/5] Ingesting raw dataset: '{raw_data_path}'")
    raw_df = load_data(raw_data_path)
    cleaned_df = clean_data(raw_df)

    # 4. Feature Engineering & Feature Selection
    print("\n[Step 2/5] Engineering clinical features and selecting predictor variables...")
    engineered_df = add_clinical_features(cleaned_df)

    target_col = cfg["data"]["target"]
    y = engineered_df[target_col].astype(int)
    X = select_features(engineered_df)

    print(f"✓ Extracted {X.shape[1]} predictor features for model training.")

    # 5. Stratified Split & Leakage-Free Imputation
    print("\n[Step 3/5] Splitting the dataset (80% training / 20% testing) and imputing missing values...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y, 
        test_size=0.2, 
        random_state=seed, 
        stratify=y
    )

    X_train_imp, X_test_imp, _ = impute_features(X_train, X_test)

    # 6. Build & Train Model
    model_type = cfg["model"]["model_type"]
    print(f"\n[Step 4/5] Training model: '{model_type}'...")
    
    model = build_model(cfg["model"])
    trained_model, train_time = train_model(model, X_train_imp, y_train)
    print(f"✓ Training execution time: {format_time(train_time)}")

    # 7. Evaluate Model Metrics
    print("\n[Step 5/5] Evaluating overall performance and per-class ESI metrics...")
    metrics = evaluate_model(trained_model, X_test_imp, y_test)

    print("\n" + "-" * 48)
    print("              MODEL EVALUATION SUMMARY           ")
    print("-" * 48)
    for metric_name, value in metrics.items():
        if "Time" in metric_name or "Latency" in metric_name:
            print(f"  {metric_name:<36}: {value:.4f}")
        else:
            print(f"  {metric_name:<36}: {value * 100:.2f}%")
    print("-" * 48)

    # 8. Save Model Artifact
    model_save_path = os.path.join(cfg["paths"]["models"], f"{model_type}_model.joblib")
    save_model(trained_model, model_save_path)

    print("\n" + "=" * 60)
    print("         TRAINING PIPELINE COMPLETED SUCCESSFULLY        ")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
