# Git学習メモ

## GitHub ：Gitリポジトリのホスティングサービス

他にBitBucket等も有名



### 重要

* Gitは差分でなくスナップショットを記録する

* コミットは直前のコミットを保存しているのでコミットを辿ることで以前の状態に戻ることが可能

## Gitの基本



![image-20210620150949607](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210620150949607.png)

![image-20210620151048567](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210620151048567.png)

![image-20210620150846760](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210620150846760.png)

![image-20210620153815271](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210620153815271.png)

![](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210620154427691.png

![image-20210620154604493](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210620154604493.png)

#### ※ステージング(git add)する際に圧縮ファイルが作成され、コミット(git commit)する際にツリーファイルとコミットファイルが作成される

Gitのデータ管理の補足

Gitのデータの管理の仕方について補足します。
動画資料では正確性よりイメージを掴んでいただくことを優先しています。ここではより正確に、どのようにGitがデータを管理しているのか見ていきます。
イメージがわかっていれば大丈夫だよという場合は飛ばしてください。

## **Gitオブジェクト**

git add や git commit した時、**「圧縮ファイル」「ツリーファイル」「コミットファイル」**が作成されることは前回の動画で見てきました。
Gitではこれらのファイルを「**Gitオブジェクト**」と呼んでいます。Gitオブジェクトは「.git/objects」ディレクトリの下に保存されます。

この3つのGitオブジェクトに関して、より詳しく解説します。

####  **圧縮ファイル**

圧縮ファイルはファイルの中身そのものを圧縮したものでしたね。正確には「**blob（ブロブ）オブジェクト**」と言います。blobというのは「カタマリ」という意味です。ファイルの中身を圧縮しただけのカタマリということになります。

圧縮ファイルのファイル名は動画では「圧縮ファイルA」と書いていましたが、実際はハッシュIDになります。
<u>ハッシュIDというのは、ヘッダー（ファイル内容の文字数など、ファイルのメタ情報）とファイル内容を、SHA-1というハッシュ関数で40文字の英数字に変換したものです。ハッシュIDのうち、先頭2文字をディレクトリ名に、残り38文字をファイル名にして保存します。</u>

実際にどのようなファイル名になるのか、確認してみましょう。

```
# 新しいディレクトリを作成します
$ mkdir sample
 
# そのディレクトリに移動します
$ cd sample
 
# Gitを初期化します。ここまでは前準備です
$ git init
 
# ファイルの中身が「Hello, world!」というgreetingというファイルを作成します
$ echo 'Hello, world!' > greeting
 
# greetingのハッシュIDを表示します
$ git hash-object greeting
af5626b4a114abcb82d63db7c8082c3c4756e51b
```

このようにハッシュIDは、「af5626b4a114abcb82d63db7c8082c3c4756e51b」という40文字の英数字になります。

では次に git add して圧縮ファイルを作成してみましょう。

```
# git add することで圧縮ファイルを作成します
$ git add greeting
 
# .git以下のファイル構造を表示します。以下は今回関係している部分だけを抜粋
$ tree .git
.git
├─ objects
   ├─ af
      └─ 5626b4a114abcb82d63db7c8082c3c4756e51b
```

※ treeコマンドのインストール方法はこのレッスンの末尾に記載しております。

圧縮ファイルは「.git/objects/af/5626b4a114abcb82d63db7c8082c3c4756e51b」として保存されています。

ここで重要なことは、<u>ハッシュIDというのは、ファイルの中身に対して一意になるということです。中身が同じファイルであれば必ず同じハッシュIDになります。そのため、ファイルの中身が同じであれば git add しても追加で圧縮ファイルが作られることはありませんし、ファイルの中身に変更があれば git add すると別の圧縮ファイルが作成されます。</u>

#### **ツリーファイル**

圧縮ファイルは、ファイルの中身を圧縮したものを保存していて、圧縮ファイルのファイル名もファイルの中身をベースにハッシュ関数で作成されたものでした。つまり、圧縮ファイルにはもともとのファイル名の情報がどこにも残っていないことになります。

そこで、ファイル名とファイルの中身の組み合わせ（ファイル構造）を保存するためにあるのがツリーファイルでしたね。コミットをするとツリーファイルが作成されます。ツリーファイルは「treeオブジェクト」と言います。

ツリーファイルは動画で説明したことと実際のファイル構造に違いがあるため注意してください。
動画ではファイル名と圧縮ファイル名の組み合わせを保存したものとして説明しました。実際は、ディレクトリの一つの階層ごとに一つのツリーファイルになっていて、ツリーファイルには圧縮ファイルだけでなくツリーファイルも保存されています。

言葉ではわかりにくいので、具体的に見てみましょう。
なお、Gitオブジェクトの中身を確認するには`git cat-file -p <オブジェクト名>` （オブジェクト名はGitオブジェクトのハッシュIDやブランチ名など。詳細は公式ドキュメントの[SPECIFYING REVISIONS](https://git-scm.com/docs/gitrevisions#_specifying_revisions)を参照）コマンドを使用します。

```
# コミットしてツリーファイルを作成します
# -m オプションを付けることでエディタを立ち上げずにコミットできます
$ git commit -m 'add greeting'
[master (root-commit) ae682f6] add greeting
 1 file changed, 1 insertion(+)
 create mode 100644 greeting
 
# master ブランチ上での最後のコミットが指しているツリーファイルの中身を表示します
$ git cat-file -p master^{tree}
100644 blob af5626b4a114abcb82d63db7c8082c3c4756e51b    greeting
```

最後のコミットが指しているtreeには、blobオブジェクト「af5626b4a114abcb82d63db7c8082c3c4756e51b」が greeting というファイル名だ、ということが保存されています。ここまでは動画の通りです。

ではここで、ディレクトリを追加してコミットすると何が起こるでしょうか。

```
$ mkdir subdir
 
# subdir ディレクトリの下に goodmorning というファイルを作成します
$ echo 'Goodmorning!' > subdir/goodmorning
 
$ git add subdir
$ git commit -m 'add subdir'
[master 75458c8] add subdir
 1 file changed, 1 insertion(+)
 create mode 100644 subdir/goodmorning
 
# ツリーファイルのIDを取得するために、最後のコミットの中身を表示します
# git cat-file -p master^{tree} コマンドでも大丈夫です
$ git cat-file -p HEAD
tree acd75d1289b95787ecaab96c73fe1f3dbfa9cf67
parent ae682f61f39b5c364781cb179035ae534c56a326
author kiyodori <メールアドレス> 1493763216 +0900
committer kiyodori <メールアドレス> 1493763216 +0900
 
add subdir
 
# ツリーファイルの先頭の文字を指定して、ツリーファイルの中身を表示します
$ git cat-file -p acd75d
100644 blob af5626b4a114abcb82d63db7c8082c3c4756e51b    greeting
040000 tree 60ac1b2d01e7f0c21178dcc2e767fb9a24d97124    subdir
```

blogオブジェクトに関してはさっきと同じです。そこに、treeオブジェクト「60ac1b2d01e7f0c21178dcc2e767fb9a24d97124」のツリー名は subdir だよ、というのが追加されています。

ここが注目ポイントで、ツリーファイルの中にツリーファイルが含まれているんですね。このように、ツリーファイルは一つのディレクトリに対応していて、ツリーファイルの中にツリーファイルと圧縮ファイルが含まれるようになっています。

![img](https://img-c.udemycdn.com/redactor/2017-05-02_23-51-17-dd32f15788229597d47c38d427e46429/%E8%A3%9C%E8%B6%B3%EF%BC%9A%E3%83%84%E3%83%AA%E3%83%BC%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E6%A7%8B%E9%80%A0.png?Expires=1624258093&Signature=AslVTbIj6q0k79x-jAldbquuVHx72xdV-0TXWevAj9xn3~-Kr3Le3IAmwC704LPdJEJZuOyhKRmen1mJ3DOEQjdzRSFrPSO6GelBxW~RBR3A51-LVtxRWgpXvYc7c6rXkuLjfVChCTf4N0akt1uygXuOwp6eqeEkOTysuBrg6pyU6lb0LNCHCz0de4B7fIqgvgAv~wuAzlz4o2C8yT8DQ0b7p5uPYvQKibcqDBHj73HCRBRFov0Oop2bzJ5B~I5hlnUZkIbv5GZjqxgRar4H6Pw53uZ~p5AjFVlISunyE54NAlUmzUnpbmhvAyr7sqy5hDuPOfDpsN3StdBGfvxyaw__&Key-Pair-Id=APKAITJV77WS5ZT7262A)

図. ツリーファイルの構造

一応 subdir のツリーファイルの中身も確認しておきましょう。

```
# ツリーファイルの先頭の文字を指定して、ツリーファイルの中身を表示します$ git cat-file -p 60ac1b100644 blob fa476f276a6fa984a789416f63f925e999834081    goodmorning
```

subdir ディレクトリには blobオブジェクト「fa476f276a6fa984a789416f63f925e999834081」がgoodmorning というファイル名で保存されています。

ここまでを振り替えると、一つのファイルに一つの圧縮ファイルが対応していて（※）、一つのディレクトリに一つのツリーファイルが対応していることがわかります。ツリーファイルは構造や名前を持たない圧縮ファイルに構造を与えるためのもので、圧縮ファイルやツリーファイルを保存しているのです。

※ ファイルの中身が同じでファイル名が違う場合、圧縮ファイルはファイルの中身をベースに作成されるため、圧縮ファイルは同じものになります。

**コミットファイル**

ツリーファイルが作成されたことで、ファイルの構造がわかるようになりました。しかしまだ、いつ、誰が、何を、何のために変更したのかということがわかりません。

そこで、その情報を保存するためにあるのがコミットファイルでした。コミットファイルは正確には「commitオブジェクト」と言います。

早速コミットファイルの中身を確認してみましょう。

```
# 最新のコミットファイルの中身を表示します
$ git cat-file -p HEAD
tree acd75d1289b95787ecaab96c73fe1f3dbfa9cf67
parent ae682f61f39b5c364781cb179035ae534c56a326
author kiyodori <メールアドレス> 1493763216 +0900
committer kiyodori <メールアドレス> 1493763216 +0900
 
add subdir
```

まず、コミットした時点のtree「acd75d1289b95787ecaab96c73fe1f3dbfa9cf67」が保存されています。これはこのプロジェクトの一番上のディレクトリのツリーファイルになります。一番上の階層のツリーをコミットファイルに保存することで、コミットした時点でのスナップショットを記録しています。

次がparent、親コミットを保存しています。親コミットは「ae682f61f39b5c364781cb179035ae534c56a326」です。Gitはこのように親コミットを保存することでコミットの履歴を辿れるようにしているんでしたね。

あとは作成者の名前とメールアドレス、改行、コミットメッセージと続きます。これで、変更者と変更理由がわかります。

![img](https://img-c.udemycdn.com/redactor/raw/2018-02-13_20-44-46-edc283eb5f892eb4c8098ff8953e9be3.png?Expires=1624258093&Signature=GW9IOG-XaKrWD4GaO9CedVqr70~iIlwV8AFgeLeKmyJQv53TxSaOFa~AK2~tCqgSQV7jmFVnytMFImSfZ-wdbWxxSWL0A4phMnYdpSSLbaHLKxXUuVeSEdac-IobTE42OzeLaQ5aFJq5n~XjoUtHMLF0uR6XBN8lQcgrpWpxZVNH5QFiAryV68xZNOA5tL171V6qJGgTmTIhy1J4m0OArJ5lrRm4sl3G59gyDDH-RY2-rBv43WmG869uTd2DEIiKVBegPxhkVPTvtnoQQGukA4LS5Uaybjz4AusksIVUKpcm~eCbphXP78R4ZRWGOX-oYRoU9S9oX8woWIRuoV-Ylg__&Key-Pair-Id=APKAITJV77WS5ZT7262A)

図. コミットファイルの構造

**まとめ**

Gitは変更履歴を保存する時、圧縮ファイル、ツリーファイル、コミットファイルという形でスナップショットを記録しています。
Gitの実体は基本的にはこれだけです。とてもシンプルですね。

Gitのコマンドは、この3つのGitオブジェクトに対して何らかの操作をしているだけです。
これから色々なコマンドを学んでいきます。その時、コマンドを闇雲に覚えるのではなく、このデータ構造に対してどういう操作をしているコマンドなのかということをイメージしてもらえれば、Gitが実際どのようなことをしているかがわかると思います。

それでは次回から、Gitの具体的なコマンド、操作に進んでいきましょう。



#### ※ treeコマンドのインストール方法

**Macの場合**

Homebrewを使ってインストールします。ターミナルで下記コマンドを実行してください。

```
$ brew install tree 
```

以上でtreeコマンドが使えるようになります。

もしHomebrewを使われていない場合は、下記URLのインストールのスクリプトをターミナルに貼って実行してください。

https://brew.sh/index_ja.html 

**Windowsの場合**

\1. ホームディレクトリ直下に `.bashrc` ファイルを作成します (`~/.bashrc` )

\2. そのファイルに以下を記載します。

```
alias tree='cmd //c tree //A //F'
```

\3. Git Bashを再起動します。

※ 初回起動時にエラー文が表示されますが、問題ないため無視して大丈夫です。

これでtreeコマンドを使用できるようになります。

![image-20210621233258432](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210621233258432.png)

```
git add . ワークツリーの変更すべてステージに追加したい場合
```

![image-20210621234446025](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210621234446025.png)

![image-20210622230941231](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210622230941231.png)

![image-20210625000731449](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210625000731449.png)

![image-20210625005306595](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210625005306595.png)

![image-20210626002657098](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210626002657098.png)

![image-20210626003332037](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210626003332037.png)

# 初回push時 に-uオプションを付けて以下のコマンドを実行すると次回以降は`git push`だけでpushできるようになる

```
git push -u origin master
```

![image-20210627205239659](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210627205239659.png)

![image-20210627205948334](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210627205948334.png)



![image-20210629225009906](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210629225009906.png)

![image-20210629225721140](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210629225721140.png)

### HEADとは今自分がいるブランチの最新のコミットのこと

