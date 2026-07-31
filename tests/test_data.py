"""
Sanity tests for data loading and schema validation.

Ensures that the raw hospital dataset loads correctly, produces a non-empty 
DataFrame, contains required predictor variables, and enforces valid ESI target scores.
"""

import sys
from pathlib import Path

# -------------------------------------------------------------------
# Ensure Python can locate the project modules inside 'src/'
# -------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import pandas as pd
import pytest
from src.data import load_data, clean_data, TARGET, VITAL_SIGNS
from src.utils import load_config


def test_data_loading_and_schema():
    """
    Test A: Data Loading & Schema Sanity Check.
    
    Verifies:
      1. Configuration file loads and raw CSV path exists.
      2. load_data() returns a non-empty pandas DataFrame.
      3. clean_data() preserves essential schema structure.
      4. Target column ('esi') exists and contains valid emergency categories (1 to 5).
      5. Core vital sign predictor columns are present in the dataset.
    """
    # 1. Load path from config
    config = load_config("config.yaml")
    raw_path = config["data"]["raw_path"]

    # 2. Test raw data loading
    raw_df = load_data(raw_path)
    assert isinstance(raw_df, pd.DataFrame), "load_data() should return a pandas DataFrame"
    assert not raw_df.empty, "Raw loaded DataFrame is empty!"

    # 3. Test data cleaning
    cleaned_df = clean_data(raw_df)
    assert not cleaned_df.empty, "Cleaned DataFrame should not be empty!"

    # 4. Check Target Column Presence
    assert TARGET in cleaned_df.columns, f"Target column '{TARGET}' missing from schema!"

    # 5. Check Target Value Validity (ESI scores must strictly be 1, 2, 3, 4, or 5)
    unique_targets = set(cleaned_df[TARGET].unique())
    assert unique_targets.issubset({1, 2, 3, 4, 5}), (
        f"Corrupt ESI target values detected! Found: {unique_targets}"
    )

    # 6. Check Vital Signs Schema Presence
    for vital_col in VITAL_SIGNS:
        assert vital_col in cleaned_df.columns, (
            f"Expected vital sign column '{vital_col}' is missing from the dataset schema!"
        )
