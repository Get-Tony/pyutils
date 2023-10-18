#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the YAML to JSON converter module."""
# license: MIT
# author: Anthony Pagan
# email: get-tony@outlook.com

import json
import sys
import pytest

from yaml_to_json import convert_directory, convert_file


# pylint: disable=redefined-outer-name

# Define system encoding
ENCODING: str = sys.getfilesystemencoding() or sys.getdefaultencoding()


@pytest.fixture
def yaml_file(tmp_path):
    """Create a temporary YAML file."""
    yaml_file = tmp_path / "test.yaml"
    yaml_file.write_text("name: Test\n")
    return yaml_file


@pytest.fixture
def json_file(tmp_path):
    """Create a temporary JSON file."""
    json_file = tmp_path / "test.json"
    return json_file


def test_convert_file(yaml_file, json_file):
    """Test that the function converts a YAML file to JSON."""
    convert_file(yaml_file, json_file)
    with open(json_file, "r", encoding=ENCODING) as open_json_file:
        json_content = json.load(open_json_file)
    assert json_content == {"name": "Test"}


def test_convert_directory(yaml_file, json_file, tmp_path):
    """Test that the function converts all YAML files in a directory to JSON."""
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    target_dir = tmp_path / "target"
    target_dir.mkdir()
    yaml_file_2 = source_dir / "test2.yaml"
    yaml_file_2.write_text("name: Test 2\n")
    convert_file(yaml_file, json_file)
    convert_directory(source_dir, target_dir)
    with open(json_file, "r", encoding=ENCODING) as open_json_file_1:
        json_content = json.load(open_json_file_1)
    assert json_content == {"name": "Test"}
    with open(
        target_dir / "test2.json", "r", encoding=ENCODING
    ) as open_json_file_2:
        json_content_2 = json.load(open_json_file_2)
    assert json_content_2 == {"name": "Test 2"}
