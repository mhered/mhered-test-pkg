---
typora-copy-images-to: assets
---

# mhered-test-pkg

A simple demo package to practice how to create python packages. 

Inspired in this article: https://mathspp.com/blog/how-to-create-a-python-package-in-2022

The code implements a simple Rock, Paper, Scissors text-based game. Inspired by Al Sweigart's  [Automate the boring stuff with Python](https://automatetheboringstuff.com/).

Installation:

```bash
$ pip install mhered-test-pkg
```

Usage:

```bash
$ python3 -m mhered_test_pkg
```



## How to create a python package 

### Pick a name

Check the name is available in [PyPI](https://pypi.org/)

### Initialize `poetry`

Install `poetry` (I started from [here](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) then modified the instructions):

 ```bash
$ curl -sSL https://install.python-poetry.org/ | python3 -
 ```

Create a local dedicated folder and initialize `poetry` inside

```bash
$ cd ~
$ mkdir mhered-test-pkg
$ cd mhered-test-pkg

$ poetry new .
Created package mhered_test_pkg in .

$ tree
.
├── mhered_test_pkg
│   └── __init__.py
├── pyproject.toml
├── README.rst
└── tests
    ├── __init__.py
    └── test_mhered_test_pkg.py
    
$ mv README.rst README.md
$ poetry install
```

Note: I renamed `README.rst` to `README.md` because I prefer to work in **Markdown**.

Note: Running `poetry install` creates a file `poetry.lock` with the dependencies

### Initialize git in the local folder

Create an empty github repo: **[mhered-test-pkg](https://github.com/mhered/mhered-test-pkg)** and follow the instructions to set it as the remote and push a first commit with the file structure:

```bash
$ git init
$ git add *
$ git commit -m "First commit"
$ git branch -M main
$ git remote add origin https://github.com/mhered/mhered-test-pkg.git
$ git push -u origin main
```

### Set up `pre-commit` hooks

  Add `pre-commit` as a development dependency, then commit updates:

```bash
$ poetry add -D pre-commit

$ git add poetry.lock pyproject.toml
$ git commit -m "Add pre-commit devt dependency."
```

Create a file `.pre-commit-config.yaml` in the root:

```yaml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
      - id: check-toml
      - id: check-yaml
      - id: end-of-file-fixer
      - id: mixed-line-ending
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/isort
    rev: 5.10.1
    hooks:
      - id: isort
        args: ["--profile", "black"]
```

Activate the `poetry` virtual environment to be able to use `pre-commit` then install the hooks and run them once: 

```bash
$ poetry shell

$ pre-commit install
$ pre-commit run all-files
```

Note: `pre-commit` is not found unless run from inside the shell - or you can use `poetry run pre-commit`

Commit the changes (including the updates to `README.md`):  

```bash
$ git add *
$ git commit -m "Run all pre-commits."
$ git push
```

Note: If some test fails, you need to add again the modified files and repeat the git commit - which is fine. But there is a strange behavior if the file was open: it seems to revert to an older version?

### Add a license

[Add a license from the github repo](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) then pull changes to local. 

This will add [LICENSE.md](./LICENSE.md)

### Upload the stub package to TestPyPI

Declare the test repository https://test.pypi.org in `poetry` and name it  `testpypi`:

```bash
$ poetry config repositories.testpypi https://test.pypi.org/legacy/
```

[Create an account on TestPyPI](https://test.pypi.org/account/register/), go to Account Settings to get an API token and then configure `poetry` to use it:

```bash
$ poetry config http-basic.testpypi __token__ pypi-YOUR-TESTPYPI-API-TOKEN
```

Note: Be careful not to expose your API token, e.g. I wrote it to a `secrets.md` file then used `.gitignore` so as not to commit and publish it publicly.

Build and upload the package:

```bash
$ poetry build
$ poetry publish -r testpypi
```

With this our package is live in TestPyPI: https://test.pypi.org/project/mhered-test-pkg/

<img src="assets/mhered-test-pkg.png" alt="mhered-test-pkg" style="zoom: 50%;" />

Note: Build creates the `dist/` folder that should be added to `.gitignore`

```bash
$ echo dist/ >> .gitignore

$ git add .
$ git commit -m "Publish to TestPyPI"
$ git push
```

### Populate the package with code

For this example I wrote a simple Rock, Paper, Scissors game inspired and slightly refactored from the example proposed by Al Sweigart in his great book [Automate the boring stuff with Python](https://automatetheboringstuff.com/). The code goes in `mhered-test-pkg/__init__.py`.

### Changelog management

Add [scriv](https://pypi.org/project/scriv/) for changelog management, as a development dependency with the `[toml]` extra :

```
$ poetry add -D scriv[toml]
```

Configure `scriv` to use **Markdown** and add version numbering in the title by adding the following lines to the `pyproject.toml` file, refer to [scriv's readthedocs](https://scriv.readthedocs.io/en/latest/configuration.html):

```toml
[tool.scriv]
format = "md"
version = "literal: pyproject.toml: tool.poetry.version"
```

Then create the default directory for changelog fragments `changelog.d/`. Note: add a `.gitkeep`  file so that git tracks the empty folder.

```
$ mkdir changelog.d
$ touch changelog.d/.gitkeep

$ scriv create

$ git add pyproject.toml poetry.lock changelog.d/.gitkeep
$ git commit -m "Add scriv as devt dependency."
```

Note: the command ` scriv create` creates a `.md` fragment file in the `changelog.d` folder. Add a description in the file:

```markdown
### Added

- A first simple implementation of Rock Paper Scissors
```

Lets update `README.md` and commit everything:

```bash
$ git add README.md changelog.d/* __init__.py
$ git commit -m "Simple Rock Paper Scissors game"
```

### Publish the package to PyPI

Create a [PyPI](https://pypi.org/) account and API token, and configure `poetry` to use it:

```bash
$ poetry config pypi-token.pipy pypi-YOUR-PYPI-API-TOKEN
```

Build and publish:

```bash
$ poetry publish --build
```

### Do a victory lap

Install, import and uninstall the package (outside of the shell) to check it works. Note: the hyphens (`-`) in the package name turn into underscores (`_`) in the module name.

```bash
$ pip install mhered-test-pkg
Defaulting to user installation because normal site-packages is not writeable
Collecting mhered-test-pkg
  Using cached mhered_test_pkg-0.1.0-py3-none-any.whl (2.5 kB)
Installing collected packages: mhered-test-pkg
Successfully installed mhered-test-pkg-0.1.0

$ python3 -m mhered_test_pkg
ROCK, PAPER, SCISSORS
0 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
r
ROCK versus... SCISSORS
You win!
1 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
q
Bye!

$ pip uninstall mhered-test-pkg
ROCK, PAPER, SCISSORS
0 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
r
ROCK versus... SCISSORS
You win!
1 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
q
Bye!
```

###  Publish a release

Add a description, installation and usage instructions in the `README.md` and declare it In `pyproject.toml`:

```toml
readme = "README.md"
```

Make `scriv` collect the previously created changelog fragment to a new `CHANGELOG.md` file with:

```bash
$ scriv collect
```

Lets commit: 

```bash
$ git add changelog.d/20220731_143829_manolo.heredia.md CHANGELOG.md README.md pyproject.toml
$ git commit -m "Prepare release 0.1.0"
```

Tag the commit, and push it to the remote (seen [here](https://stackabuse.com/git-push-tags-to-a-remote-repo/)):

```bash
$ git tag -a v0.1.0 -m "Initial version"
$ git push origin v0.1.0
```



I discovered I hadn't configured version numbering for scriv, so I did it now, and added a new release to test it.

First modify `pyproject.toml` to increment the version to `0.1.1` and have `scriv` read the version from `tool.poetry.version`:

```toml
[tool.poetry]
name = "mhered-test-pkg"
version = "0.1.1"
description = "A simple demo package to practice how to create python packages."
authors = ["Manuel Heredia <manolo.heredia@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.dev-dependencies]
pytest = "^5.2"
pre-commit = "^2.20.0"
scriv = {extras = ["toml"], version = "^0.16.0"}

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.scriv]
format = "md"
version = "literal: pyproject.toml: tool.poetry.version"
```

Next add a changelog fragment:

```bash
$ scriv create
```

and edit it to describe the change

```markdown
### Fixed

- Configure `scriv` to get version number from `pyproject.toml`
```

Bump version in `mhered-test-pkg/__init__.py` `__version__ = "0.1.1"`

Add a unit test to check it is always in sync with `tool.poetry.version` in `pyproject.toml` ([there seems to be no better way](https://github.com/python-poetry/poetry/issues/144#issuecomment-877835259))

```python
import toml
from pathlib import Path
import mhered_test_pkg

def test_versions_are_in_sync():
    """ Checks if tool.poetry.version in pyproject.toml and
    	__version__ in mhered_test_pkg.__init__.py are in sync."""

    path = Path(__file__).resolve().parents[2] / "pyproject.toml"
    pyproject = toml.loads(open(str(path)).read())
    pyproject_version = pyproject["tool"]["poetry"]["version"]

    init_py_version = mhered_test_pkg.__version__
    
    assert init_py_version == pyproject_version
```

Add a new changelog fragment:

```bash
$ scriv create
```

and edit it to describe the change

```markdown
## Added

- Test to check that versions defined in `pyproject.py` and `__init__.py` are in sync
```



Update the Changelog:

```
$ scriv collect

$ git add
$ git commit -m "Configure versions in scriv"

$ git tag -a v0.1.1 -m "Configure versions in scriv"
$ git push origin v0.1.1
```
