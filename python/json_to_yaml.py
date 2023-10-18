#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert a JSON file to YAML"""
# version: 0.2.0
# license: MIT
# author: Anthony Pagan
# email: get-tony@outlook.com
# Requires: pyyaml

import argparse
import json
import os
import sys
import yaml


# Define system encoding
ENCODING = sys.getfilesystemencoding() or sys.getdefaultencoding()


def convert_file(source_path: str, target_path: str = None) -> None:
    """Convert a JSON file to YAML.

    Args:
        source_path: The path to the source JSON file.
        target_path: The path to the target YAML file, or None to print to stdout.

    Returns:
        None.
    """
    # Check if the source file exists
    if not os.path.exists(source_path):
        print(f"ERROR: {source_path} not found")
        return

    # Load the JSON content
    try:
        with open(source_path, "r", encoding=ENCODING) as source_file:
            source_content = json.load(source_file)
    except json.JSONDecodeError as exc:
        print(f"ERROR: {source_path} is not valid JSON: {exc}")
        return

    # Convert the JSON to YAML
    output = yaml.dump(source_content)

    # Write to the target file or stdout
    if target_path is None:
        print(output)
    elif os.path.exists(target_path):
        print(f"ERROR: {target_path} already exists")
    else:
        with open(target_path, "w", encoding=ENCODING) as target_file:
            target_file.write(output)


def main() -> None:
    """Parse command line arguments and convert files."""
    parser = argparse.ArgumentParser(description="Convert JSON files to YAML")
    parser.add_argument(
        "source",
        metavar="source_file",
        type=str,
        help="the path to the source JSON file to convert",
    )
    parser.add_argument(
        "target",
        metavar="target_file",
        type=str,
        nargs="?",
        default=None,
        help="the path to the target YAML file to write (default: stdout)",
    )
    args = parser.parse_args()

    source_path: str = args.source
    target_path: str = args.target

    convert_file(source_path, target_path)


if __name__ == "__main__":
    main()
