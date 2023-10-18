#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert YAML files to JSON files."""
# version: 0.2.0
# license: MIT
# author: Anthony Pagan
# repo: https://github.com/get-tony/pyutils
# Requires: pyyaml

import argparse
import json
import os
import sys
from typing import Optional
import yaml


# Define system encoding
ENCODING: str = sys.getfilesystemencoding() or sys.getdefaultencoding()


def convert_file(
    source_file_path: str, target_file_path: Optional[str] = None
) -> None:
    """Convert a single YAML file to JSON.

    Args:
        source_file_path: The path to the source YAML file.
        target_file_path: The path to the target JSON file.

    Returns:
        None.
    """
    # Open the source file
    try:
        with open(source_file_path, "r", encoding=ENCODING) as source_file:
            source_content = yaml.safe_load(source_file)
    except FileNotFoundError:
        print(f"ERROR: {source_file_path} not found")
        return

    # Convert the YAML to JSON
    output = json.dumps(source_content)

    # Write to the target file or stdout
    if target_file_path is None:
        print(output)
    else:
        try:
            with open(target_file_path, "x", encoding=ENCODING) as target_file:
                target_file.write(output)
        except FileExistsError:
            print(f"ERROR: {target_file_path} already exists")


def convert_directory(
    source_dir_path: str, target_dir_path: Optional[str] = None
) -> None:
    """Convert all YAML files in a directory to JSON.

    Args:
        source_dir_path: The path to the source directory.
        target_dir_path: The path to the target directory.

    Returns:
        None.
    """
    for root, _, files in os.walk(source_dir_path):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                source_file_path = os.path.join(root, file)
                if target_dir_path is None:
                    target_file_path = None
                else:
                    target_file_path = os.path.join(
                        target_dir_path,
                        file.replace(".yaml", ".json").replace(
                            ".yml", ".json"
                        ),
                    )
                convert_file(source_file_path, target_file_path)


def main() -> None:
    """Parse command line arguments and convert files."""
    parser = argparse.ArgumentParser(description="Convert YAML files to JSON.")
    parser.add_argument(
        "source",
        metavar="source_file_or_dir",
        type=str,
        help="the source YAML file or directory",
    )
    parser.add_argument(
        "target",
        metavar="target_file_or_dir",
        type=str,
        nargs="?",
        default=None,
        help="the target JSON file or directory",
    )
    args = parser.parse_args()

    source_path: str = args.source
    target_path: Optional[str] = args.target

    # Convert a single file
    if os.path.isfile(source_path):
        if target_path is not None and os.path.isdir(target_path):
            target_path = os.path.join(
                target_path,
                os.path.basename(source_path)
                .replace(".yaml", ".json")
                .replace(".yml", ".json"),
            )
        convert_file(source_path, target_path)
    # Convert a directory
    elif os.path.isdir(source_path):
        if target_path is not None and os.path.isfile(target_path):
            print(
                "ERROR: target must be a directory when source is a directory"
            )
            return
        convert_directory(source_path, target_path)
    # Invalid source path
    else:
        print(f"ERROR: {source_path} is not a valid file or directory")


if __name__ == "__main__":
    main()
