
<a id='changelog-0.1.6'></a>
# 0.1.6 — 2022-08-05

## Fixed

- Bug: In PyPI_publish.yaml replace `uses: poetr build --publish` with `run:`


<a id='changelog-0.1.5'></a>
# 0.1.5 — 2022-08-05

## Fixed

- Incorrect call to PYPI_TOKEN in GH action PyPI_publish.yaml

<a id='changelog-0.1.4'></a>
# 0.1.4 — 2022-08-04

## Added

- Github Action CI.yaml to run tox for CI on push and pull requests
- Codecov integration
- PyPI_publish.yaml to publish releases to PyPI

<a id='changelog-0.1.3'></a>

# 0.1.3 — 2022-08-03

## Added

- Automated formatting, linting, testing and coverage with tox
- README.md sections on tox and coverage

- Tests coverage 97%

## Changed

- Refactor code into testable functions

<a id='changelog-0.1.2'></a>
# 0.1.2 — 2022-08-01

## Added

- Basic tests
<a id='changelog-0.1.1'></a>

# 0.1.1 — 2022-08-01

## Added

- Test to check that versions defined in `pyproject.py` and `__init__.py` are in sync

## Fixed

- Configure `scriv` to get version number from `pyproject.toml`
<a id='changelog-0.1.0'></a>

# 0.1.0 — 2022-07-31

## Added

- A first simple implementation of Rock Paper Scissors
