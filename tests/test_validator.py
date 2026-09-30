"""Tests for the schema validator."""

import json

import pytest

from json_config_loader.validator import (
    SchemaLoadError,
    load_schema,
    validate_config,
)

SIMPLE_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "port": {"type": "integer", "minimum": 1, "maximum": 65535},
    },
    "required": ["name", "port"],
}


def test_validate_ok():
    errors = validate_config({"name": "demo", "port": 8080}, SIMPLE_SCHEMA)
    assert errors == []


def test_validate_missing_required():
    errors = validate_config({"name": "demo"}, SIMPLE_SCHEMA)
    assert len(errors) == 1
    assert "port" in errors[0]


def test_validate_wrong_type():
    errors = validate_config({"name": 42, "port": 8080}, SIMPLE_SCHEMA)
    assert any("name" in e for e in errors)


def test_validate_out_of_range():
    errors = validate_config({"name": "demo", "port": 99999}, SIMPLE_SCHEMA)
    assert any("port" in e for e in errors)


def test_load_schema_valid(tmp_path):
    sf = tmp_path / "schema.json"
    sf.write_text(json.dumps(SIMPLE_SCHEMA))

    schema = load_schema(str(sf))
    assert schema["type"] == "object"


def test_load_schema_missing(tmp_path):
    with pytest.raises(SchemaLoadError, match="not found"):
        load_schema(str(tmp_path / "nope.json"))
