"""
Main training pipeline script for the Emergency Department triage prediction project.

This script executes the end-to-end workflow:
  1. Loads configuration settings from config.yaml.
  2. Ingests and cleans raw hospital data (src/data.py).
  3. Engineers clinical features and splits data without leakage (src/features.py).
  4. Imputes missing values safely using training set medians (src/features.py).
  5. Builds and trains the selected model (src/model.py).
  6. Evaluates global and per-class ESI metrics (src/model.py).
  7. Saves the trained model artifact to disk (.joblib).
"""

import os
import sys
import yaml
from pathlib import Path
from sklearn.model_selection import train_test_split

# -------------------------------------------------------------------
# Ensure Python can locate the project modules inside 'src/'
# -------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from src.data import load_data, clean_data
from src.features import add_clinical_features, select_features, impute_features
from src.model import build_model, train_model, evaluate_model, save_model


def main():
    print("\n" + "=" * 60)
    print("      STARTING CARISURG ED TRIAGE TRAINING PIPELINE      ")
    print("=" * 60 + "\n")

    # 1. Load Configuration Settings
    config_path = ROOT_DIR / "config.yaml"
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found at {config_path}")

    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)

    seed = cfg.get("seed", 42)
    print(f"✓ Configuration loaded successfully. (Global Seed: {seed})")

    # 2. Ensure Output Directories Exist
    for folder_key, folder_path in cfg.get("paths", {}).items():
        os.makedirs(folder_path, exist_ok=True)

    # 3. Load & Clean Raw Data
    raw_data_path = cfg["data"]["raw_path"]
    print(f"\n[Step 1/5] Loading raw data from: {raw_data_path}")
    raw_df = load_data(raw_data_path)
    cleaned_df = clean_data(raw_df)

    # 4. Feature Engineering & Feature Selection
    print("\n[Step 2/5] Engineering clinical features & selecting valid predictors...")
    engineered_df = add_clinical_features(cleaned_df)

    # Separate target (esi) from features (X)
    target_col = cfg["data"]["target"]
    y = engineered_df[target_col].astype(int)
    X = select_features(engineered_df)

    print(f"✓ Selected {X.shape[1]} predictor features for model training.")

    # 5. Train-Test Split (Stratified to maintain ESI class balance)
    print("\n[Step 3/5] Splitting data into training (80%) and testing (20%) sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y, 
        test_size=0.2, 
        random_state=seed, 
        stratify=y
    )

    # Leakage-Free Median Imputation
    print("✓ Imputing missing values using training medians...")
    X_train_imp, X_test_imp, _ = impute_features(X_train, X_test)

    # 6. Build & Train Model
    model_type = cfg["model"]["model_type"]
    print(f"\n[Step 4/5] Building and training model: '{model_type}'...")
    
    model = build_model(cfg["model"])
    trained_model, train_time = train_model(model, X_train_imp, y_train)

    # 7. Evaluate Model Performance
    print("\n[Step 5/5] Evaluating model performance...")
    metrics = evaluate_model(trained_model, X_test_imp, y_test)

    # Print Formatted Results Summary
    print("\n" + "-" * 45)
    print("              MODEL PERFORMANCE METRICS           ")
    print("-" * 45)
    for metric_name, value in metrics.items():
        if "Time" in metric_name or "Latency" in metric_name:
            print(f"  {metric_name:<35}: {value:.4f}")
        else:
            print(f"  {metric_name:<35}: {value * 100:.2f}%")
    print("-" * 45)

    # 8. Save Trained Model Artifact
    model_save_path = os.path.join(cfg["paths"]["models"], f"{model_type}_model.joblib")
    save_model(trained_model, model_save_path)

    print("\n" + "=" * 60)
    print("         TRAINING PIPELINE COMPLETED SUCCESSFULLY        ")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
