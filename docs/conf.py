# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'mtakagishi'
copyright = '2021, mtakagishi'
author = 'mtakagishi'

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y/%m/%d'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'recommonmark',
    'sphinx_sitemap',
    'sphinxnotes.strike',
    'sphinxcontrib.blockdiag',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = 'ja'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_favicon = "_static/favicon.ico"
# html_logo = "_static/logo.png"
html_theme_options = {
    "github_url": "https://github.com/mtakagishi/mtakagishi",
    "twitter_url": "https://twitter.com/mtakagishi",
    # "google_analytics_id": "UA-183061927-2",
    "navbar_end": ["navbar-icon-links.html"],
    "footer_items": ["copyright"],
    "external_links": [
        {"name": "ゆる言語学ラジオメモ",
         "url": "https://yurugengo.mtakagishi.com"},
        {"name": "ノート", "url": "https://note.mtakagishi.com"}
    ]
}
html_sidebars = {
    "**": []
}

[extensions]
todo_include_todos = True

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
# sphinx-sitemap
html_baseurl = 'https://mtakagishi.com/'
html_extra_path = ['robots.txt']

# blockdiag
blockdiag_html_image_format = 'SVG'
blockdiag_fontpath = 'docs/ipaexg.ttf'
