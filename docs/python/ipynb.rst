*********************************************
ipynb拡張子を参照する
*********************************************
Last Updated on |date|

前提
=================
* pythonとpoetryコマンドが使える状況
* jupyterがインストールされてない。
* jupyterで開けば何とかなる

手順
================
* cd [ipynbファイルのあるフォルダ]
* poetry init
* poetry install
* poetry add jupyter
* poetry run jupyter notebook

これで既定のブラウザでjupyterが開くのでipynbが参照できる。

.. |date| date::