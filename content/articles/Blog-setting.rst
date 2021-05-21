ブログを作ったらやること
###############################

:title: ブログを作ったらやること
:date: 2021-05-20
:category: blog
:tag: blog

| 

ブログを作ったら、最初にやることのメモです。

* Google Analyticsの登録
* sitemapの作成
* robots.txtの作成
* Google Search Consoleの登録 / sitemapの登録

| 

Google Analyticsの登録
-----------------------

アクセス解析ツールのGoogle Analyticsに登録します。アクセス状況の確認に必須です。

登録したらトラッキングIDをHTMLに追記します。

pelicanでは、publishconf.pyにトラッキングIDを追加すると自動でやってくれます。

    GOOGLE_ANALYTICS = "xxxxxxxxxxxx"

`Google Analytics登録方法 <https://blog.siteanatomy.com/register-google-analytics/>`_

| 

sitemapの作成
--------------

Google検索にヒットさせ易くするためのファイルで、作成したらGoogle Search Consoleに登録します。

小規模HPには不要のようですが、一応作成します。

サイトマップは、pelicanのプラグイン「sitemap」で自動生成できます。

pelicanconf.pyに以下の設定を追加すると、出力フォルダに「sitemap.xml」が生成されます。

    PLUGINS = ['sitemap',]
    
    SITEMAP = {'format': 'xml'}

| 

※pelican以外の場合

一般的な静的サイトジェネレータにはsitemap生成のプラグインがあるようですので、他のジェネレータ使用時はそちらを使用します。

また、sitemap生成の無料ページもあるようです。

| 

robots.txtの作成
-----------------

sitemapへのリンクファイルです。

rootディレクトリに、「robots.txt」という名前のファイルを作成して、中身を以下のように記述します。

    | User-agent: *
    | Disallow:
    | 
    | Sitemap: https://xxxxxxxxx/sitemap.xml

| 

Google Search Consoleの登録 / sitemapの登録
---------------------------------------------

Google Search Consoleに登録します。HPへの流入ルート、検索順位などSEO関連情報がわかります。

登録完了したら、サイトマップも登録しておきます。

登録したては「サイトマップを読み込めませんでした」とエラーが出ますが、しばらく放置しておくと読み込んでくれるようです。

`Google Serach Console登録方法 <http://faster-than-the-sol.blogspot.com/2020/10/github-listing.html>`_

| 

参考URL
------------

`Google Analyticsについて <https://wacul-ai.com/blog/access-analysis/google-analytics-method/what-is-google-analytics/>`_

`sitemapについて <https://ferret-plus.com/curriculums/3563>`_

`robots.txtについて <https://ferret-plus.com/6879>`_

`Google Search Consoleについて <https://www.akibare-hp.jp/kouza/hp_kihon-serchconsole/>`_
