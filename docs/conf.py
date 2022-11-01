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
import os
import sys


# -- Project information -----------------------------------------------------

project = 'Label Sleuth'
copyright = '2022, Label Sleuth'
author = 'Label Sleuth'

import pydata_sphinx_theme

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
   'sphinx.ext.autodoc',
   'sphinx.ext.coverage',
   'sphinx.ext.napoleon',
   'sphinx.ext.autosummary',
   'sphinx.ext.intersphinx',
   'sphinx.ext.viewcode',
   'sphinx.ext.todo',
   'notfound.extension',
   'myst_parser',
   'sphinx_copybutton',
   'sphinx_design',
   'sphinx_togglebutton'
]

myst_enable_extensions = ["colon_fence"]

# Add no prefix to resource URLs for 404 page
notfound_urls_prefix = ''

# Automatically create header anchors for h1, h2, and h3 level headings
myst_heading_anchors = 3

html_title = 'Label Sleuth'

html_css_files = ["css/custom.css"]

html_js_files = ['js/custom.js']

source_suffix = ['.rst', '.md']

add_module_names = False

# Enable todo directive
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_logo = "_static/images/homepage/logo_white.svg"
html_theme_options = {
  "icon_links": [
     {
        "name": "GitHub",
        "url": "https://github.com/label-sleuth/label-sleuth",
        "icon": "fab fa-github",
        "type": "fontawesome"
      },
      {
        "name": "Slack",
        "url": "https://join.slack.com/t/labelsleuth/shared_invite/zt-1h1exje12-wuSTcktxUVHefZgAZ9bEiQ",
        "icon": "fab fa-slack",
        "type": "fontawesome"
      }
  ],
  "favicons": [
    {
        "rel": "icon",
        "sizes": "37x37",
        "href": "images/homepage/fav.ico",
    }
  ],
  "navbar_align": "right",
  "use_edit_page_button": True,
  "navbar_end": ["navbar-icon-links"],
  "show_prev_next": False,
  "show_nav_level": 2,
}

html_context = {
  "default_mode": "light",
  "github_url": "https://github.com",
  "github_user": "label-sleuth",
  "github_repo": "label-sleuth.org",
  "github_version": "main",
  "doc_path": "docs",
}

html_sidebars = {
  "index": []
}

html_additional_pages = {'index': 'index.html'}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
