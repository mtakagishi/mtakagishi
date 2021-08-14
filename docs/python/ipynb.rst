*********************************************
ipynbが開けないときの対処方法
*********************************************
Last Updated on |date|

* ipynb拡張子は、jupyterのファイルです。
* 端末を変えたり、しばらく放置すると、開き方を忘れて読めなくてハマります。
* ここでは応急処置をまとめました。


前提
=================
* pythonとpoetryコマンドが使える状況
* jupyterがインストールされてない or 開き方がわからない
* 端末のPython環境をあまり汚したくない
* とにかくjupyterで開けば何とかなる。

手順
================
* cd [ipynbファイルのあるフォルダ]
* poetry config virtualenvs.in-project true
* poetry init
* poetry install
* poetry add jupyter
* poetry run jupyter notebook

これで既定のブラウザでjupyterが開くのでipynbが参照できる。

.. |date| date::