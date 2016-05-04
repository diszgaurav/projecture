# projecture
Projecture is a project scaffolding(or a minimal bootstrap) generation tool for various projects (see list of supported project types below). Correctly structuring your project (i.e. some defined standard way or a way which is widely acceptable to the related community) makes things easy for you, for contributors and for your users.

## List of supported project types:
- python

# Installation

```bash
pip install projecture
```

# Usages

projecture installation creates a projecture_create executable in your path. Create a new project from command line as:

```bash
projecture_create pyproject -t python -n "your name" -e "your email" -a "project generated from projecture"
```

or from python:

```python
import projecture
projecture.create_project('pyproject',
                          project_type='python',
                          author_name='your name',
                          author_email='your_email',
                          about='project generated from projecture',
                          force=True)
```

This will create pyproject dir in your current working dir.

# Projects

## Python

Python project generates following structure:

```bash
pyproject/                      # your project root (project_dir)
├── LICENSE                     # default license file with MIT license
├── MANIFEST.in                 # file to include non-package data
├── pyproject                   # your actual python package; will be referred as package_dir further
│   ├── cmdline.py              # command line interface script for the package
│   ├── __init__.py
│   ├── pyproject.py            # package's main file
│   └── tests                   # dir containing package tests
│       ├── __init__.py
│       ├── test_pyproject.py   #
├── README.md                   # README file (markdown format)
├── README.rst                  # restructured format README for tools like Sphinx
├── requirements.txt            # file to contain dependencies
├── setup.py                    # setup tools script to package/install project
```
