#################################################
rst入門
#################################################
Last Updated on |date|

reStructuredTextに関するメモ

*******
入門
*******

基本情報
=================================
* RST、reST、ReST
* Python製

参考URL
=================================
* https://docutils.sphinx-users.jp/docutils/docs/ref/rst/restructuredtext.html
* https://www.sphinx-doc.org/ja/master/usage/restructuredtext/basics.html
* https://devguide.python.org/documenting/#additional-markup-constructs
* https://developer.lsst.io/restructuredtext/style.html

セクション
=================================

パラグラフ
=================================
段落の塊は、1行以上の空行で区切る


インラインマークアップ
=================================
文章内で利用できる装飾

ボールド
--------------------------
\*\*太文字\*\* ⇒ **太文字**


コードサンプル
--------------------------
\`\`コードサンプル\`\` ⇒ ``コードサンプル``

数式
--------------------------
\:math\:\`\\sqrt\{16\}\` ⇒ :math:`\sqrt{16}`

リテラルブロック
=================================
リテラルブロック\:\:
  リテラルブロック内容

出力結果
-------------
リテラルブロック::

  It is not processed in any way, except
  that the indentation is removed.
  
  It can span multiple lines.

リスト
=================================
箇条書き
-------------------------------
箇条書き::

  * this is
  * a list

    * with a nested list
    * and some subitems

  * and here the parent list continues

箇条書き(表示）

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

番号付き
-------------------------------

番号付き::

  1. This is a numbered list.
  2. It has two items too.

  #. This is a numbered list.
  #. It has two items too.

番号付き(表示)

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

用語
-------------------------------

用語::

  term1
    Definition 1.

  term2
    Definition 2, paragraph 1.

    Definition 2, paragraph 2.

  term3 : classifier
    Definition 3.

  term4 : classifier one : classifier two
    Definition 4.

用語(表示)

term1
  Definition 1.

term2
  Definition 2, paragraph 1.

  Definition 2, paragraph 2.

term3 : classifier
  Definition 3.

term4 : classifier one : classifier two
  Definition 4.

項目リスト
-------------------------------

項目リスト::

  :fieldname1: Field content
  :fieldname12: Field content
  :fieldname123: Field content
  :fieldname1234: Field content


項目リスト(表示)

:fieldname1: Field content
:fieldname12: Field content
:fieldname123: Field content
:fieldname1234: Field content

リンク
=================================
外部リンク
-------------------------------
内部リンク
-------------------------------


テーブル
=================================
VSCode拡張
-------------------------------
Table Formatter　が便利

:kbd:`Ctrl` + :kbd:`P` から『Table: Format Current』

グリッド
-------------------------------
Table Fromatter::

  +
  ||Mon|Tue|Wed|Thu|Fri|
  +=
  |田中|(^^)|(xx)|(xx)|('')|(^^)|
  +-
  |鈴木|(^^)|(^^)|('')|(xx)|(^^)|
  +

フォーマット後::

  +------+------+------+------+------+------+
  |      | Mon  | Tue  | Wed  | Thu  | Fri  |
  +======+======+======+======+======+======+
  | 田中 | (^^) | (xx) | (xx) | ('') | (^^) |
  +------+------+------+------+------+------+
  | 鈴木 | (^^) | (^^) | ('') | (xx) | (^^) |
  +------+------+------+------+------+------+

実際の表示

+------+------+------+------+------+------+
|      | Mon  | Tue  | Wed  | Thu  | Fri  |
+======+======+======+======+======+======+
| 田中 | (^^) | (xx) | (xx) | ('') | (^^) |
+------+------+------+------+------+------+
| 鈴木 | (^^) | (^^) | ('') | (xx) | (^^) |
+------+------+------+------+------+------+


シンプル
-------------------------------

Table Fromatter::

  =
  Input . Output
  -
  A B "A or B" A_and_B
  = = = =
  False False False False
  True False True False
  =

フォーマット後::

  =====  =====  ========  =======
  Input    .     Output
  -----  -----  --------  -------
    A      B    "A or B"  A_and_B
  =====  =====  ========  =======
  False  False  False     False
  True   False  True      False
  =====  =====  ========  =======


実際の表示

=====  =====  ========  =======
Input    .     Output
-----  -----  --------  -------
  A      B    "A or B"  A_and_B
=====  =====  ========  =======
False  False  False     False
True   False  True      False
=====  =====  ========  =======

ディレクティブ
=================================
プログラミングでは「指示」を示す言葉として使われる。Sphinxでは指示のあるブロック

スニペット
=================================
reStructuredText という拡張についているスニペットを紹介

code
------------------------------------
ディレクティブ表記::

  .. code-block:: shell

    echo Hello world

レンダリング後:

.. code-block:: shell

  echo Hello world


image
------------------------------------
ディレクティブ表記::
  
  .. image:: https://unsplash.it/336/280/?random

レンダリング後:

.. image:: https://unsplash.it/336/280/?random

figure
------------------------------------
ディレクティブ表記::

  .. figure:: path
  
レンダリング後:

link
------------------------------------
ディレクティブ表記::

  `Title <http://link>`_ 

レンダリング後:

`Title <http://link>`_ 

attention
------------------------------------
ディレクティブ表記::

  .. attention:: text

レンダリング後:

.. attention:: text

note
------------------------------------
ディレクティブ表記::

  .. note:: text
  
レンダリング後:

.. note:: text


warning
------------------------------------
ディレクティブ表記::

  .. warning:: text

レンダリング後:

.. warning:: text


error
------------------------------------
ディレクティブ表記::

  .. error:: text
  
レンダリング後:

.. error:: text


hint
------------------------------------
ディレクティブ表記::

  .. hint:: text
  
レンダリング後:

.. hint:: text


important
------------------------------------
ディレクティブ表記::

  .. important:: text
  

レンダリング後:

.. important:: text


caution
------------------------------------
ディレクティブ表記::

  .. caution:: text
  
レンダリング後:

.. caution:: text


danger
------------------------------------
ディレクティブ表記::

  .. danger:: text
  
レンダリング後:

.. danger:: text


tip
------------------------------------
ディレクティブ表記::

  .. tip:: text
  

レンダリング後:

.. tip:: text


admonition
------------------------------------
ディレクティブ表記::

  .. admonition:: text
  

レンダリング後:

.. admonition:: text


rubric
------------------------------------
ディレクティブ表記::

  .. rubric:: text
  

レンダリング後:

.. rubric:: text


doc
------------------------------------
ディレクティブ表記::

  :doc:`/text` 

レンダリング後:

:doc:`/text` 

ref
------------------------------------
ディレクティブ表記::

  :ref:`Label` 

レンダリング後:

:ref:`Label` 

label
------------------------------------
ディレクティブ表記::

  .. _Title:
  
  

レンダリング後:

.. _Title:

download
------------------------------------
ディレクティブ表記::

  :download:`Title <path>` 

レンダリング後:

:download:`Title <path>` 

numref
------------------------------------
ディレクティブ表記::

  :numref:`Title <figure>` 

レンダリング後:

:numref:`Title <figure>` 

math
------------------------------------
ディレクティブ表記::

  :math:`a^5` 

レンダリング後:

:math:`a^5` 

command
------------------------------------
ディレクティブ表記::

  :command:`Title` 

レンダリング後:

:command:`Title` 

file
------------------------------------
ディレクティブ表記::

  :file:`path` 

レンダリング後:

:file:`path` 

guilabel
------------------------------------
ディレクティブ表記::

  :guilabel:`Title` 

レンダリング後:

:guilabel:`Title` 

key
------------------------------------
ディレクティブ表記::

  :kbd:`shortcut` 

レンダリング後:

:kbd:`shortcut` 

menu
------------------------------------
ディレクティブ表記::

  :menuselection:`Title --> Title2` 

レンダリング後:

:menuselection:`Title --> Title2` 

literalinclude
------------------------------------
ディレクティブ表記::

  .. literalinclude:: path
  

レンダリング後:

.. literalinclude:: path


.. |date| date::