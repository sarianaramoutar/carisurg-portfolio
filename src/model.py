"""
Model building, training, prediction, and evaluation functions for the
Emergency Department triage prediction project.
"""

import time

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
)


# ---------------------------------------------------------------------
# Build model
# ---------------------------------------------------------------------

def build_model(config):
    """
    Build the final pinned Random Forest model from the configuration.

    Parameters
    ----------
    config : dict
        Dictionary containing the model hyperparameters.

    Returns
    -------
    sklearn.ensemble.RandomForestClassifier
        Configured Random Forest model.
    """

    return RandomForestClassifier(
        n_estimators=config["n_estimators"],
        max_depth=config["max_depth"],
        max_features=config["max_features"],
        min_samples_split=config["min_samples_split"],
        min_samples_leaf=config["min_samples_leaf"],
        class_weight=config["class_weight"],
        random_state=config["random_state"],
        n_jobs=-1,
    )


# ---------------------------------------------------------------------
# Train model
# ---------------------------------------------------------------------

def train_model(model, X_train, y_train):
    """
    Train the model and measure training time.

    Returns
    -------
    model : trained estimator
    training_time : float
        Training time in seconds.
    """

    start = time.perf_counter()
    model.fit(X_train, y_train)
    end = time.perf_counter()

    training_time = end - start

    return model, training_time


# ---------------------------------------------------------------------
# Predict
# ---------------------------------------------------------------------

def predict(model, X_test):
    """
    Generate predictions from the trained model.
    """

    return model.predict(X_test)


# ---------------------------------------------------------------------
# Evaluate model
# ---------------------------------------------------------------------

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model using the same metrics as the Week 7 notebook.

    Returns
    -------
    metrics : dict
        Dictionary containing evaluation metrics and inference timing.
    """

    # Measure inference time
    start = time.perf_counter()
    predictions = model.predict(X_test)
    end = time.perf_counter()

    inference_time = end - start
    inference_time_per_prediction = inference_time / len(X_test)

    # Multiclass evaluation metrics
    accuracy = accuracy_score(y_test, predictions)

    macro_precision, macro_recall, macro_f1, _ = (
        precision_recall_fscore_support(
            y_test,
            predictions,
            average="macro",
            zero_division=0,
        )
    )

    _, _, weighted_f1, _ = precision_recall_fscore_support(
        y_test,
        predictions,
        average="weighted",
        zero_division=0,
    )

    metrics = {
        "Accuracy": accuracy,
        "Macro Precision": macro_precision,
        "Macro Recall": macro_recall,
        "Macro F1": macro_f1,
        "Weighted F1": weighted_f1,
        "Total Inference Time (seconds)": inference_time,
        "Inference Time Per Prediction (seconds)": inference_time_per_prediction,
    }

    return metrics
