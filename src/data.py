"""
Data loading and preparation functions for the Emergency Department
triage prediction project.

This module loads the cleaned Yale EMMLC dataset and prepares the
feature matrix (X) and target variable (y) ready for modelling.
"""

import pandas as pd

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

DEMOGRAPHICS = [
    "age",
    "gender",
    "ethnicity",
    "race",
    "insurance_type",
]

ADMIN = [
    "Unnamed: 0",
    "dep_name",
    "patient_id",
    "encounter_id",
    "visit_id",
    "disposition_id",
]

LEAKAGE = [
    "n_edvisits",
    "n_admissions",
    "admitted_to_hospital",
    "admission_type",
    "admission_source",
    "discharge_disposition",
    "discharge_destination",
    "length_of_stay",
    "admission_to_icu_flag",
    "icu_stay_days",
    "mortality_flag",
    "disposition_dt",
    "discharge_dt",
]


# ---------------------------------------------------------------------
# Load dataset
# ---------------------------------------------------------------------

def load_data(file_path):
    """
    Load the cleaned triage dataset.

    Parameters
    ----------
    file_path : str
        Path to the CSV dataset.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset.
    """

    return pd.read_csv(file_path)


# ---------------------------------------------------------------------
# Prepare features
# ---------------------------------------------------------------------

def prepare_data(df):
    """
    Prepare the feature matrix (X) and target vector (y).

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    Returns
    -------
    X : pandas.DataFrame
        Prepared feature matrix.

    y : pandas.Series
        Target variable.
    """

    exclude_cols = list(
        set(DEMOGRAPHICS + ADMIN + LEAKAGE + [TARGET])
    )

    # Keep only columns that actually exist
    exclude_cols = [
        col for col in exclude_cols
        if col in df.columns
    ]

    vital_signs = [
        col for col in VITAL_SIGNS
        if col in df.columns
    ]

    chief_complaints = [
        col
        for col in df.columns
        if col.startswith("cc_")
        and pd.api.types.is_numeric_dtype(df[col])
    ]

    selected_features = list(
        set(vital_signs + chief_complaints)
    )

    final_features = [
        col
        for col in selected_features
        if col not in exclude_cols
    ]

    X = df[final_features].copy()

    # Retain the median-imputation step from Week 7.
    X = X.fillna(X.median())

    y = df[TARGET].copy()

    return X, y
