# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "event-driven-acquisition"
copyright = "2022, Willi L. Stepp"
author = "Willi L. Stepp"

release = "0.1"
version = "0.1.0"

# -- General configuration

import os
import sys


autodoc_mock_imports = [
    "PyQt5",
    "numpy",
    "tensorflow",
    "pycromanager",
    "zmq",
    "pyqtgraph",
    "pycromanager",
    "qdarkstyle",
    "qimage2ndarray",
]

sys.path.insert(0, os.path.abspath(os.path.join("..", "..")))


extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

autosummary_generate = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = "footnote"
