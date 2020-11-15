***********************
Sphinx拡張設定
***********************
| netlifyまででサイトは管理は問題なし
| その後行った拡張など

TODOを記録できるようにする
===============================

設定
-----------
conf.py::

  extensions = ['sphinx.ext.todo' ]

  [extensions]
  todo_include_todos=True

使い方
----------

todoを書く::

  .. todo:: todo-text

todoをリストアップする::

  .. todolist::


Googleアナリティクス設定
=================================

conf.py::

  html_theme_options = {
      "google_analytics_id": "UA-XXXXXXX",
  }

.. attention:: pydata-sphinx-theme 限定


マークダウンを扱えるようにする
========================================
.. todo:: マークダウンを扱えるようにする
