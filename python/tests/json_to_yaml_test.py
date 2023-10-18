#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert a JSON file to YAML"""
# license: MIT
# author: Anthony Pagan
# email: get-tony@outlook.com
# Requires: pyyaml

import json
import os
import sys
import yaml

from json_to_yaml import convert_file


# Define system encoding
ENCODING = sys.getfilesystemencoding() or sys.getdefaultencoding()


def test_convert_file(tmp_path):
    """Test that the function converts a JSON file to YAML."""
    # Create a temporary JSON file
    source_path = tmp_path / "test.json"
    source_content = {"name": "John", "age": 30, "city": "New York"}
    with open(source_path, "w", encoding=ENCODING) as source_file:
        json.dump(source_content, source_file)

    # Convert the JSON file to YAML
    target_path = tmp_path / "test.yaml"
    convert_file(source_path, target_path)

    # Check that the YAML file was created and has the correct content
    assert os.path.exists(target_path)
    with open(target_path, "r", encoding=ENCODING) as target_file:
        target_content = yaml.safe_load(target_file)
    assert target_content == source_content


def test_convert_file_invalid_json(tmp_path, capsys):
    """Test that the function raises an error for invalid JSON."""
    # Create a temporary file with invalid JSON content
    source_path = tmp_path / "test.json"
    with open(source_path, "w", encoding=ENCODING) as source_file:
        source_file.write("invalid json")

    # Convert the file and check that an error was raised
    target_path = tmp_path / "test.yaml"
    convert_file(source_path, target_path)
    assert "ERROR" in capsys.readouterr().out


def test_convert_file_target_exists(tmp_path, capsys):
    """Test that the function raises an error if the target file already exists."""
    # Create a temporary JSON file
    source_path = tmp_path / "test.json"
    source_content = {"name": "John", "age": 30, "city": "New York"}
    with open(source_path, "w", encoding=ENCODING) as source_file:
        json.dump(source_content, source_file)

    # Create a temporary YAML file
    target_path = tmp_path / "test.yaml"
    with open(target_path, "w", encoding=ENCODING) as target_file:
        target_file.write("existing content")

    # Convert the JSON file to YAML and check that an error was raised
    convert_file(source_path, target_path)
    assert "ERROR" in capsys.readouterr().out


def test_convert_file_source_not_found(tmp_path, capsys):
    """Test that the function raises an error if the source file is not found."""
    # Convert a non-existent file and check that an error was raised
    source_path = tmp_path / "nonexistent.json"
    target_path = tmp_path / "test.yaml"
    convert_file(source_path, target_path)
    assert "ERROR" in capsys.readouterr().out
