"""
Feature engineering and preprocessing functions for the Emergency
Department triage prediction project.
"""

import numpy as np

from sklearn.preprocessing import StandardScaler


# ---------------------------------------------------------------------
# Clinical feature engineering
# ---------------------------------------------------------------------

def add_clinical_features(df):
    """
    Create clinically meaningful engineered features.

    Parameters
    ----------
    df : pandas.DataFrame
        Input feature dataframe.

    Returns
    -------
    pandas.DataFrame
        Feature-engineered dataframe.
    """

    df_engineered = df.copy()

    # Bradycardia indicator
    if "triage_vital_hr" in df_engineered.columns:
        df_engineered["eng_bradycardia"] = (
            df_engineered["triage_vital_hr"] < 60
        ).astype(int)

    # Hyperglycaemia indicator
    if "triage_glucose" in df_engineered.columns:
        df_engineered["eng_hyperglycemia"] = (
            df_engineered["triage_glucose"] > 180
        ).astype(int)

    # Hypothermia indicator
    if "triage_vital_temp" in df_engineered.columns:
        df_engineered["eng_hypothermia"] = (
            df_engineered["triage_vital_temp"] < 35
        ).astype(int)

    # Respiratory distress indicator
    if "triage_vital_rr" in df_engineered.columns:
        df_engineered["eng_respiratory_distress"] = (
            df_engineered["triage_vital_rr"] > 20
        ).astype(int)

    # Oxygen saturation to respiratory rate ratio
    if (
        "triage_vital_o2" in df_engineered.columns
        and "triage_vital_rr" in df_engineered.columns
    ):
        df_engineered["eng_o2_rr_ratio"] = (
            df_engineered["triage_vital_o2"]
            / df_engineered["triage_vital_rr"].replace(0, np.nan)
        )

    return df_engineered


# ---------------------------------------------------------------------
# Feature scaling
# ---------------------------------------------------------------------

def scale_features(X_train, X_test):
    """
    Standardise the training and testing feature sets.

    The scaler is fitted only on the training data to
    prevent data leakage.
    """

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler
