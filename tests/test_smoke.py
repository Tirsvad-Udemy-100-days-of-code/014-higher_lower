"""@file test_smoke.py
@brief Smoke test: the package and its entry point can be imported.
"""

import higher_lower
from higher_lower import __main__ as entry_point


def test_package_imports() -> None:
    """@brief The package imports without side effects."""
    assert higher_lower.__doc__


def test_entry_point_is_callable() -> None:
    """@brief The entry point exists; importing it does not start a game."""
    assert callable(entry_point.main)
