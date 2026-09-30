"""Tests for the config loader."""

import json

import pytest

from json_config_loader.loader import ConfigLoadError, load_config


def test_load_valid_config(tmp_path):
    cfg = tmp_path / "config.json"
    cfg.write_text(json.dumps({"name": "demo", "port": 8080}))

    data = load_config(str(cfg))
    assert data == {"name": "demo", "port": 8080}


def test_load_missing_file_raises(tmp_path):
    with pytest.raises(ConfigLoadError, match="not found"):
        load_config(str(tmp_path / "missing.json"))


def test_load_invalid_json_raises(tmp_path):
    cfg = tmp_path / "bad.json"
    cfg.write_text("{not valid json")

    with pytest.raises(ConfigLoadError, match="Invalid JSON"):
        load_config(str(cfg))


def test_load_non_object_root_raises(tmp_path):
    cfg = tmp_path / "arr.json"
    cfg.write_text("[1, 2, 3]")

    with pytest.raises(ConfigLoadError, match="must be a JSON object"):
        load_config(str(cfg))
