"""Validate JSON configs against a JSON schema."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError


class SchemaLoadError(Exception):
    """Raised when a schema file cannot be loaded or is invalid."""


def load_schema(path: str) -> dict:
    """Load a JSON schema from disk."""
    schema_path = Path(path)

    if not schema_path.exists():
        raise SchemaLoadError(f"Schema file not found: {path}")

    try:
        with schema_path.open("r", encoding="utf-8") as fh:
            schema = json.load(fh)
    except json.JSONDecodeError as exc:
        raise SchemaLoadError(f"Invalid JSON in schema {path}: {exc}") from exc

    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise SchemaLoadError(f"Invalid JSON schema: {exc.message}") from exc

    return schema


def validate_config(config: dict, schema: dict) -> list:
    """Validate a config dict against a schema.

    Returns a list of human-readable error messages. Empty list means valid.
    """
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(config), key=lambda e: list(e.path))

    messages = []
    for err in errors:
        location = ".".join(str(p) for p in err.path) or "<root>"
        messages.append(f"{location}: {err.message}")
    return messages
