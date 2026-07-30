"""
Data loading and cleaning module for Emergency Department Triage Prediction.

This module handles raw dataset ingestion, vital sign type coercion,
and target variable (ESI) validation.
"""

import pandas as pd
import numpy as np

# ---------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------

TARGET = "esi"

VITAL_SIGNS = [
    "triage_vital_dbp",
    "triage_vital_hr",
    "triage_vital_o2",
    "triage_vital_rr",
    "triage_vital_sbp",
    "triage_vital_temp",
    "triage_glucose",
]


# ---------------------------------------------------------------------
# Load Raw Data
# ---------------------------------------------------------------------

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load raw triage dataset from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV dataset.

    Returns
    -------
    pandas.DataFrame
        Loaded raw dataset.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✓ Successfully loaded dataset from {file_path} (Shape: {df.shape})")
        return df
    except Exception as e:
        raise FileNotFoundError(f"Failed to load dataset at '{file_path}': {str(e)}")


# ---------------------------------------------------------------------
# Clean Data
# ---------------------------------------------------------------------

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw triage DataFrame:
      1. Drops rows missing the target variable (ESI).
      2. Validates ESI values to ensure they are within the clinical range [1, 5].
      3. Coerces vital signs to numeric types.

    Parameters
    ----------
    df : pandas.DataFrame
        Raw loaded dataframe.

    Returns
    -------
    pandas.DataFrame
        Cleaned dataframe ready for feature engineering.
    """
    df_clean = df.copy()

    # 1. Clean and validate Target (ESI)
    if TARGET not in df_clean.columns:
        raise KeyError(f"Target column '{TARGET}' not found in dataset.")

    # Drop missing target rows
    initial_rows = len(df_clean)
    df_clean = df_clean.dropna(subset=[TARGET])
    
    # Ensure target is numeric and within valid ESI range (1 to 5)
    df_clean[TARGET] = pd.to_numeric(df_clean[TARGET], errors="coerce")
    df_clean = df_clean[df_clean[TARGET].isin([1.0, 2.0, 3.0, 4.0, 5.0])]
    df_clean[TARGET] = df_clean[TARGET].astype(int)

    dropped_rows = initial_rows - len(df_clean)
    if dropped_rows > 0:
        print(f"✓ Dropped {dropped_rows} rows with invalid/missing target '{TARGET}'.")

    # 2. Coerce vital sign columns to numeric float
    for col in VITAL_SIGNS:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")

    print(f"✓ Cleaned dataset ready with {len(df_clean)} records.")
    return df_clean
