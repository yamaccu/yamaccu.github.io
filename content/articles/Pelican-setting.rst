Pelicanの設定
###############################

:title: Pelicanの設定
:date: 2021-05-19
:category: pelican
:tags: pelican

| 

この記事では、Python製の静的サイトジェネレータ「pelican」の設定ファイルについて解説します。

設定ファイルは2つあります。

* pelicanconf.py
* publishconf.py

手元の環境で動作確認をする際は「pelicanconf.py」を使用します。

本番環境へデプロイする際も基本的に「pelicanconf.py」を使用しますが、
本番環境用に設定したい項目は「publishconf.py」に記述して、「pelicanfong.py」の設定に上書き設定するイメージです。

| 

**設定項目**
===============================

Basic Setting
-------------

::
  
  PATH = 'content'

pelicanコマンドの対象ディレクトリを指定します。

これを設定しておくと、コマンドプロンプトで"pelican"と打つだけで指定ディレクトリのファイルをHTML化してくれます

| 

::

  ARTICLE_PATHS = ['articles']

書いたブログの記事を格納するディレクトリ名です。

このディレクトリは上記のPATH直下に作成します。

| 

::

  SITEURL = 'http://127.0.0.1:8000'

サイトを公開するURLです。

| 

::

  SITENAME = 'xxxxxx'

サイト名です。

| 

::

  SUMMARY_MAX_LENGTH = 5

| topページで、各記事のサマリーを表示する文字量の設定です。
| (数字を変えるとサマリー表示量が変わります。数字と表示量の関係は不明、カット&トライで試してみてください。)

| 

::

  PYGMENTS_RST_OPTIONS = {
    'linenos': 'table',
  }

`コードブロック <https://planset-study-sphinx.readthedocs.io/ja/latest/04.html#id10>`_ でデフォルトで使う強調構文を指定します。

'linenos': 'table'は行番号を表示するオプションです。

| 

::

  PLUGIN_PATHS = ['plugins']

プラグインを保存するディレクトリ名です。

| 

::

  PLUGINS = ['related_posts',
             'share_post',
             'neighbors']

使用するプラグインの指定です。

| 

::
  
  RELATED_POSTS_MAX = 5

プラグイン「related_posts」の設定で、関連記事の表示数です。

| 

URL Settings
-------------

::

  ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
  ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
  YEAR_ARCHIVE_URL = 'posts/{date:%Y}/'
  YEAR_ARCHIVE_SAVE_AS =  'posts/{date:%Y}/index.html'
  MONTH_ARCHIVE_URL = 'posts/{date:%Y}/{date:%m}/'
  MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

URLの指定です。

上記のように、URLにメタデータを含めることができます。

page、Categoryなどの固定ページも設定すればデフォルトURLから変更ができます。

| 

::

  SLUGIFY_SOURCE = 'basename'

メタファイル{slug}の値の引用先を設定します。

title：ファイルのタイトル、basename：ファイル内のslugタグ

ファイルタイトルから引用した場合、漢字をタイトルとしていると中国語読みがslugに設定されます。

| 

Time and Date
--------------

::

  TIMEZONE = 'Asia/Tokyo'

タイムゾーンの設定です。

| 

::

  DEFAULT_DATE='fs'

デフォルト時間の設定です。

記事のファイル内でメタデータ{Date}を指定しなかった場合、ここの設定が反映されます。

'fs'とするとファイルシステムのタイムスタンプを使用します。

| 

::

  DEFAULT_DATE_FORMAT = '%Y/%m/%d'

投稿した記事の日付フォーマットの設定です。

| 

META DATA
----------

::

  AUTHOR = 'xxxx'

記事の著者の設定です。

| 

Feed Settings
--------------

::

  FEED_ALL_ATOM = None
  CATEGORY_FEED_ATOM = None
  TRANSLATION_FEED_ATOM = None
  AUTHOR_FEED_ATOM = None
  AUTHOR_FEED_RSS = None

Feedを使うときの設定です。

使わなければすべてNoneとします。
  
| 

Translations
-------------

::

  DEFAULT_LANG = 'Japanese'
  
ページの言語設定です。

| 

Theme
------

::

  THEME = 'themes/Flex'

pelicanのテーマを導入する場合、ここでディレクトリを指定します。

テーマの設定は下記を参考に。

https://www.sairablog.com/article/python-pelican-blog-theme-howto.html

| 

::

  SITESUBTITLE = "xxxxxxx"

サイトのサブタイトルです。

| 

::

  MENUITEMS = (
      ("Archives", "/archives.html"),
      ("Categories", "/categories.html"),
  )

使用するMenuの項目です。

サイト上部にリンクとして表示されます。

CategoryやTagをメタデータとして設定しておくと、Menuで一覧をみることができます。

| 

::

  SOCIAL = (('twitter', 'https://twitter.com/xxxxxxxx'),
          ("github", "https://github.com/xxxxxx"))

SNSのリンク設定です。

アイコンとリンクを自動生成してくれます。

| 

Pagination
-----------

::

  DEFAULT_PAGINATION = 10

一度に表示する記事数の設定です。

| 

Flexテーマの設定
-----------------

::

  MAIN_MENU = True

上部のMenuの表示・非表示設定です。

| 

::

  SITELOGO = SITEURL+"/images/profile.png"

サイトに表示するロゴの指定です。

| 

::

  FAVICON = "/images/favicon.ico"

ブラウザのタブ部に表示するロゴの指定です。

| 

::

  PYGMENTS_STYLE = "monokai"

コードブロックのスタイルの指定です。

参考　https://help.farbox.com/pygments.html

| 

::

  DISABLE_URL_HASH = True

記事内のアンカーの有効・無効設定です。Trueは無効。

| 

::

  CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
  }
  COPYRIGHT_YEAR = datetime.now().year

ページ下部のライセンス表示の設定です。

|  

::

  USE_LESS = True

CSSファイルの代わりにLESSファイルを使用するかどうかの設定です。

| 

**publish.confの記述**
======================

publishconf.pyの中に "from pelicanconf import \*" と記述することで、pelicanconf.pyの設定をpublishでも使用できます。
以下は、追加で設定した方が良いであろうものです。

| 

::
  
  SITEURL = 'https://xxxxxx'
  
  MENUITEMS = (
      ("Archives", "xxxxxx"),
      ("Categories", "xxxxxx"),
  )
  
  SITELOGO = "/blog/images/profile.png"
  
  FAVICON = "/images/favicon.ico"

URL設定系は手元の環境と本番環境で異なると思うので、publish.conf内で設定する必要があるかと思います。

| 

::

  GOOGLE_ANALYTICS = "xxxxxxxx"

Google Analyticsのトラッキングコードの設定ができます。

| 

::

  GOOGLE_ADSENSE = {
  'ca_id': 'ca-pub-xxxxxxxx',    # Your AdSense ID
  'page_level_ads': True,          # Allow Page Level Ads (mobile)
  'ads': {
    'aside': 'xxx',          # Side bar banner (all pages)
    'main_menu': 'xxx',      # Banner before main menu (all pages)
    'index_top': 'xxx',      # Banner after main menu (index only)
    'index_bottom': 'xxx',   # Banner before footer (index only)
    'article_top': 'xxx',    # Banner after article title (article only)
    'article_bottom': 'xxx', # Banner after article content (article only)
  }

google adsensの設定ができます。

| 

**参考URL**
===============

`pelican公式 <https://docs.getpelican.com/en/stable/settings.html>`_

`FLEX公式 <https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings>`_
