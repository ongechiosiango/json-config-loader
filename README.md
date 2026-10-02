# JSON Config Loader

[![CI](https://github.com/ongechiosiango/json-config-loader/actions/workflows/ci.yml/badge.svg)](https://github.com/ongechiosiango/json-config-loader/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)

Load a JSON config file and validate it against a JSON schema.

## Features

- Load JSON config files with clear, actionable error messages.
- Validate against JSON Schema (Draft 2020-12) via jsonschema.
- Pretty-print configs with syntax highlighting via rich.
- Simple CLI with non-zero exit codes for scripting.

## Installation

From source:

    git clone git@github.com:ongechiosiango/json-config-loader.git
    cd json-config-loader
    python3 -m venv venv
    source venv/bin/activate
    pip install -e ".[dev]"

## Usage

    json-config-loader config.json --schema schema.json

Or just print a config:

    json-config-loader config.json --print

See docs/usage.md for more.

## Development

    pip install -e ".[dev]"
    pytest -v

## Contributing

See CONTRIBUTING.md.

## License

MIT - see LICENSE.
