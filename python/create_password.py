#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create pseudo-random passwords with alphanumeric, numbers, and special characters."""
# version: 0.1.1
# license: MIT
# author: Anthony Pagan
# repo: https://github.com/get-tony/pyutils

import secrets
import string


def create_passwords(
    number_of_passwords: int, password_length: int
) -> list[str]:
    """Create a list of pseudo-random passwords.

    Args:
        number_of_passwords: The number of passwords to generate.
        password_length: The length of each password.

    Returns:
        A list of pseudo-random passwords.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    current_passwords = []
    for _ in range(number_of_passwords):
        current_password = "".join(
            secrets.choice(chars) for _ in range(password_length)
        )
        current_passwords.append(current_password)
    return current_passwords


if __name__ == "__main__":
    passwords = create_passwords(5, 20)
    print("# Random Passwords:")
    for password in passwords:
        print(password)
