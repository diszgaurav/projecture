projecture
==========

Projecture is a project scaffolding(or a minimal bootstrap) generation
tool for various projects (see list of supported project types below).
Correctly structuring your project (i.e. some defined standard way or a
way which is more acceptable to the related community) makes things easy
for you, for contributors and for your users.

List of supported project types:
--------------------------------

-  python

Installation
============

.. code:: bash

    pip install projecture

Usages
======

projecture installation creates a projecture\_create executable in your
path. Create a new project from command line as:

.. code:: bash

    projecture_create pyproject --author_name "your name" --author_email "your email" --about "project generated from projecture"

or from python:

.. code:: python

    import projecture
    projecture.create_project('pyproject', author_name='your name', author_email='your_email', about='project generated from projecture')

This will create pyproject dir in your current working dir.
