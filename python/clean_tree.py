#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find and remove unwanted files and folders.

Usage:
    clean_tree.py [options] DIRECTORY

Options:
    -h, --help          Show this help message and exit.
    -s, --suppress      Suppress the list of unwanted items from being printed.
    -f, --force         Skip confirmation and remove unwanted items directly.

Clean Tree File:
The clean tree file is a file named ".clean_tree" that contains a list of
unwanted files and folders. The file should be located in the directory that
you want to clean up. Each line in the file should contain the name of a file
or folder that you want to remove.

Example '.clean_tree' file contents:
__pycache__
.coverage
.pytest_cache
"""
# version: 0.3.7
# license: MIT
# author: Anthony Pagan
# email: get-tony@outlook.com


import sys
import argparse
import shutil
from pathlib import Path


def load_config(config_path: Path) -> set:
    """Load the unwanted paths from the configuration file."""
    try:
        with config_path.open() as open_conf_file:
            config_data = open_conf_file.read().splitlines()
        return set(config_data)
    except FileNotFoundError:
        print(f"Removal list not found: {config_path}")
        print("Please make sure the removal list exists and try again.")
        sys.exit(1)


def find_unwanted_items(dir_path: Path, unwanted_paths: set) -> list:
    """Find the unwanted items in the directory."""
    unwanted_items = []
    for item in dir_path.rglob("*"):
        if item.name in unwanted_paths:
            unwanted_items.append(item)
    return unwanted_items


def remove_unwanted_items(unwanted_items: list) -> None:
    """Remove the unwanted items from the directory."""
    for item in unwanted_items:
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)


def main():
    """Parse the command line arguments and run the cleanup process."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", help="The directory to clean up.")
    parser.add_argument(
        "-s",
        "--suppress",
        action="store_true",
        help="Suppress the list of unwanted items from being printed.",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Skip confirmation and remove unwanted items directly.",
    )
    args = parser.parse_args()

    dir_path = Path(args.directory)
    config_path = dir_path / ".clean_tree"
    loaded_unwanted_items = load_config(config_path)

    unwanted_items = find_unwanted_items(dir_path, loaded_unwanted_items)

    if not args.suppress:
        print("Unwanted items found:")
        for item in unwanted_items:
            print(item)

    if args.force or (
        not args.force
        and input("Do you want to remove these items? (y/N): ").lower() == "y"
    ):
        remove_unwanted_items(unwanted_items)
        print(f"Removed {len(unwanted_items)} unwanted items.")
    else:
        print("Operation cancelled.")


if __name__ == "__main__":
    main()
