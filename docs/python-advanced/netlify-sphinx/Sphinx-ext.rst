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

.. attention:: 

  | pydata-sphinx-theme の対応方法です。
  | 各テーマに合わせて対応してください。

analytics.js方式（旧）
-------------------------

conf.py::

  html_theme_options = {
      "google_analytics_id": "UA-XXXXXXX",
  }

gtag.js方式（新）
-------------------------

* conf.py の template_path の設定を確認
* layout.htmlを用意し、template_path配下に作成。

layout.html::

  {% extends "pydata_sphinx_theme/layout.html" %}
  {%- block htmltitle %}
  <title>{{ title|striptags|e }}{{ titlesuffix }}</title>
  <!-- Global site tag (gtag.js) - Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-XXXXXXXXXX');
  </script>
  {%- endblock %}

