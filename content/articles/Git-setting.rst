Github 初pushまでの設定
###############################

:title: Github 初pushまでの設定
:date: 2021-06-03
:category: github
:tags: github

| 

githubのレポジトリにプッシュするまでの設定です。

#. gitをインストール
#. githubにsign up
#. 端末のSSH公開鍵の設定
#. ローカル環境の設定
#. レポジトリをクローン
#. 変更＆プッシュ

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

SSH公開鍵の生成

::

  ssh-keygen -t rsa

githubのSetting => SSH and GPG keys で生成したSSH鍵を登録

`参考HP <https://qiita.com/shizuma/items/2b2f873a0034839e47ce>`_

| 

ローカル環境設定
===============================

::

  git config --global user.name "ユーザー名"
  git config --global user.email "メールアドレス"

ユーザー名、メールアドレスはgithubの登録情報と同じもの。

| 

githubのレポジトリをクローン
===============================

githubのページでレポジトリ作成

作成したレポジトリをローカル環境にクローン

::

  git clone <URLアドレス>

※Clone時に設定されるもの

* origin設定


| 

変更＆プッシュ
===============================

ファイルの追加、修正をしたら

::

  git add <ファイル名>
  git commit -m "コメント"
  git push (-f) origin master

※-fは強制プッシュなので取り扱い注意

| 



