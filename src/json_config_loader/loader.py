"""Load and parse JSON config files."""

from __future__ import annotations

import json
from pathlib import Path


class ConfigLoadError(Exception):
    """Raised when a JSON config file cannot be loaded or parsed."""


def load_config(path: str) -> dict:
    """Load a JSON file from disk and return it as a dict.

    Raises ConfigLoadError if the file is missing, unreadable, or invalid JSON.
    """
    config_path = Path(path)

    if not config_path.exists():
        raise ConfigLoadError(f"Config file not found: {path}")

    if not config_path.is_file():
        raise ConfigLoadError(f"Path is not a file: {path}")

    try:
        with config_path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as exc:
        raise ConfigLoadError(f"Invalid JSON in {path}: {exc}") from exc
    except OSError as exc:
        raise ConfigLoadError(f"Could not read {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ConfigLoadError(
            f"Config root must be a JSON object, got {type(data).__name__}"
        )

    return data
