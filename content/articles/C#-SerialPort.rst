C#でシリアル通信
###############################

:title: C#でシリアル通信
:date: 2021-06-09
:category: C#
:tags: C#

| 

C#でシリアル通信する方法です。
サンプルとしてWPFで作成します。

| 

使用Class
----------

`SerialPortクラス <https://docs.microsoft.com/ja-jp/dotnet/api/system.io.ports.serialport?view=dotnet-plat-ext-5.0>`_ を使用します。

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

ポート選択
------------------------------------------------

使用可能なポートを取得します。

リスキャン処理を追加したいときは、このメソッドを再度実施します。

::

  private void scanCOMPorts()
  {
    ComboBox.Items.Clear();
    string[] ports = SerialPort.GetPortNames();
    foreach (var port in ports)
    {
      　ComboBox.Items.Add(p);
    }
  }

調査中：ObservableCollectionを使えばリスキャンいらない？

`参考1 <https://hyperts.net/csharp-serial-wpf/>`_

| 


シリアルポートオープン
----------------------------------

シリアルポート接続を開きます。

下記はボタンのクリックイベントに実装しています。

::

  private void serialOpenBtn_Click(object sender, EventArgs e)
  {
    serialPort.PortName = ComboBox.SelectedValue.ToString();
    serialPort.BaudRate = 9600;
    serialPort.DataBits = 8;
    serialPort.Parity = Parity.None;
    serialPort.StopBits = StopBits.One;
    serialPort.WriteTimeout = 1000;
    serialPort.ReadTimeout = 1000;
    try
    {
        serialPort.Open();
    }
    catch (Exception ex)
    {
        MessageBox.Show(ex.Message);
    }
  }

| 

シリアルポートクローズ
----------------------------------

シリアルポート接続を閉じます。

下記は、ボタンのクリックイベントに実装しています。

::

  private void serialCloseBtn_Click(object sender, EventArgs e)
  {
   try
    {
        serialPort.Close();
    }
    catch (Exception ex)
    {
        MessageBox.Show(ex.Message);
    }
  }

| 

データ送信
----------------------------------

byte配列を送信します。

::

  private byte[] sendData()
  {
    byte[] sendBytes = { 0,1,2,254,255 };
    if (serialPort.IsOpen)
    {
      serialPort.Write(sendBytes, 0, sendBytes.Length);
    }

    return sendBytes;
  }

| 

文字列を送信します。

::

  private string sendData()
  {
    string sendStr = "01234";
    if (serialPort.IsOpen)
    {
      serialPort.Write(sendStr);
    }

    return sendStr;
  }

| 

データ受信
----------------------------------

byte配列を受信します。

::

  private byte[] recieveData()
  {
    return 
  }

※Array.Resizeを使えばbyte配列の領域を事前に固定しなくて大丈夫かも。

`参考2 <http://diy.ease-labs.com/?page_id=10049>`_

| 

文字列を受信します。

::

  private byte[] recieveData()
  {
    return serialPort.ReadExisting()
  }

| 


割込みを使った受信。

データを受信したらすぐにデータを取り込んでくれます。

割込み設定はOpen()時に一緒に実施すると良いです。

::

  private void serialOpenBtn_Click(object sender, EventArgs e)
  {
    try
    {
      serialPort.Open();
      serialPort.DataReceived += OnReceived;
    }
    catch (Exception ex)
    {
      MessageBox.Show(ex.Message);
    }
  }

  private void OnReceived(object sender, SerialDataReceivedEventArgs e)
  {
    RecieveData += serialPort.ReadExisting();
  }

| 

バッファクリア
----------------------------------

バッファにたまっているデータをクリアします。

::

  private void BuffClear()
  {
    serialPort.DiscardInBuffer();
  }



参考URL
------------


