# Let's go to Tokyo Disney Resort

予約が非常に困難な東京ディズニーリゾートの予約を自動化します。<br>
信じていれば夢は叶う、とシンデレラは言いました。<br>
このアプリを起動し、信じて（放置して）いればチケットが取れます。<br>
さあ、夢の国へ！<br>


## Abstract
パークチケットの購入手順は、<br>
日付指定→チケット指定→個人情報入力orログイン<br>
という手順で進みます。<br>

現在東京ディズニーリゾートは完全予約制となっており、1ヶ月先の1週間分のチケットを、各水曜日の16時から予約できるような仕組みとなっております。<br>
水曜日の16時以降、日付指定画面からチケット指定画面に進もうとすると、高確率でアクセス集中画面へリダイレクトされてしまい、なかなか予約へ進むことができません。<br>
そこで、チケット指定画面にアクセスできるまで、Google Chromeを自動制御するソフトウェアを作成しました。


## Preparation
Google Chromeをインストールしていない場合、[ここ](https://www.google.com/intl/ja/chrome/)からインストールして下さい。<br>
また、以下のパッケージを使用します。インストールしていない場合は以下のコマンドでインストールして下さい。
```
$ pip install selenium
$ pip install chromedriver-binary=[Version of Your Chrome]
```
Chrome Driverのバージョンは、自身が使っているものに合わせてください。<br>
Google Chromeのバージョン確認方法は[こちら](https://pc-karuma.net/google-chrome-version-update/)<br>
（実行確認済Ver.: 87.0.4280.67 Official Build  x86_64）<br>

続いて、このリポジトリを好きなディレクトリでクローンします。
```
$ git clone https://github.com/Tiger-0512/get-dream.git
```


## Get Dream!
ディレクトリに入って実行します。
```
$ cd get-dream
$ python run.py
```
実行すると、コマンドライン上に指示が出ます。<br>
従っていけばあら簡単！チケットが取れます。


## Reference Image
日付指定画面
![日付指定画面](./images/image1.png)
<br>
アクセス集中画面
![アクセス集中画面](./images/image2.png)
<br>
チケット指定画面
![チケット指定画面](./images/image3.png)
