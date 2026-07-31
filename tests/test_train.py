"""
Sanity smoke test for the training pipeline.

Runs an end-to-end execution of the data pipeline on a small 50-row 
subset to verify the model builds, trains, and evaluates without error.
"""

import sys
from pathlib import Path

# -------------------------------------------------------------------
# Ensure Python can locate the project modules inside 'src/'
# -------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import pandas as pd
from sklearn.model_selection import train_test_split

from src.data import load_data, clean_data
from src.features import add_clinical_features, select_features, impute_features
from src.model import build_model, train_model, evaluate_model
from src.utils import load_config


def test_pipeline_smoke_test():
    """
    Test B: 50-Row Training Pipeline Smoke Test.
    
    Loads a tiny 50-row sample of the dataset and runs it through:
      Data cleaning -> Feature engineering -> Imputation -> Training -> Evaluation.
    
    Verifies that the whole pipeline completes without raising exceptions.
    """
    # 1. Load config
    config = load_config("config.yaml")
    raw_path = config["data"]["raw_path"]

    # 2. Ingest data and slice a tiny 50-row subset
    raw_df = load_data(raw_path)
    sample_df = raw_df.head(50).copy()
    assert len(sample_df) == 50, "Sample dataframe should contain exactly 50 rows!"

    # 3. Data cleaning
    cleaned_df = clean_data(sample_df)
    assert not cleaned_df.empty, "Cleaned sample dataframe should not be empty!"

    # 4. Feature engineering & selection
    engineered_df = add_clinical_features(cleaned_df)
    target_col = config["data"]["target"]
    y = engineered_df[target_col].astype(int)
    X = select_features(engineered_df)

    assert X.shape[0] == len(y), "Predictors (X) and Target (y) must have matching row counts!"

    # 5. Imputation & Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    X_train_imp, X_test_imp, _ = impute_features(X_train, X_test)

    # 6. Model Construction & Training
    model = build_model(config["model"])
    trained_model, train_time = train_model(model, X_train_imp, y_train)

    assert trained_model is not None, "Trained model object should not be None!"
    assert train_time >= 0, "Training time calculation should be non-negative!"

    # 7. Model Evaluation
    metrics = evaluate_model(trained_model, X_test_imp, y_test)

    assert isinstance(metrics, dict), "evaluate_model() must return a dictionary of metrics!"
    assert "Accuracy" in metrics, "Metrics dictionary must contain 'Accuracy' key!"
