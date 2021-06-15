micropythonにreplでアクセス
###############################

:title: micropythonにreplでアクセス
:date: 2021-06-16
:category: micropython
:tags: micropython,repl

| 

micropythonにreplでアクセスする方法です。

| repl：「Read（読み取り）、Eval（評価）、Print（印字）、Loop（ループ）」の頭字語。
| 一つずつコマンドを実行できる仕組みで、コマンドプロンプトのようなイメージ。

| 

アクセス方法
-----------------

デバイスのシリアルポートに、シリアル通信アプリ（teratermなど）でアクセスします。

通信速度は115200bps。

CTR+Cを二回で、mainで実行している処理を中止してreplで操作可能になります。

| 

コマンド
-----------------------

::

    help()

ヘルプを表示します。

| 

::

    help('modules')

使用可能なライブラリを表示します。

| 

::

    help(obj)

調べたいobjectの説明を表示します

| 

::

    入力途中にTABキー

入力候補の表示をしてくれます。便利。

例えば、machine. でTabを押すとmachineの配下のクラスが表示されます。

| 

::

    dir()

インポート済みのファイルの情報を表示します。

| 

::

    sys.path.append('ディレクトリパス')

import時に探索されるパスを追加します。

| 

::

    os.listdir()

カレントディレクトリのファイルを表示します。

| 


参考URL
------------

`micropython公式 <https://micropython-docs-ja.readthedocs.io/ja/latest/esp8266/tutorial/repl.html>`_

