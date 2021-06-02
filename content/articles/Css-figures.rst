CSSで図形をつくる
###############################

:title: CSSで図形をつくる
:date: 2021-06-02
:category: HTML
:tags: HTML, CSS

| 

HTMLとCSSを使って、図形を表示させる方法です。

Divを使って作ります

| 

丸と四角
----------

コードと結果は以下です。

HTML

::

  <div class="square"></div>
  <div class="circle"></div>


CSS

::

  .square {
    width: 50px;
    height: 50px;
    background: black;
  }

  .circle {
    width: 50px;
    height: 50px;
    background: black;
    border-radius: 50px;
  }

| 

.. raw:: html

  <p class="codepen" data-height="265" data-theme-id="light" data-default-tab="css,result" data-user="yy87750722" data-slug-hash="KKWyajK" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="KKWyajK">
  <span>See the Pen <a href="https://codepen.io/yy87750722/pen/KKWyajK">
  KKWyajK</a> by やまっく (<a href="https://codepen.io/yy87750722">@yy87750722</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
  </p>
  <script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>



| 
| 
| 

疑似要素（before/after）を使った組み合わせ図形
------------------------------------------------

疑似要素：HTMLの要素に対して、CSSで要素を追記できる方法。

これを使えば、作った図形に2つまで図形の追加ができます。（合計3つの図形を一つのDiv内に作れる）

サンプルは下記です。

HTML

::

  <div class="Switch"></div>

CSS

::

  .Switch {
    width: 30px;
    height: 63px;
    background: #ccc;
    position: relative;
  }
  .Switch:before {
    content: '';
    position: absolute;
    width: 18px;
    height: 48px;
    left: 6px;
    top: 6px;
    background: #fff;
  }
  .Switch:after {
    content: '';
    position: absolute;
    width: 18px;
    height: 18px;
    left: 6px;
    top: 6px;
    background: #596;
  }


| 

.. raw:: html

  <p class="codepen" data-height="265" data-theme-id="light" data-default-tab="css,result" data-user="yy87750722" data-slug-hash="oNZEvBQ" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="oNZEvBQ">
  <span>See the Pen <a href="https://codepen.io/yy87750722/pen/oNZEvBQ">
  oNZEvBQ</a> by やまっく (<a href="https://codepen.io/yy87750722">@yy87750722</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
  </p>
  <script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

| 
| 

参考URL
------------

`CSSで作図する <https://qiita.com/yaegaki/items/a1e518d16be9b85479b4>`_

`CSSの疑似要素とは <https://saruwakakun.com/html-css/basic/before-after>`_

