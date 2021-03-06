*****************************
Python環境の準備
*****************************
Last Updated on |date|

Python仮想環境準備
===========================
Pythonは事前にインストールしておく。今回は、Python環境をキレイに保つために仮想環境で分離。 `poetry`_ を利用しました。

poetryのインストール::

	pip install --user poetry

.. hint::
  poetryインストールは、上記のような方法でもよいが、poetry推奨ではない。
  poetry推奨方法だとバージョンアップに追随できるため、公式を参照されたい。
  → `公式インストール <https://python-poetry.org/docs/#installation>`_ 

venv環境を独立するためのconfig確認・設定::

	poetry config --list
	poetry config virtualenvs.in-project true

pyproject.tomlの作成::

	poetry init

仮想環境の作成::

	poetry install

.venvフォルダが作成され、以後、poetry add コマンドでパッケージを追加できます。

Pythonコードも触るかもしれないので下記を念のため追加

	poetry add --dev flake8 autopep8 pylint

.. _poetry: https://python-poetry.org/
.. |date| date::