******************************************************
Poetryパッケージ管理
******************************************************
Last Updated on |date|

仮想環境+パッケージ管理ツール

`公式サイト <https://python-poetry.org/>`_ 


基本コマンド
=============
:バージョン確認: poetry --version
:設定確認: poetry config --list
:venv分離: poetry config virtualenvs.in-project true
:新規PKG: poetry new
:pyproject.toml作成: poetry init
:pyproject.tomlベースにinstall: poetry installpo
:依存PKGを最新化: poetry update
:PKG追加: poetry add [pkg]
:開発者PKG追加: poetry add --dev [pkg]
:GITHUBのPKGを追加: poetry add git+https://github.com/repo/pkg.git
:PKG削除: poetry remove [pkg]
:poetry自体のupdate: poetry self update

インストール
=================

`インストール手順 <https://python-poetry.org/docs/#installation`_ 

.. hint:: :kbd:`pip install --user poetry`  の利用はpoetry self update ができないので注意

基本設定
====================
in-projectはTrueにしておくことをオススメ。該当プロジェクトに閉じて管理できる。

venv環境を独立するためのconfig確認・設定::

	poetry config --list
	poetry config virtualenvs.in-project true

2021/04/17実施
---------------
インストールコマンド::

  PS C:\WINDOWS\system32> (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
  Retrieving Poetry metadata
  
  # Welcome to Poetry!
  
  This will download and install the latest version of Poetry,
  a dependency and package manager for Python.
  
  It will add the `poetry` command to Poetry's bin directory, located at:
  
  %USERPROFILE%\.poetry\bin
  
  This path will then be added to your `PATH` environment variable by
  modifying the `HKEY_CURRENT_USER/Environment/PATH` registry key.
  
  You can uninstall at any time by executing this script with the --uninstall option,
  and these changes will be reverted.
  
  Installing version: 1.1.6
    - Downloading poetry-1.1.6-win32.tar.gz (52.15MB)
  
  Poetry (1.1.6) is installed now. Great!
  
  To get started you need Poetry's bin directory (%USERPROFILE%\.poetry\bin) in your `PATH`
  environment variable. Future applications will automatically have the
  correct environment, but you may need to restart your current shell.

.. hint:: 環境変数などは自動で置き換わる。ターミナルは再起動が必要。


poetry self updateコマンド実行
------------------------------------------------------------
1.1.6 から 1.1.7へのself updateが、エラーとなりました。(2021/08/14)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. error:: 
  
  ModuleNotFoundError: No module named 'msgpack.exceptions'

.. hint::
  %USERPROFILE%\.poetry フォルダを削除し、推奨手順で再インストールしたら復旧できました。


1.1.7から1.1.8へのself updateが、エラーとなりました。(2021/08/22)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. error:: 

  ModuleNotFoundError: No module named 'crashtest.inspector'

.. hint::
  | %USERPROFILE%\.poetry フォルダを削除し、推奨手順で再インストールしたら復旧できました。
  | issueが出てますね。修正待ちです。
  | https://github.com/python-poetry/poetry/issues/2681

.. |date| date::
