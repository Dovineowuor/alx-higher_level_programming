#!/usr/bin/python3
# 0-read_file.py
"""Defines a text file-reading function."""


def number_of_lines(filename=""):
    def read_file(filename=""):
        with open(filename, "r", encoding="UTF-8") as f:
            return len(list(f))
        """Print the contents of a UTF8 text file to stdout."""
        with open(filename, encoding="utf-8") as f:
            print(f.read(), end="")