"""
Shared utility helper functions for the Emergency Department triage pipeline.

Handles recurring operational tasks:
  1. Parsing command-line arguments.
  2. Loading YAML configuration files safely.
  3. Creating output directories.
  4. Formatting raw execution time into human-readable strings.
"""

import argparse
import os
import yaml


def parse_args():
    """
    Parse command-line arguments for training script execution.

    Returns
    -------
    argparse.Namespace
        Parsed arguments containing config file path.
    """
    parser = argparse.ArgumentParser(
        description="Train the Emergency Department triage prediction model."
    )
    parser.add_argument(
        "--config",
        type=str,
        default="config.yaml",
        help="Path to the YAML configuration file (default: 'config.yaml')."
    )
    return parser.parse_args()


def load_config(config_path: str) -> dict:
    """
    Load and parse a YAML configuration file safely.

    Parameters
    ----------
    config_path : str
        Path to the configuration YAML file.

    Returns
    -------
    dict
        Parsed configuration settings dictionary.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"Configuration file not found: '{os.path.abspath(config_path)}'"
        )

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def create_folder(folder_path: str):
    """
    Create a directory if it does not already exist.

    Parameters
    ----------
    folder_path : str
        Target directory path.
    """
    os.makedirs(folder_path, exist_ok=True)


def format_time(seconds: float) -> str:
    """
    Convert elapsed time in seconds into a clean, human-readable string.

    Parameters
    ----------
    seconds : float
        Time in seconds.

    Returns
    -------
    str
        Formatted time string (e.g., '2.450 seconds' or '1.20 minutes').
    """
    if seconds >= 3600:
        return f"{seconds / 3600:.2f} hours"
    if seconds >= 60:
        return f"{seconds / 60:.2f} minutes"
    if seconds >= 1:
        return f"{seconds:.3f} seconds"
    return f"{seconds * 1000:.3f} milliseconds"
