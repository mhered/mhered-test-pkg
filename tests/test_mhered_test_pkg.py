from pathlib import Path

import toml

import mhered_test_pkg


def test_versions_are_in_sync():
    """Checks if tool.poetry.version in pyproject.toml and
    __version__ in mhered_test_pkg.__init__.py are in sync."""

    path = Path(__file__).resolve().parents[2] / "pyproject.toml"
    pyproject = toml.loads(open(str(path)).read())
    pyproject_version = pyproject["tool"]["poetry"]["version"]

    init_py_version = mhered_test_pkg.__version__

    assert init_py_version == pyproject_version
