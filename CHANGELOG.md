
<a id='changelog-0.1.10'></a>
# 0.1.10 — 2022-08-08

## Added

- Create linting and coverage environments in `tox.ini`

## Changed

- Move linting checks to `pre-commit`
- Run linting and coverage from `tox` under Python 3.8 only

## Fixed

- Review of `README.md`
- Review of `CHANGELOG.md`

<a id='changelog-0.1.8'></a>

# 0.1.8 — 2022-08-07

## Added

- New entry point `$ rps` to execute rock, paper, scissors game
- Badges in `README.md`

## Changed

- Moved code to `src/` folder

## Fixed

- In development module can be executed in two ways: `$ python3 -m src.mhered_test_pkg` or `$ python3 ./src/mhered_test_pkg/__main__.py`



<a id='changelog-0.1.7'></a>

# 0.1.7 — 2022-08-05

## Fixed

- Typo in `PyPI_publish.yaml`: `pypi_token.pypi` should be `pypi-token.pypi`

- Typo in `PyPI_publish.yaml`: `uses: poetr build --publish` should be `run:`

<a id='changelog-0.1.5'></a>

# 0.1.5 — 2022-08-05

## Fixed

- Typo in `PyPI_publish.yaml`: `PyPI_TOKEN` should be  `PYPI_TOKEN`  

<a id='changelog-0.1.4'></a>

# 0.1.4 — 2022-08-04

## Added

- Github action `CI.yaml` to run `tox` for CI on push and pull requests
- **Codecov** integration
- `PyPI_publish.yaml` to publish releases to **PyPI**

<a id='changelog-0.1.3'></a>

# 0.1.3 — 2022-08-03

## Added

- Automated formatting, linting, testing and coverage with `tox`
- `README.md` sections on `tox` and `coverage`

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
