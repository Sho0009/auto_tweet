# Auto_tweet

このプログラムは、自動撮影した画像を動画化してTwitterに自動ツイートできます。


# Requirement

　　動作させるためには下記のライブラリのインストールが必要です。
 ```
 *Opencv                 4.6.0.66
 *schedule　　              1.1.0
 *oauthlib               3.2.2
 *requests_oauthlib      1.3.1
 *requests               2.28.1
 *datetime
 *time
 *os
 *glob
 *shutil
 *json
 ```


# Installation

動作させるためには下記のライブラリのインストールが必要です。

```
pip install oauthlib
pip install opencv-python
pip install schedule
pip install requests
```


# Usage

使用したいカメラを接続し、自動動作させたい時間をmix.pyで設定します。
そして、mix.pyを実行することで動作します。


# Note

注意点
*photo.pyのデバイス設定
*TwitterのAPIキーの入力
*画像保存先ファイルの確認

