==========================================================================================
Sphinxのsitemapを構築する
==========================================================================================
Last Updated on |date|

追加パッケージ
---------------------------------
sphinx-sitemap::

  poetry add sphinx-sitemap

conf.pyの設定例
---------------------------------

conf.py::

  # 以下を追記します。
  extensions = ['sphinx_sitemap']

  html_baseurl = 'https://mtakagishi.tk/'
  html_extra_path = ['robots.txt']


検索エンジンクローラ対応
---------------------------------
  
conf.pyと同じ階層に、robots.txt を配置しておく。

robots.txt::

  user-agent: *
  
  sitemap: https://mtakagishi.tk/sitemap.xml




.. |date| date::