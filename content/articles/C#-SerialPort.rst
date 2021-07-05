C#でシリアル通信
###############################

:title: C#でシリアル通信
:date: 2021-06-09
:modify: 2021-07-05
:category: C#
:tags: C#

| 

C#でシリアル通信する方法です。WPFで作成します。

githubにサンプルをあげています。
`こちら <https://github.com/yamaccu/WPF-SerialCommunication/tree/main>`_

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

使用可能なポートを取得して、ComboBoxにBindingします。

ReactivePropertyを使っています。

Xaml側::

  <ComboBox ItemsSource="{Binding COMPorts}" DropDownOpened="ComboBox_DropDownOpened_COMPort" />

cs側::

  public ReactiveCollection<string> COMPorts { get; set; } = new ReactiveCollection<string>();

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

ComboBoxのDropDownOpenedイベントにポート取得のメソッドを登録しておくと、
ドロップダウンを開く度に使用可能ポートをロードしてくれて便利です。





| 


シリアルポートオープン
----------------------------------

シリアルポート接続を開きます。

Open前に各種設定を行います。

::

  public static void SerialOpen(string port,int baudrate)
  {
    serialPort.PortName = port;
    serialPort.BaudRate = baudrate;
    serialPort.DataBits = 8;
    serialPort.Parity = Parity.None;
    serialPort.StopBits = StopBits.One;
    serialPort.WriteTimeout = 1000;
    serialPort.ReadTimeout = 1000;
    serialPort.Encoding=Encoding.UTF8;

    serialPort.Open();
  }

| 

Openするメソッドを呼び出す側では、Open失敗時にエラーメッセージが出るようにします。

::

  public void SerialOpen()
  {
    try
    {
        SerialCom.SerialOpen(SelectedPort.Value, SelectedBaudrate.Value);
    }
    catch(Exception ex)
    {
        MessageBox.Show(ex.Message);
    }
  }


| 

シリアルポートクローズ
----------------------------------

シリアルポート接続を閉じます。

::

  serialPort.Close();


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
    byte[] resByte = new byte[serialPort.BytesToRead];
    serialPort.Read(resByte, 0, serialPort.BytesToRead);
    return resByte; 
  }

| 

文字列を受信します。

::

  private byte[] recieveData()
  {
    return serialPort.ReadExisting()
  }

| 


割込みを使って受信します。

データを受信したらすぐにデータを取り込んでくれます。

割込み設定はOpen()時に一緒に実施します。

::

  public void SerialOpen()
  {
    try
    {
        SerialCom.SerialOpen(SelectedPort.Value, SelectedBaudrate.Value);
        SerialCom.serialPort.DataReceived += OnReceived;
    }
    catch(Exception ex)
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

  serialPort.DiscardInBuffer();

| 

参考URL
------------

`参考１ <http://diy.ease-labs.com/?page_id=10049>`_



