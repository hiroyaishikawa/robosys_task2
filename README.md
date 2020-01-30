# ロボットシステム学　課題2 
## 概要
ROSで利用するための簡単なパブリッシャとサブスクライバを作成しました。

パブリッシャにて入力された数値をサブスクライバで表示、その総和を計算し、出力します。

## 動作デモ(Youtube)
https://www.youtube.com/watch?v=ZH2RezGNH0Y&feature=youtu.be

## 動作環境
Ubuntu 18.04.3 LTS

ROS Melodic

Python3.6.9

## 使い方
1．roscoreを起動

2．2つ目の端末を起動し、catkinワークスペースへ移動し$ rosrun robosys input.py を実行

3．3つ目の端末を起動し、catkinワークスペースへ移動し$ rosrun robosys twice.py を実行

4．2つ目の端末で数値を入力し、Enterで確定

5．3つ目の端末に入力した数字と総和が表示される

6．再び2つ目の端末へ数字を入力すると3つ目の端末へ送信され、入力数値と総和が表示

 　以下繰り返し

## ライセンス
このソフトウェアはMITライセンスで提供されます。詳細はLICENSEをご覧ください。

## 製作者
石川 弘也

## 参考文献
ROS.org シンプルなPublisherとSubscriberを実行してみる http://wiki.ros.org/ja/ROS/Tutorials

からあげ READMEの良さそうな書き方・テンプレート【GitHub/Bitbucket】https://karaage.hatenadiary.jp/entry/2018/01/19/073000 
