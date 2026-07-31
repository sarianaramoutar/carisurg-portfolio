"""
Model construction, training, prediction, evaluation, and persistence for Emergency Department triage prediction.

Supports multiple machine learning models through a configuration-based interface.
"""

import time
import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


# ---------------------------------------------------------------------
# 1. Build Model (Supports Random Forest, Logistic Regression, & Gradient Boosting)
# ---------------------------------------------------------------------

def build_model(config: dict):
    """
    Build a model instance dynamically based on configuration settings.

    Parameters
    ----------
    config : dict
        Dictionary containing 'model_type' and model 'hyperparameters'.

    Returns
    -------
    sklearn estimator object
        Configured scikit-learn model.
    """
    model_type = config.get("model_type", "random_forest").lower()
    params = config.get("hyperparameters", {})

    if model_type == "random_forest":
        return RandomForestClassifier(**params)
    elif model_type == "logistic_regression":
        return LogisticRegression(**params)
    elif model_type == "gradient_boosting":
        return GradientBoostingClassifier(**params)
    else:
        raise ValueError(
            f"Unsupported model_type: '{model_type}'. "
            "Supported options: 'random_forest', 'logistic_regression', 'gradient_boosting'."
        )


# ---------------------------------------------------------------------
# 2. Train Model
# ---------------------------------------------------------------------

def train_model(model, X_train, y_train):
    """
    Train the model on the training set and measure execution time.

    Parameters
    ----------
    model : sklearn estimator
        Unfitted model object.
    X_train : pandas.DataFrame or numpy.ndarray
        Training features.
    y_train : pandas.Series or numpy.ndarray
        Training labels.

    Returns
    -------
    model : trained estimator
        Fitted model object.
    training_time : float
        Elapsed training time in seconds.
    """
    start_time = time.perf_counter()
    model.fit(X_train, y_train)
    end_time = time.perf_counter()

    training_time = end_time - start_time
    print(f"✓ Model trained in {training_time:.3f} seconds.")

    return model, training_time


# ---------------------------------------------------------------------
# 3. Predict Labels
# ---------------------------------------------------------------------

def predict(model, X_test):
    """
    Generate triage level predictions for test records.

    Parameters
    ----------
    model : trained estimator
        Fitted model object.
    X_test : pandas.DataFrame or numpy.ndarray
        Testing features.

    Returns
    -------
    numpy.ndarray
        Predicted ESI levels.
    """
    return model.predict(X_test)


# ---------------------------------------------------------------------
# 4. Evaluate Model (Includes Full Per-Class Metrics for ESI 1 to 5)
# ---------------------------------------------------------------------

def evaluate_model(model, X_test, y_test) -> dict:
    """
    Evaluate model across global metrics, full per-class ESI levels (1–5), and latency.

    Computes:
      - Overall Accuracy & Weighted F1
      - Macro Precision, Recall, and F1
      - Breakdown for every ESI level (ESI-1, ESI-2, ESI-3, ESI-4, ESI-5)
      - Total and per-patient inference latency (ms)
    These metrics allow overall performance and individual ESI levels to be evaluated separately.
    
    Parameters
    ----------
    model : trained estimator
        Fitted model object.
    X_test : pandas.DataFrame or numpy.ndarray
        Testing features.
    y_test : pandas.Series or numpy.ndarray
        True target labels.

    Returns
    -------
    dict
        Dictionary containing overall and per-class metrics.
    """
    # 1. Benchmark Inference Latency - Measure how long prediction takes.
    start_time = time.perf_counter()
    y_pred = model.predict(X_test)
    end_time = time.perf_counter()

    total_inference_time = end_time - start_time
    latency_per_sample_ms = (total_inference_time / len(X_test)) * 1000

    # 2. Overall Aggregated Metrics
    accuracy = accuracy_score(y_test, y_pred)

    macro_precision, macro_recall, macro_f1, _ = precision_recall_fscore_support(
        y_test, y_pred, average="macro", zero_division=0
    )

    _, _, weighted_f1, _ = precision_recall_fscore_support(
        y_test, y_pred, average="weighted", zero_division=0
    )

    metrics = {
        "Accuracy": float(accuracy),
        "Weighted F1": float(weighted_f1),
        "Macro Precision": float(macro_precision),
        "Macro Recall": float(macro_recall),
        "Macro F1": float(macro_f1),
        "Inference Time Total (s)": float(total_inference_time),
        "Latency Per Patient (ms)": float(latency_per_sample_ms),
    }

    # 3. Full Per-Class Breakdown (ESI Levels 1 through 5)
    classes = sorted(list(np.unique(np.concatenate([y_test, y_pred]))))
    per_class_precision, per_class_recall, per_class_f1, _ = precision_recall_fscore_support(
        y_test, y_pred, labels=classes, average=None, zero_division=0
    )

    # Store individual metrics for each ESI level (1, 2, 3, 4, 5)
    for idx, esi_level in enumerate(classes):
        level_int = int(esi_level)
        metrics[f"ESI-{level_int} Recall"] = float(per_class_recall[idx])
        metrics[f"ESI-{level_int} Precision"] = float(per_class_precision[idx])
        metrics[f"ESI-{level_int} F1"] = float(per_class_f1[idx])
    # Store metrics for every ESI level individually.
    # This allows performance to be assessed for clinically
    # important triage categories based on project priorities
    
    return metrics


# ---------------------------------------------------------------------
# 5. Model Persistence (Save / Load Artifacts)
# ---------------------------------------------------------------------

def save_model(model, file_path: str):
    """
    Save a trained model object to disk as a .joblib file.

    Parameters
    ----------
    model : trained estimator
        Fitted model object.
    file_path : str
        Target file path (e.g., 'models/optimised_rf.joblib').
    """
    joblib.dump(model, file_path)
    print(f"✓ Model successfully saved to '{file_path}'")


def load_model(file_path: str):
    """
    Load a trained model object from disk.

    Parameters
    ----------
    file_path : str
        Path to saved .joblib file.

    Returns
    -------
    trained estimator
        Loaded model ready for inference.
    """
    try:
        model = joblib.load(file_path)
        print(f"✓ Model loaded successfully from '{file_path}'")
        return model
    except Exception as e:
        raise FileNotFoundError(f"Failed to load model from '{file_path}': {str(e)}")
