Pelicanで画像を表示する
###############################

:title: Pelicanで画像を表示する
:date: 2021-07-29
:category: pelican
:tags: pelican

| 

Pelicanで画像を表示する方法です。

公式ドキュメントの該当箇所は `こちら <https://docs.getpelican.com/en/latest/content.html?highlight=filename#linking-to-internal-content>`_ です。

| 

手順
===============================

1. cotentフォルダの配下のimagesフォルダに画像を保存します。

2. 以下のように、rstファイルに記述します。

::

  .. image:: {static}/images/test.png
    :height: 200px
    :width: 200px
    :align: left
    :alt: test.png

これで、以下のようにファイルが表示されます。

.. image:: {static}/images/test.png
  :height: 200px
  :width: 200px
  :align: left
  :alt: test.png



