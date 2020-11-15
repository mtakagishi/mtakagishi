***********************
Sphinx拡張設定
***********************

TODOを記録する
========================

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

マークダウンを扱えるようにする
========================================
.. todo:: マークダウンを扱えるようにする
