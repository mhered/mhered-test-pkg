# mhered-test-pkg

`mhered-test-pkg` is a simple package to demonstrate how to create a python package. 

Inspired in this article: https://mathspp.com/blog/how-to-create-a-python-package-in-2022

## How to

### Pick a name

Check the name is available in [PiPy](https://pypi.org/)

### Initialize `poetry`

Install poetry (modified the instructions starting from [here](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions)):

 ```bash
$ curl -sSL https://install.python-poetry.org/ | python3 -
 ```

Create a dedicated folder locally and initialize poetry inside

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

Note: I renamed README.rst to README.md because I prefer to work in Markdown.

Running `poetry install` creates a file `poetry.lock` with the dependencies

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

Activate the `poetry` virtual environment to be able to use `pre-commit` then install the hooks and then we run them once, just for good measure. 

```bash
$ poetry shell

$ pre-commit install
$ pre-commit run all-files
```

Note: `pre-commit` is not found if run from outside of the shell - you can use instead `poetry run pre-commit`

Commit the changes (including the updates to `README.md`):  

```bash
$ git add *
$ git commit -m "Run all pre-commits."
$ git push
```

Note: behavior is a bit strange. if some test fails, you need to add modified files and repeat the git commit - which is fine - but then if the file was open it seems to revert to an older version?

## Add a license

[Add a license from github](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) then pull changes to local. 

This will add [LICENSE.md](./LICENSE.md)
