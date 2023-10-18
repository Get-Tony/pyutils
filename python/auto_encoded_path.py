#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Path subclass that uses the system encoding by default."""
# version: 0.1.3
# license: MIT
# author: Anthony Pagan
# email: get-tony@outlook.com

import sys
import io
from typing import override
from pathlib import Path


class AutoEncodedPath(Path):
    """Path subclass that uses the system encoding by default."""

    local_encoding: str = (
        sys.getfilesystemencoding() or sys.getdefaultencoding()
    )

    @override
    def read_text(self, encoding: str = None, errors: str = None) -> str:
        """Read the file and return the contents as a string."""
        if encoding is None:
            encoding = self.local_encoding
        return super().read_text(encoding=encoding, errors=errors)

    @override
    def write_text(
        self,
        data: str,
        encoding: str = None,
        errors: str = None,
        newline: str = None,
    ) -> None:
        """Write a string to the file."""
        if encoding is None:
            encoding = self.local_encoding
        return super().write_text(
            data=data, encoding=encoding, errors=errors, newline=newline
        )

    @override
    def open(  # pylint: disable=too-many-arguments
        self,
        mode: str = "r",
        buffering: int = -1,
        encoding: str = None,
        errors: str = None,
        newline: str = None,
    ) -> "io.TextIOWrapper":
        """Open the file and return a corresponding file object."""
        if encoding is None:
            encoding = self.local_encoding
        return super().open(
            mode=mode,
            buffering=buffering,
            encoding=encoding,
            errors=errors,
            newline=newline,
        )
