#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the create_password module."""
# license: MIT
# author: Anthony Pagan
# repo: https://github.com/get-tony/pyutils

import string
from create_password import create_passwords


def test_create_passwords_length():
    """Test that the function returns the correct number of passwords,
    and that each password has the correct length."""
    passwords = create_passwords(5, 20)
    assert len(passwords) == 5
    for password in passwords:
        assert len(password) == 20


def test_create_passwords_characters():
    """Test that each password only contains characters from the allowed
    set of characters (letters, digits, and punctuation)."""
    passwords = create_passwords(5, 20)
    chars = set(string.ascii_letters + string.digits + string.punctuation)
    for password in passwords:
        assert set(password) <= chars
