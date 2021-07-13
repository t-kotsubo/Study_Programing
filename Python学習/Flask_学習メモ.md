## Webアプリケーションの基礎技術

* ルーティング：Webブラウザからのリクエストに合わせて、呼び出す処理を切り替える
*  テンプレートエンジン：アプリケーションが保持するデータなどをHTMLのひな型と組み合わせてWebページを生成する



## Flaskの特徴

* 軽量Webアプリケーションフレームワーク。標準で提供する機能を最小限に絞る
* Python用Webアクセスライブラリに、Werkzeug WSGIツールキットを採用
* テンプレートエンジンとしてJinja2を採用
* Flask extensionsによる機能拡張



Flaskではルートごとに処理を記述する

例）ホスト名/testの場合

```
@app.route(/test)
def hello():
	return render_template("index.html")
```



## フォームの記述方法

### ①

![image-20200522140759893](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200522140759893.png)

### ②

![image-20200522140921541](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200522140921541.png)

### ③

![image-20200522141055935](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200522141055935.png)



![image-20200525164011891](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200525164011891.png)



## 参考になるWebページ

Flask
http://flask.pocoo.org/

Flask - Wikipedia
https://ja.wikipedia.org/wiki/Flask

Flaskへ ようこそ — Flask documentation
https://a2c.bitbucket.io/flask/

Flaskの簡単な使い方 - Qiita
https://qiita.com/zaburo/items/5091041a5afb2a7dffc8

ウェブアプリケーションフレームワーク Flask を使ってみる - Qiita
https://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4

[Python] Flask 入門 - ゾンビでもわかるPythonプログラミング
http://python.zombie-hunting-club.com/entry/2017/11/03/223503


【Jinja2テンプレートエンジン】

Welcome to Jinja2 — Jinja2 Documentation (2.10)
http://jinja.pocoo.org/docs/2.10/

Jinja2｜Pythonテンプレートエンジン - Qiita
https://qiita.com/yasumodev/items/ae11047e2c8694867892

Jinja2の基本的な使い方 - Qiita
https://qiita.com/RyoMa_0923/items/528303906a55f9b568e0

Jinja2の使い方がわかるとFlaskを用いた開発がよりスマートになる - Qiita
https://qiita.com/ryo2851/items/7ae5de21307d101b4759



## SQL Alchemy



![image-20200526110806223](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200526110806223.png)



###  SQL Alchemyの参考サイト

SQLAlchemy入門 SQLAlchemyとは - Python学習講座
http://www.python.ambitious-engineer.com/archives/1469

Flask-SQLAlchemyの使い方 - Qiita
https://qiita.com/msrks/items/673c083ca91f000d3ed1

Flask-SQLAlchemy — Flask-SQLAlchemy Documentation (2.3)
http://flask-sqlalchemy.pocoo.org/2.3/	

SQLAlchemyでSQLの基本的なクエリーまとめ(PythonのORM) - Qiita
https://qiita.com/bokotomo/items/a762b1bc0f192a55eae8