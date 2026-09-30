# Usage Guide

## Validate a config against a schema

    json-config-loader config.json --schema schema.json

## Just load and print the config

    json-config-loader config.json --print

## Example

Given config.json:

    {"name": "myapp", "port": 8080}

And schema.json:

    {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "port": {"type": "integer", "minimum": 1}
      },
      "required": ["name", "port"]
    }

Running:

    json-config-loader config.json --schema schema.json

Prints:

    Loaded config: config.json
    Config is valid
