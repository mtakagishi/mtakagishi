#################################################
Angular入門
#################################################
Last Updated on |date|

.. |date| date::

Angularについて
==================================================
* `公式ドキュメント <https://angular.jp/docs>`_ 
* SPAフレームワーク
* Google＋コミュニティにてメンテ
* 年2回のアップデート

必要知識
==================================================
* JavaScript
* HTML
* CSS
* Nodejs
* npm package manager

.. hint:: TypeScriptの知識は役に立つが必須でない

Angular CLIのインストール
==================================================

以下のコマンドを実行::

  npm install -g @angular/cli

.. todo:: 

  3つのWARNが発生。要調査

  * npm WARN deprecated har-validator@5.1.5: this library is no longer supported
  * npm WARN deprecated debug@4.2.0: Debug versions >=3.2.0 <3.2.7 || >=4 <4.3.1 have a low-severity ReDos regression when used in a Node.js environment. It is recommended you upgrade to 3.2.7 or 4.3.1. (https://github.com/visionmedia/debug/issues/797)
  * npm WARN deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142

Angular初期化
==================================================

以下でmy-appを作ってみる::

  ng new my-app

Angular実行
==================================================

実行すると4200ポートで初期画面を表示::

  cd my-app
  ng serve --open

.. figure:: /ex/angular/welcome.png

NextStepsのコマンド群
=================================================
上記画像の、NextStepsにある各ボタンには、それぞれのコマンドが表示される。

新規コンポーネントの作成::

  ng generate component xyz

AngularMaterialのインストール::

  ng add @angular/material

AngularPWAのインストール::

  ng add @angular/pwa

.. note::

  PWAは「Progressive Web Apps」のこと。スマートフォンで動作可能なネイティブアプリと遜色ないWebサイト。 `Googleチェックリスト <https://web.dev/pwa-checklist/>`_ がある。

依存モジュールのインストール::

  ng add ______

テストの実行・常駐::

  ng test

本番向けビルド::

  ng build --prod

公式ドキュメントのセットアップとしては以上。引き続き概念の解説やチュートリアルが用意されている。

.. toctree::
  :maxdepth: 2
  
  tutorial
