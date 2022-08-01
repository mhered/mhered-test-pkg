from pathlib import Path

import toml

from mhered_test_pkg import __version__, move_msg


def test_versions_are_in_sync():
    """Checks if tool.poetry.version in pyproject.toml and
    __version__ in mhered_test_pkg.__init__.py are in sync."""

    path = Path(__file__).resolve().parents[1] / "pyproject.toml"
    pyproject = toml.loads(open(str(path)).read())
    pyproject_version = pyproject["tool"]["poetry"]["version"]

    init_py_version = __version__

    assert init_py_version == pyproject_version


def test_move_msg_r():
    """Checks message for r is ROCK"""
    assert move_msg("r") == "ROCK"


def test_move_msg_p():
    """Checks message for p is PAPER"""
    assert move_msg("p") == "PAPER"


def test_move_msg_s():
    """Checks message for s is SCISSORS"""
    assert move_msg("s") == "SCISSORS"
