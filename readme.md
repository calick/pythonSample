# pythonとは
* オープンソースのプログラミング言語  
Guido van Rossumというオランダのプログラマーが開発。  
プログラマーはコードを書くよりも読むことに時間を使っているということに気づいたGuidoが読みやすいプログラミング言語を開発。


# virtualenv環境の使い方
<pre>
ex. python3で環境を作成
$ virtualenv -p python3 test_env
（virtualenv -p [Pythonのコマンド] [作成する環境名]）

作成したtest_envへ移動
$ cd test_env

環境を起動
$ source bin/activate

仮想環境を終了する
$ deactivate
</pre>