Contributing Guidelines
=======================

.. page-authors::
    Marek Suchanek
    John Shepherdson


Thank you for considering contributing to the OSTrails documentation! We welcome contributions from everyone, regardless of your level of experience. This document outlines the process for contributing to the documentation.

Ways of Contributing
--------------------

- **Reporting Issues**: If you find a bug in the documentation, please open an issue on the GitHub repository.
- **Suggesting Enhancements**: If you have an idea for improving the documentation, please open an issue on the GitHub repository.
- **Improving the Documentation**: If you would like to improve the documentation, please follow the process outlined below.

Issue Reporting
---------------

If you find a bug in the documentation, please `open an issue <https://github.com/ostrails/docs/issues/new/choose>`_ in the GitHub repository. When reporting an issue, please follow the requested information for given issue templates.

Documentation
-------------

The documentation is hosted on Read-the-Docs and using standard Sphinx documentation. The documentation is written in reStructuredText (``.rst``) format. It can be compiled locally using Sphinx and viewed in a web browser.

Writing Style
^^^^^^^^^^^^^

When contributing to the documentation, please follow the following writing style:

- Use British English.
- Use the active voice.
- Use the present tense.
- Use the imperative mood for commands.

For more information on ReStructuredText syntax, please refer to the `official documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_. In this documentation, we use ``=`` underline for headings, ``-`` underline for subheadings, and ``^`` underline for subsubheadings.

We also use the following extensions:

- ``sphinxcontrib.bibtex`` for managing bibliographies (see `sphinxcontrib.bibtex docs <https://sphinxcontrib-bibtex.readthedocs.io/en/latest/>`_)
- ``sphinxcontrib.openapi`` for rendering OpenAPI specifications (see `sphinxcontrib.openapi docs <https://sphinxcontrib-openapi.readthedocs.io/>`_)

All bibliographical references should be added to the ``references.bib`` file in the ``docs`` directory. A record need to contain all required fields according to the `BibTeX format <https://www.bibtex.com/e/entry-types/>`_.

The code style is captured using `EditorConfig <https://editorconfig.org/>`_, see ``.editorconfig`` file. Please ensure that your editor supports EditorConfig. It is also checked using CI together with the absence of warnings.

Building the Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^

First, install the required dependencies (preferably in a virtual environment):

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate

    pip install -r requirements.txt


Then, you can build the documentation using the following command:

.. code-block:: bash

    cd docs
    make html


Once built, you can view the documentation by opening the ``index.html`` file in the ``_build/html`` directory in a web browser.

Way of Working
--------------

The following part describes the way of working when contributing to the documentation. Always also comply to the ``CODE_OF_CONDUCT.md`` when contributing (based on `Contributor Covenant <https://www.contributor-covenant.org/>`_).

Commit Messages
^^^^^^^^^^^^^^^

Please follow the `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ specification when writing commit messages. This will help us to automatically generate the changelog.

For instance, the following commit message:

.. code-block:: none

    feat: add new extension to the documentation
    docs: update framework general description
    deps: update dependencies
    fix: correct typos


Branching and Pull Requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When contributing to the documentation, please follow these steps:

1. Fork the repository (if not in the OSTrails organisation).
2. Create a new branch for your changes (base = `next``).
3. Make your changes and commit them.
4. Push your changes.
5. Open a pull request to the ``next`` branch of the main repository.

Crediting Contributors
^^^^^^^^^^^^^^^^^^^^^^

We will credit all contributors in the documentation. If you would like to be credited, please add your name and related information to the ``CONTRIBUTORS.yml`` file.

Then, you can add your name to the list of contributors for a specific page:

.. code-block:: rst

    Page Title
    ==========

    .. page-authors::
        Jane Smith
