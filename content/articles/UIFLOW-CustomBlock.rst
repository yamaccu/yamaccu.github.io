**UIFLOWでカスタムブロックを作る**
###################################

:title: UIFLOWでカスタムブロックを作る
:date: 2021-07-15
:category: M5Stack
:tags: M5Stack

| 

`M5Stack <https://m5stack.com/>`_ のビジュアルプログラミング「`UIFLOW <https://flow.m5stack.com/>`_」でカスタムブロックを作成する方法です。

`こちらのカスタムブロック作成ページ <http://block-maker.m5stack.com/>`_ から作成します。

`github <https://github.com/yamaccu/UIFLOW-wavplayer>`_ に、WAVファイルを再生するためのカスタムブロックをあげています。

| 

※M5Stack：ESP32マイコンを使用し、wifi/LCD/各種センサなどを一体化させたマイコンボード


| 

**手順**
----------

1. Pythonでプログラムを書く
2. setupブロックを作る
3. 自作関数を実行するブロックを作る

| 

**Pythonでプログラムを書く**
----------------------------------

まずはブロック化したいpythonのプログラムを書きます。

| 

**setupブロックを作る**
----------------------------------

初期設定用(setup)のブロックを作成します。

importやdefなどはこのブロックで実行します。

.. image:: {static}/images/UIFLOW-CustomBlock-1.PNG
  :height: 500px
  :width: 669px
  :align: left
  :alt: UIFLOW-CustomBlock-1.PNG

* Name：Blockmaker上だけの識別名なので何でも大丈夫です。
* Type：Executeにします。
* Parameter：まずブロック名をtype:Labelで設定します。
  変数があれば、type:String/Number/Variableで設定します。
* BlockCode：作ったプログラムをコピペします。

| 

**自作関数を実行するブロックを作る**
-------------------------------------------------

setupブロックで定義した自作関数を実行するブロックを作ります。

.. image:: {static}/images/UIFLOW-CustomBlock-2.PNG
  :height: 500px
  :width: 669px
  :align: left
  :alt: UIFLOW-CustomBlock-2.PNG

* 基本はsetupブロックと同じです。
* defで定義した関数をBlockCodeへ入力します。
* 変数があればparameterで設定します。

| ※parameterで設定した変数をBlockCode内で読み出すには、「${変数}」と書きます。
| ex) playwav(${playwav},${volume})
| 

| 

**完成したら**
----------------------------------

右下のDownloadボタンをおしてDownloadして、UIFLOWのCustomから読み込みます。

| 


**参考URL**
----------------

`qiita 自作モジュール用のUI Flowのカスタムブロックを作る <https://qiita.com/ciniml/items/618899c9065d51d5c54e>`_



| 

