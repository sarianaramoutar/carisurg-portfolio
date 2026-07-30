"""
Feature engineering, selection, and preprocessing module for Emergency
Department triage prediction.

This module is responsible for:
  1. Creating domain-specific clinical features (e.g., Shock Index, ratios).
  2. Selecting valid feature columns while excluding demographics, admin, and leakage data.
  3. Imputing missing values safely without data leakage.
  4. Standardising numerical features for models requiring scaled inputs.
"""

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


# ---------------------------------------------------------------------
# Feature Exclusion Constants (Fairness & Governance Standards)
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
# 1. Clinical Feature Engineering
# ---------------------------------------------------------------------

def add_clinical_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create clinically meaningful engineered features based on emergency department triage rules.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe containing raw vital signs.

    Returns
    -------
    pandas.DataFrame
        Dataframe augmented with engineered clinical features.
    """
    df_eng = df.copy()

    # Shock Index = Heart Rate / Systolic Blood Pressure (Key indicator of clinical shock)
    if "triage_vital_hr" in df_eng.columns and "triage_vital_sbp" in df_eng.columns:
        df_eng["eng_shock_index"] = (
            df_eng["triage_vital_hr"] / df_eng["triage_vital_sbp"].replace(0, np.nan)
        )

    # Bradycardia indicator (Heart Rate < 60 bpm)
    if "triage_vital_hr" in df_eng.columns:
        df_eng["eng_bradycardia"] = (
            df_eng["triage_vital_hr"] < 60
        ).astype(int)

    # Hyperglycaemia indicator (Blood Glucose > 180 mg/dL)
    if "triage_glucose" in df_eng.columns:
        df_eng["eng_hyperglycemia"] = (
            df_eng["triage_glucose"] > 180
        ).astype(int)

    # Hypothermia indicator (Temperature < 35°C)
    if "triage_vital_temp" in df_eng.columns:
        df_eng["eng_hypothermia"] = (
            df_eng["triage_vital_temp"] < 35
        ).astype(int)

    # Respiratory distress indicator (Respiratory Rate > 20 breaths/min)
    if "triage_vital_rr" in df_eng.columns:
        df_eng["eng_respiratory_distress"] = (
            df_eng["triage_vital_rr"] > 20
        ).astype(int)

    # SpO2 to Respiratory Rate Ratio
    if "triage_vital_o2" in df_eng.columns and "triage_vital_rr" in df_eng.columns:
        df_eng["eng_o2_rr_ratio"] = (
            df_eng["triage_vital_o2"] / df_eng["triage_vital_rr"].replace(0, np.nan)
        )

    return df_eng


# ---------------------------------------------------------------------
# 2. Feature Selection & Filtering
# ---------------------------------------------------------------------

def select_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract only valid predictor variables (vitals, chief complaints, engineered features)
    while dropping forbidden columns (demographics, administrative, leakage, target).

    Parameters
    ----------
    df : pandas.DataFrame
        Cleaned dataframe with engineered features.

    Returns
    -------
    pandas.DataFrame
        Filtered feature matrix (X).
    """
    # Create master list of columns to strictly exclude
    exclude_cols = set(DEMOGRAPHICS + ADMIN + LEAKAGE + [TARGET])

    # Dynamic search for chief complaints (all binary cc_* columns)
    chief_complaints = [
        col for col in df.columns 
        if col.startswith("cc_")
    ]

    # Dynamic search for engineered features (all eng_* columns)
    engineered_cols = [
        col for col in df.columns 
        if col.startswith("eng_")
    ]

    # Gather candidate features
    candidate_features = set(VITAL_SIGNS + chief_complaints + engineered_cols)

    # Keep only features present in dataset and not in the exclusion list
    final_features = [
        col for col in candidate_features
        if col in df.columns and col not in exclude_cols
    ]

    return df[final_features].copy()


# ---------------------------------------------------------------------
# 3. Leakage-Free Median Imputation
# ---------------------------------------------------------------------

def impute_features(X_train: pd.DataFrame, X_test: pd.DataFrame):
    """
    Impute missing values using training set medians.

    Fits the imputer ONLY on X_train to prevent data leakage, then
    transforms both X_train and X_test.

    Parameters
    ----------
    X_train : pandas.DataFrame
        Training feature set.
    X_test : pandas.DataFrame
        Testing feature set.

    Returns
    -------
    X_train_imp : pandas.DataFrame
        Imputed training set with column names preserved.
    X_test_imp : pandas.DataFrame
        Imputed testing set with column names preserved.
    imputer : SimpleImputer
        Fitted imputer object for future production inference.
    """
    imputer = SimpleImputer(strategy="median")

    # Fit on X_train, transform both sets
    X_train_array = imputer.fit_transform(X_train)
    X_test_array = imputer.transform(X_test)

    # Reconstruct DataFrames to retain column names for SHAP/feature importance
    X_train_imp = pd.DataFrame(X_train_array, columns=X_train.columns, index=X_train.index)
    X_test_imp = pd.DataFrame(X_test_array, columns=X_test.columns, index=X_test.index)

    return X_train_imp, X_test_imp, imputer


# ---------------------------------------------------------------------
# 4. Feature Scaling (Optional for Distance/Linear Models)
# ---------------------------------------------------------------------

def scale_features(X_train: pd.DataFrame, X_test: pd.DataFrame):
    """
    Standardise features by removing the mean and scaling to unit variance.

    Fits the scaler ONLY on X_train to prevent data leakage.

    Parameters
    ----------
    X_train : pandas.DataFrame
        Imputed training features.
    X_test : pandas.DataFrame
        Imputed testing features.

    Returns
    -------
    X_train_scaled : pandas.DataFrame
        Scaled training set.
    X_test_scaled : pandas.DataFrame
        Scaled testing set.
    scaler : StandardScaler
        Fitted scaler object.
    """
    scaler = StandardScaler()

    X_train_array = scaler.fit_transform(X_train)
    X_test_array = scaler.transform(X_test)

    # Reconstruct DataFrames to retain column names
    X_train_scaled = pd.DataFrame(X_train_array, columns=X_train.columns, index=X_train.index)
    X_test_scaled = pd.DataFrame(X_test_array, columns=X_test.columns, index=X_test.index)

    return X_train_scaled, X_test_scaled, scaler
