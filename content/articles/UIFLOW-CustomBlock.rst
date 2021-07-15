UIFLOWでカスタムブロックを作る
###############################

:title: UIFLOWでカスタムブロックを作る
:date: 2021-07-15
:category: M5Stack
:tags: M5Stack

| 

M5Stack等で使用できるビジュアルプログラミング「UIFLOW」でカスタムブロックを作成する方法です。

M5Stackとは、ESP32マイコンを使用し、wifi/LCD/各種センサなどを一体化させたマイコンボードです。

githubに、WAVファイルを再生するためのカスタムブロックのサンプルをあげています。

リンク

* `M5Stack <https://m5stack.com/>`_
* `UIFLOW <https://flow.m5stack.com/>`_ 
* `カスタムブロック作成 <http://block-maker.m5stack.com/>`_
* `githubサンプル <https://github.com/yamaccu/UIFLOW-wavplayer>`_

| 
| 

手順
----------

1. Pythonでプログラムを書く
2. setup用のブロックを作る
3. 自作関数を実行するためのブロックを作る

| 


Pythonでプログラムを書く
----------------------------------

まずはブロック化したいプログラムを書きます。

| 

setup用のブロックを作る
----------------------------------

UIFLOWのsetup実行時に、importとかdefとか実施しますので、
そのためのブロックを作ります。

* NameはBlockmaker上だけの識別名なので何でも大丈夫です。
* TypeはExecuteにします。
* Parameterは、まずブロック名をLabelで設定します。
  変数があれば、String/Number/Variableで設定します。
* BlockCodeに作ったプログラムをコピペします。

※Variavle：他のブロックの値を代入する変数、Valueブロックを繋げられるようになります。

| ※BlockCode内の変数は、「${変数}」と書きます。
| ex) playwav(${playwav},${volume})


| 

自作関数を実行するためのブロックを作る
-------------------------------------------------

defで定義した自作関数を実行するブロックを作ります。

* NameはBlockmaker上だけの識別名なので何でも大丈夫です。
* TypeはExecuteにします。
* Parameterは、まずブロック名をLabelで設定します。
  変数があれば、String/Number/Variableで設定します。
* BlockCodeに定義した関数と変数を記述します。

| 

完成したら
----------------------------------

右下のDownloadボタンをおしてDownloadして、UIFLOWのCustomから読み込みます。

| 

参考URL
------------

`qiita 自作モジュール用のUI Flowのカスタムブロックを作る <https://qiita.com/ciniml/items/618899c9065d51d5c54e>`_
