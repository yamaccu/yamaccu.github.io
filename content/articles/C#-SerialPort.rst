C#でシリアル通信
###############################

:title: C#でシリアル通信
:date: 2021-06-09
:modify: 2021-07-05
:category: C#
:tags: C#

| 

C#でシリアル通信する方法です。WPFで作成します。

`github <https://github.com/yamaccu/WPF-SerialCommunication/tree/main>`_ にサンプルをあげています。

作成したアプリはこんな感じです。

.. image:: {static}/images/C-SerialPort-1.png
  :height: 354px
  :width: 438px
  :align: left

| 

**使用Class**
--------------

`SerialPort class <https://docs.microsoft.com/ja-jp/dotnet/api/system.io.ports.serialport?view=dotnet-plat-ext-5.0>`_ を使用します。

NugetでSystem.IO.Portsをインストールする必要があります。

複数ポートを同時に使用しない場合は、staticで使うことが多いようです。

以下、機能の解説です。

|

+------------------------+--------------------------------+
| 機能                   | メソッド                       |
+========================+================================+
| ポート選択             | GetPortNames()                 |
+------------------------+--------------------------------+
| シリアルポートオープン | Open()                         |
+------------------------+--------------------------------+
| シリアルポートクローズ | Close()                        |
+------------------------+--------------------------------+
| データ送信             | Write(byte[], int32, int32) /  |
|                        | Write(string)                  |
+------------------------+--------------------------------+
| データ受信             | Read(byte[], int32, int32) /   |
|                        | ReadExisting()                 |
+------------------------+--------------------------------+
| バッファクリア         | DiscardInBuffer()              |
+------------------------+--------------------------------+

| 
| 

**使用ポートの選択**
------------------------------------------------

使用可能なポートを取得します。

※Binding用にReactivePropertyを使用しています。

.. code-block:: C#

  public ReactiveCollection<string> COMPorts { get; set; }
      = new ReactiveCollection<string>();

  public void ScanCOMPorts()
  {
    COMPorts.Clear();
    string[] ports = SerialPort.GetPortNames();
    foreach (var port in ports)
    {
      COMPorts.Add(port);
    }
  }

| 

ComboBoxにBindingします。

XAML:

.. code-block:: C#

  <ComboBox ItemsSource="{Binding COMPorts}" />

| 

ComboBoxのDropDownOpenedイベントにポート取得のメソッドを登録しておくと、
ドロップダウンを開く度に使用可能ポートをロードしてくれて便利です。

| 


**シリアルポートオープン**
----------------------------------

シリアルポート接続を開きます。

Open前に各種設定を行います。

.. code-block:: C#

  serialPort.PortName = port;     //選択したport名
  serialPort.BaudRate = baudrate;    //選択したbaudrate
  serialPort.DataBits = 8;
  serialPort.Parity = Parity.None;
  serialPort.StopBits = StopBits.One;
  serialPort.WriteTimeout = 1000;
  serialPort.ReadTimeout = 1000;
  serialPort.Encoding=Encoding.UTF8;

  serialPort.Open();

| 

**シリアルポートクローズ**
----------------------------------

シリアルポート接続を閉じます。

.. code-block:: C#

  serialPort.Close();


| 

**データ送信**
----------------------------------

byte配列を送信します。

.. code-block:: C#

  byte[] sendBytes = { 0,1,2,254,255 };
  if (serialPort.IsOpen)
  {
    serialPort.Write(sendBytes, 0, sendBytes.Length);
  }

| 

文字列を送信します。

.. code-block:: C#

  string sendStr = "01234";
  if (serialPort.IsOpen)
  {
    serialPort.Write(sendStr);
  }

| 

**データ受信**
----------------------------------

byte配列を受信します。

.. code-block:: C#

  byte[] resByte = new byte[serialPort.BytesToRead];
  serialPort.Read(resByte, 0, serialPort.BytesToRead);

| 

文字列を受信します。

.. code-block:: C#

  string resStr;
  resStr = serialPort.ReadExisting()

| 


割込みを使って受信します。

データを受信したらすぐにデータを取り込んでくれます。


.. code-block:: C#

  SerialCom.serialPort.DataReceived += OnReceived;

  private void OnReceived(object sender, SerialDataReceivedEventArgs e)
  {
    resStr += serialPort.ReadExisting();
  }

| 

**バッファクリア**
----------------------------------

バッファにたまっているデータをクリアします。

.. code-block:: C#

  serialPort.DiscardInBuffer();

| 



ご指摘等ありましたら、下記twitterにお願いします。


.. raw:: html

  <blockquote class="twitter-tweet"><p lang="ja" dir="ltr">勉強用に、WPFでシリアル通信アプリを作りました。<br>組み込み系のプロダクトだと、デバッグ用にシリアル通信まぁまぁ使いますね。<a href="https://twitter.com/hashtag/wpf?src=hash&amp;ref_src=twsrc%5Etfw">#wpf</a> <a href="https://twitter.com/hashtag/Csharp?src=hash&amp;ref_src=twsrc%5Etfw">#Csharp</a><a href="https://t.co/kyVjuQT67q">https://t.co/kyVjuQT67q</a></p>&mdash; やまっく (@YY87750722) <a href="https://twitter.com/YY87750722/status/1412054673071083520?ref_src=twsrc%5Etfw">July 5, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>