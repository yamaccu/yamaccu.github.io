Github 初pushまでの設定
###############################

:title: Github 初pushまでの設定
:date: 2021-06-02
:category: github
:tags: github

| 

githubのレポジトリにプッシュするまでの設定です。

# gitをインストール
# githubにsign up
# 端末でSSH公開鍵の設定をしgithubに登録
# 設定ファイル作成
# 

| 

gitをインストール
===============================

`git公式 <https://gitforwindows.org/>`_

| 

githubにsign up
===============================

`github <https://github.co.jp/>`_

| 

端末のSSH公開鍵の設定
===============================

`参考HP <https://qiita.com/shizuma/items/2b2f873a0034839e47ce>`_

| 

設定
===============================

::

  git config --global user.name "ユーザー名"
  git config --global user.email "メールアドレス"

  git remote add origin <URLアドレス>
  

| 

sitemap
===============================

html出力フォルダに、sitemapu.xmlを自動生成してくれます。

| 

tipue_search
===============================

ブログ内の検索機能の追加です。

メニューに検索ボックスを設定してくれます。

以下の設定を設定ファイル（pelicanconf.py）に追加します。

::

  DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

| 

参考HP
===============================

`公式doc <https://docs.getpelican.com/en/latest/plugins.html>`_

