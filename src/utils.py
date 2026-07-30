"""
Shared utility functions used throughout the project.

These helper functions avoid repeating common tasks such as
loading configuration files, parsing command-line arguments,
creating folders, and formatting execution times.
"""

import argparse
import os
import yaml


def parse_args():
    """
    Parse command-line arguments.

    Returns
    -------
    argparse.Namespace
        Parsed command-line arguments.
    """

    parser = argparse.ArgumentParser(
        description="Train the Emergency Department triage prediction model."
    )

    parser.add_argument(
        "--config",
        type=str,
        default="config.yaml",
        help="Path to the configuration file."
    )

    return parser.parse_args()


def load_config(config_path):
    """
    Load the YAML configuration file.

    Parameters
    ----------
    config_path : str
        Path to the YAML configuration file.

    Returns
    -------
    dict
        Configuration dictionary.
    """

    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"Configuration file not found: {os.path.abspath(config_path)}"
        )

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def create_folder(folder_path):
    """
    Create a folder if it does not already exist.

    Parameters
    ----------
    folder_path : str
        Folder location.
    """

    os.makedirs(folder_path, exist_ok=True)


def format_time(seconds):
    """
    Convert seconds into a readable string.

    Parameters
    ----------
    seconds : float

    Returns
    -------
    str
        Human-readable time.
    """

    if seconds >= 3600:
        return f"{seconds / 3600:.2f} hours"

    if seconds >= 60:
        return f"{seconds / 60:.2f} minutes"

    if seconds >= 1:
        return f"{seconds:.3f} seconds"

    return f"{seconds * 1000:.3f} milliseconds"
