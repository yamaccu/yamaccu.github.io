Pelicanのプラグイン
###############################

:title: Pelicanのプラグイン
:date: 2021-05-24
:category: pelican
:tags: pelican

| 

Pelicanのプラグインの解説です。

以下のプラグインが便利かと思います。

* related_posts
* share_post
* neighbors
* sitemap
* tipue_search

| 

プラグイン導入方法
===============================

1. pluginsフォルダを作成します。

2. | githubからコピーしてきます。
   | `レポジトリ <https://github.com/pelican-plugins>`_

3. 設定ファイル（pelicanconf.py）で使用するpluginを設定します。

::

  PLUGIN_PATHS = ['plugins']
  PLUGINS = ['related_posts',
             'share_post',
             'neighbors',
             'sitemap',
             'tipue_search',]

| 

related_posts
===============================

記事の最後に、関連記事をリストアップして表示してくれます。

同じタグのついた記事を表示する仕様のようです。

| 

share_posts
===============================

記事の最後に、SNSのshareボタンを追加してくれます。

※Flexテーマを使用している場合は、テーマ内のファイル修正が必要です。

`こちらのHP <https://www.ainoniwa.net/pelican/2020/0830a.html>`_ が非常にわかりやすいです。

| 

neighbors
===============================

記事の最後に、次の記事 / 前の記事 へ移動するボタンを追加してくれます。

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

