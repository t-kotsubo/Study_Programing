# Git 学習メモ

## Gitの準備

* Git を使う準備として、`git init`  を実行する必要がある。

* ターミナルに出てくる「` $`」は入力する必要ない。

![1545959188347](C:\Users\Takayuki.Kotsubo\AppData\Roaming\Typora\typora-user-images\1545959188347.png)



## 共有するファイルを選択

* **ファイルを選択するには、「`git add ファイル名`」 を使う**

![1545961308249](C:\Users\Takayuki.Kotsubo\AppData\Roaming\Typora\typora-user-images\1545961308249.png)

※ addはあくまでも新たにgitの管理下に置くためにコマンドであって、実際にリモートにアップロードするにはコミット、プッシュを行う。



## 選択したファイルを記録する（コミット）する

* 選択したファイルを記録するには、「`git commit -m "メッセージ"`」を実行する。

* このように記録することを「コミット」と言い、このメッセージのことを「コミットメッセージ」と呼ぶ。	

![1545961267008](C:\Users\Takayuki.Kotsubo\AppData\Roaming\Typora\typora-user-images\1545961267008.png)



## 共有の仕組み

* Git では「リモート（remote）」という共有ファイルの置き場を使う。

* リモートにファイルをアップロードしたり、リモートからファイルをダウンロードすることで、開発者同士がファイルを共有することができる

## リモートの登録

* リモートにアップロードするにはそのリモートの URL を登録する必要がある。
* リモートを登録する際には名前を付ける必要があり、一般的には「```origin```」とすることが多い。
* 具体的には下記の図のように、`git remote add リモート名 URL` とすることで登録できる。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/git/study/1/1485516628208.png)

参考サイト

https://techacademy.jp/magazine/10268



## リモートにファイルをアップロード（プッシュ）する

* `git push origin master` とすることで登録したリモートにアップロード（プッシュと言う）することが可能。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/git/study/1/1485480919551.png)



## リモートのファイルをダウンロード（プル）する

* `git pull origin master`とすることで、リモートからファイルをダウンロードすることができる。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/git/study/1/1485225564635.png)



## 変更したファイルを把握する

* `git status`を用いることで自分が変更したファイルのファイル名を表示することができる。

![1545966392634](C:\Users\Takayuki.Kotsubo\AppData\Roaming\Typora\typora-user-images\1545966392634.png)



## 変更内容を把握する

* 変更内容を把握するためには、`git diff` コマンドを使用する。
* 追加された内容は下記の図のように緑色で表示される。

![1545966713118](C:\Users\Takayuki.Kotsubo\AppData\Roaming\Typora\typora-user-images\1545966713118.png)

* [コードを変更した部分]()では、右の図のように変更前のコードが<u>赤色</u>、変更後のコードが<u>緑色</u>で表示される。

  ![1545967082070](C:\Users\Takayuki.Kotsubo\AppData\Roaming\Typora\typora-user-images\1545967082070.png)



## addしたファイルを確認

* `git status`を使うことで、どのファイルを add していて、どのファイルがまだ add されていないかを確認することができる。
* `git status`を実行すると下の図のように`、<u>add されたファイルが緑色</u>、まだ <u>add されていないファイルが赤色</u>で表示されるのだ。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/git/study/1/1485313378425.png)



## コミット履歴を表示する

* `git log`	というコマンドを使うと、自分や他人のコミットを確認することができる。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/git/study/1/1485405607192.png)

* コミットメッセージだけでなく変更内容も見たければ、`git log -p`で確認できる。
* 表示内容が多い時は下の図のように特殊な表示モードになる。上下キーを使うと表示範囲を変えられて、<u>**Qキー**を押すことで終了できる</u>。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/git/study/1/1485411741288.gif)]



