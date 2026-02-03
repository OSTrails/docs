import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent / '_ext'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OSTrails'
release = '0.1.0'

master_doc = 'index'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.openapi',
    # custom extensions:
    'authors',
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# sphinxcontrib.openapi
http_strict_mode = False

# sphinxcontrib.bibtex
bibtex_bibfiles = ['references.bib']
bibtex_reference_style = 'author_year'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

color_purple = '#745BA3'
color_orange = '#EE7544'

html_theme = 'furo'
html_static_path = ['_static']
html_title = 'OSTrails Documentation'
html_favicon = '_static/img/icon.png'
html_theme_options = {
    "light_logo": "img/logo.svg",
    "dark_logo": "img/logo-white.svg",
    "light_css_variables": {
        "color-brand-primary": color_orange,
        "color-brand-content": color_purple,
        "font-stack": "Quicksand, Montserrat, Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
        'sidebar-item-spacing-horizontal': '.75rem',
    },
    "dark_css_variables": {
        "color-brand-primary": color_orange,
        "color-brand-content": color_purple,
        "font-stack": "Quicksand, Montserrat, Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
        'sidebar-item-spacing-horizontal': '.75rem',
    },
    'sidebar_hide_name': True,
    'top_of_page_buttons': [],
}
html_css_files = ['custom.css']
html_js_files = ['custom.js']
html_show_copyright = False
