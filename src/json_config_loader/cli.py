"""Command-line interface for JSON Config Loader."""

from __future__ import annotations

import argparse
import json

from rich.console import Console
from rich.syntax import Syntax

from .loader import ConfigLoadError, load_config
from .validator import SchemaLoadError, load_schema, validate_config

console = Console()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="json-config-loader",
        description="Load a JSON config file and validate it against a JSON schema.",
    )
    parser.add_argument("config", help="Path to the JSON config file.")
    parser.add_argument(
        "--schema", "-s", help="Path to the JSON schema file (optional).",
    )
    parser.add_argument(
        "--print", "-p", dest="print_config", action="store_true",
        help="Print the loaded config as pretty JSON.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    try:
        config = load_config(args.config)
    except ConfigLoadError as exc:
        console.print(f"[bold red]Error:[/bold red] {exc}")
        return 1

    console.print(f"[green]Loaded config:[/green] {args.config}")

    if args.print_config:
        console.print(Syntax(json.dumps(config, indent=2), "json", theme="monokai"))

    if args.schema:
        try:
            schema = load_schema(args.schema)
        except SchemaLoadError as exc:
            console.print(f"[bold red]Schema error:[/bold red] {exc}")
            return 1

        errors = validate_config(config, schema)
        if errors:
            console.print(
                f"[bold red]Validation failed[/bold red] ({len(errors)} error(s)):"
            )
            for msg in errors:
                console.print(f"  [red]x[/red] {msg}")
            return 2

        console.print("[bold green]Config is valid[/bold green]")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
