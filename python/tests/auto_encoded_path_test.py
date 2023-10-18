#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the AutoEncodedPath class."""
# license: MIT
# author: Anthony Pagan
# email: get-tony@outlook.com

import tempfile
import os
from auto_encoded_path import AutoEncodedPath


def test_read_text() -> None:
    """Test the read_text method of the AutoEncodedPath class."""
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = os.path.join(temp_dir, "test.txt")
        with open(test_file, "w", encoding="utf-8") as file:
            file.write("Hello, world!")
        path = AutoEncodedPath(test_file)
        contents = path.read_text()
        assert contents == "Hello, world!"


def test_write_text() -> None:
    """Test the write_text method of the AutoEncodedPath class."""
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = os.path.join(temp_dir, "test.txt")
        path = AutoEncodedPath(test_file)
        path.write_text("Goodbye, world!")
        with open(test_file, "r", encoding="utf-8") as file:
            contents = file.read()
        assert contents == "Goodbye, world!"


def test_open() -> None:
    """Test the open method of the AutoEncodedPath class."""
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = os.path.join(temp_dir, "test.txt")
        with open(test_file, "w", encoding="utf-8") as file:
            file.write("Hello, world!")
        path = AutoEncodedPath(test_file)
        with path.open() as file:
            contents = file.read()
        assert contents == "Hello, world!"
