import sys


def always_string(value):
    """Regardless of the Python version, this always returns a string """
    return value.decode('utf-8') if sys.version > '3' else value