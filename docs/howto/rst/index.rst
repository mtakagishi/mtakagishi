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
VSCode拡張によるスニペット
-------------------------------


.. |date| date::