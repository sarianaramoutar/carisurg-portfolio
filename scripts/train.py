"""
Main training script for the Emergency Department triage prediction project.

This script loads the project configuration, prepares the dataset,
engineers additional clinical features, trains the final Random Forest
model, and evaluates its performance.
"""

import sys
from pathlib import Path

# -------------------------------------------------------------------
# Allow Python to locate the project modules
# -------------------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_DIR))
sys.path.append(str(ROOT_DIR / "src"))

# -------------------------------------------------------------------
# Import project modules
# -------------------------------------------------------------------

from src.data import load_clean_df
from src.features import prepare_features
from src.model import (
    build_model,
    train_model,
    evaluate_model
)
from src.utils import (
    parse_args,
    load_config,
    create_folder
)

# -------------------------------------------------------------------
# Main workflow
# -------------------------------------------------------------------

def main():

    # Read command-line arguments
    args = parse_args()

    # Load project configuration
    cfg = load_config(args.config)

    # Ensure output folders exist
    create_folder("figs")
    create_folder("models")

    # --------------------------------------------------------------
    # Load dataset
    # --------------------------------------------------------------

    print("Loading dataset...")

    df = load_clean_df(
        cfg["data"]["raw_path"]
    )

    # --------------------------------------------------------------
    # Prepare features
    # --------------------------------------------------------------

    print("Preparing features...")

    X_train, X_test, y_train, y_test = prepare_features(df)

    # --------------------------------------------------------------
    # Build final model
    # --------------------------------------------------------------

    print("Building model...")

    model = build_model(cfg)

    # --------------------------------------------------------------
    # Train
    # --------------------------------------------------------------

    print("Training model...")

    trained_model, training_time = train_model(
        model,
        X_train,
        y_train
    )

    # --------------------------------------------------------------
    # Evaluate
    # --------------------------------------------------------------

    print("Evaluating model...\n")

    results = evaluate_model(
        trained_model,
        X_test,
        y_test,
        training_time
    )

    print(results)

    print("\nTraining complete.")


if __name__ == "__main__":
    main()
