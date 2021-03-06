********************************
プロジェクト操作
********************************
Last Updated on |date|

https://goharbor.io/docs/2.1.0/working-with-projects/

新規プロジェクト
==============================
* コンテナイメージは、プロジェクトにプッシュする
* プロジェクトには、PublicとPrivateの2種類がある。
* 事前準備として、Harbor管理者か、プロジェクト管理者でログインしておく。

手順
----------
#. Project -> New Project
#. nameを決定
#. Public/Privateを選択
#. OKをクリック

設定
-----------
Configrationをクリック

* PublicチェックボックスONにするとproject内のリポジトリを全公開
* 署名のないコンテナイメージを拒絶する場合は、Enable content trustをチェック

検索
---------
* searchフィールドprojectやリポジトリの検索可能。
* public/privateいずれもアクセス権があるものが検索される。

プロジェクト設定
==============================
project設定にはprojectの管理者権限が必要

脆弱性に関する設定
-------------------------
Prevent vulnerable images from runing チェックボックス
* 「Prevent vulnerable images from runing」：脆弱なコンテナイメージを実行できないようにする設定可能
* セキュリティレベルを設定し、脆弱なコンテナイメージのPULLを抑制できる。無視して実行させる設定も可能
* 「Automatically scan images on push」：プッシュ時に自動で脆弱性スキャンする設定が可能

Robotアカウントの追加方法
------------------------------------
* Robotアカウントではログインできない
* DockerとHelmのコマンドを通した操作のみ可能
* 追加するとアカウントリストにrobot$ で表示される。

#. 管理権限のあるユーザでログイン
#. 追加したいProjectで「Robot Accounts」を選択
#. [New Robot Account]を選択
#. nameを確定する。必要に応じてdescriptionも記入
#. 有効期間を設定。無期限の場合は「Never Expired」。何も設定しないとデフォルト値（30日）がセット。デフォルト値はSystem Settingから変更可能
#. Helm chart へのpush/pullに必要な権限を付与
#. Saveをクリック
#. 確認画面にて「Export to File」からアクセストークンをファイル入手するか、クリップボードに貼り付け
#. トークンをパスワードとしてログイン認証可能

Webhookによる通知設定
-------------------------------
* HTTP と Slack の2種のイベントに対応

脆弱性の許可リスト設定
-------------------------------
* 許可リストをコントロールし、実行許可させない設定が可能

信頼済みコンテナの設定
------------------------------
* Notary が必要


イメージ・タグ・Helmチャートの操作
============================================
* preheat(予熱？）ができるとの記述。
* Dockerコマンドからのpull/push
* k8sからのpull
* ラベル付け、タグ付け操作
* Helm chartとのマッピング

API Explorer
==============================


.. |date| date::

