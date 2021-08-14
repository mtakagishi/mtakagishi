==========================================================================================
SphinxにGoogle Analyticsのタグを埋め込む方法
==========================================================================================
Last Updated on |date|

.. note:: 

  | 当サイトが採用するpydata_sphinx_themeをベースにした記事です。
  | htmltitleブロックを拡張する方法を取りましたが、
  | "basic/layout.html" からの派生テーマなら同じ方法で行けるはずです。
  | ご利用のテーマの構成を確認のうえ参考にしてください。

* conf.py の template_path の設定を確認
* layout.htmlを用意し、template_path配下に作成。
* googleアナリティクス設定の「ウェブストリームの詳細」画面を参考に下記のように「layout.html」格納

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


.. |date| date::