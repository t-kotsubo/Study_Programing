
### コンテナ型仮想化
コンテナ型仮想化技術では仮想化ソフトウェアなしにOSのリソースを隔離し、仮想OSにします。この仮想OSをコンテナと呼びます。


### ホストOS型仮想化
OS上にインストールした仮想化ソフトウェアを利用し、ハードウェアを演算により再現しゲストOSを作り出す仕組みはホストOS型の仮想化と呼びます。（VMware　PlayerやOracle VirtualBoxに代表される仮想化ソフトウェアはこれに分類されます。）

![image-20200417110451030](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200417110451030.png)



## Docker Hub

Dockerイメージのレジストリ。GitHubと同様にユーザーや組織がリポジトリを持つことができ、リポジトリでそれぞれのDockerイメージを管理しています。

## Docker Compose

複数のDockerコンテナを跨いで運用管理を行うツール

## Docker Swarm

複数のサーバー（ノード）を跨いだDockerコンテナ群の運用管理を行う

※複数のノードを跨いで多くのコンテナ群を管理する手法をコンテナオーケストレーションと言う。

※コンテナオーケストレーションで使用されている代表的なOSSとしてKubernetesがある。（DockerSwarm以上に

機能が充実し、拡張性が高いのが特徴）

---

## Dockerfile

Dockerfileは、Dockerのイメージを自動で作成してくれるファイル。`dockerbuild.`と入力するだけで、DockerシステムはDockerfileを自動で読み込み、書かれている内容の通りのDockerイメージを作成してくれます。

---

## Dockerfileでよく使われる命令コード一覧

| 項目       | 内容                                                         |      |
| ---------- | ------------------------------------------------------------ | ---- |
| FROM       | ベース（コンテナのひな型）となるDockerイメージ（OS）を定義する |      |
| LABEL      | メタデータを提供します。メンテナ情報を含めるのに良い場所です。 |      |
| ENV        | 永続的な環境変数を設定します。                               |      |
| RUN        | コマンドを実行してイメージレイヤを作成します。パッケージをコンテナにインストールするために使用されます。 |      |
| COPY       | Dockerを動作させているホストマシン上のファイルやディレクトリをDockerコンテナ内にコピーするためのインストラクションです。 |      |
| ADD        | ファイルとディレクトリをコンテナにコピーします。ローカルの.tarファイルをアンパックできます。 |      |
| CMD        | 出来上がったイメージをDockerコンテナとして実行する前に行われるコマンドを定義。実行中のコンテナにコマンドと引数を提供します。パラメータは上書きできます。コンテナ起動時に1度実行されます。 |      |
| WORKDIR    | あとに続く説明の作業ディレクトリを設定します。               |      |
| ARG        | ビルド時にDockerに渡す変数を定義します。                     |      |
| ENTRYPOINT | 実行中のコンテナにコマンドと引数を提供します。引数は存続します。 |      |
| EXPOSE     | ポートを公開します。                                         |      |
| VOLUME     | 永続データにアクセスして保存するためのディレクトリマウントポイントを作成します。 |      |

Dockerfileの参考サイト：
http://docs.docker.jp/engine/articles/dockerfile_best-practice.html



## DockerイメージとDockerコンテナの関連性

| 名称               | 役割                                                         |
| :----------------- | :----------------------------------------------------------- |
| **Dockerイメージ** | Dockerコンテナを構成するファイルシステムや、実行するアプリケーションや設定をまとめたもので、コンテナを作成するための利用されるテンプレートとなるもの。 |
| **Dockerコンテナ** | Dockerイメージを基に作成され、具現化されたファイルシステムとアプリケーションが実行されている状態。 |

---

## Dockerコマンド一覧


### Dockerのコマンド全般について調べる

```
docker help
```

### Dockerの特定のコマンドについて調べる

```
docker コマンド名　--help
```

### Dockerの特定のサブコマンドについて調べる

```
docker コマンド名 サブコマンド名 --help
```

### DockerHubに登録されているリポジトリを検索する

```
docker search [options] 検索キーワード
```


### Dockerイメージをpullする

```
docker image pull [options] リポジトリ名[:タグ名]
※タグ名を省略した場合はデフォルトタグ（多くの場合latest)が利用される
```

### Dockerイメージにタグをつける
```
docker image tag 元イメージ名[:タグ] 新イメージ名[:タグ]
```

### Dockerホストに保持されているイメージの一覧を表示する

```
docker image ls
```

### Docker imageを公開する/レジストリに登録する

```
docker image push [options] リポジトリ名[:タグ]
※Docker Hubのレジストリ登録する場合は予め「docker login」コマンドでDocker Hubへのログインが必要
```

### Dockerイメージをビルドする

```
docker image build -t イメージ名[:タグ名] Dockerfile配置ディレクトリのパス
※タグ名を省略したときはlatestとなる
```

### Dockerイメージの特定のバージョンに任意のタグをつける

```
docker image tag 元イメージ名[:タグ] 新イメージ名[:タグ]
例）example/echoのlatestに0.1.0のタグをつける場合
docker image tag example/echo:latest example/echo:0.1.0
```

### Dockerイメージ名：タグ名を変更する
```
dokcer tag イメージID イメージ名：タグ名
```



### コンテナを作成して起動する

#### docker runコマンド

```
docker container run [options] イメージ名[:タグ][コマンド] [コマンド引数]

docker container run [options] イメージID[コマンド] [コマンド引数]
```


##### ●docker container runでよく利用されるオプション

| オプション | 機能                                                         |
| ---------- | ------------------------------------------------------------ |
| -i         | docker起動後にコンテナ側の標準入力を開いたままにする※1       |
| -t         | ターミナルを有効にする ※1                                    |
| -p         | 「Windows側ポート番号:コンテナ側ポート番号」のようにポートマッピングを指定 |
| -e         | 環境変数（enviroment variables)を設定する                    |
| --rm       | コンテナ停止時にコンテナを破棄する                           |
| -v         | ホストとコンテナ間でディレクトリ、ファイルを共有するときに使用する |
| -d         | バックグラウンドで実行する ※2                                |
| --name     | コンテナ名を指定する                                         |

※1: -i -t もしくは-itのセットの形式でよく利用される
※2: -p ホスト側のポート：コンテナ側のポートの形式で指定する



##### 環境変数をホストOS側からゲストOS（コンテナ）に渡して起動する

###### ●コマンド引数で環境変数を「コンテナ」渡す（-e --env）
###### 【変数名と値を指定して渡す】

```
docker run --env [ 変数名=値 ] [ その他のオプション ] [イメージ名] [コマンド]
docker run -e [ 変数名=値 ] [ その他のオプション ] [イメージ名] [コマンド]

例) docker run -e hoge=$fuga -e piyo="hogera" alpine env
```

###### 【ホストの環境変数のまま渡す】

```
docker run --env [ ホスト側変数名 ] [ その他のオプション ] [ イメージ名 ] [ コマンド ]
docker run -e [ ホスト側変数名 ] [ その他のオプション ] [ イメージ名 ] [ コマンド ]

例）docker run -e hoge -e piyo alpine env
```

###### ●コマンド引数から外部ファイルで環境変数を「コンテナ」に渡す（--env-file）

###### 【ホストの環境変数のまま渡す】

```
docker run --env-file [ ファイルパス ] [ その他のオプション ] [ イメージ名 ] [ コマンド ]

例) docker run --env-file $(pwd)/myEnvFile alpine env
```



### コンテナを起動する（作成は行わず、既存のものを起動する）

```
sudo docker start コンテナ名またはコンテナID
```

### コンテナの一覧を表示する

```
docker container ls [options]
```

| 項目         | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| CONTAINER ID | コンテナに付与される一意のID                                 |
| IMAGE        | コンテナ作成に使用されたDockerイメージ                       |
| COMMAND      | コンテナで実行されているアプリケーションのプロセス           |
| CREATED      | コンテナが作成されて経過した時間                             |
| STATUS       | Up（実行中）、Exited（終了）といったコンテナの実行状態       |
| PORTS        | ホストのポートとコンテナポートの紐づけ（ポートフォワーディング） |
| NAMES        | コンテナにつけられた名前                                     |

### コンテナ一覧でコンテナIDだけを抽出する

```
docker container ls -q
```

### コンテナ一覧から「filter」を使って抽出する

```
docker container ls --filter "filter名=値"
１．コンテナ名で検索する場合
docker container ls --filter "name=値"
例）コンテナ名：echo1で抽出する場合
docker container ls --filter "name=echo1"

２．イメージで抽出する場合
docker container ls --filter "ancestor=値"
例）イメージ名：example/echoで抽出する場合
docker container ls --fileter "ancestor=example/echo"
```

### 終了したコンテナ情報を含めて一覧を表示する

```
docker container ls -a
```

### コンテナを停止する
```
docker container stop コンテナIDまたはコンテナ名

※すべてのコンテナを停止する場合
docker container stop $(docker ps -q)
```

### コンテナを再起動する
```
docker container restart コンテナIDまたはコンテナ名
```

### コンテナを破棄する
```
docker container rm コンテナIDまたはコンテナ名
※通常、docker container rmコマンドでは実行中のコンテナを破棄することはできないが、-fオプションをつけることで実行中のコンテナの停止・削除まで行うことが可能
```

### イメージを破棄する
```
docker image rmi [イメージID]
```

### 標準出力のログを取得する

``` 
docker container logs [options] コンテナIDまたはコンテナ名
```

※一般的にDockerコンテナにおけるログとは、コンテナに標準出力として出されるものを指す。

### 実行中のコンテナでのコマンド実行
```
docker container exec [options] コンテナIDまたはコンテナ名 コンテナ内で実行するコマンド
```
### コンテナ間、コンテナ・ホスト間でファイルをコピーする

```
docker container cp [options] コンテナIDまたはコンテナ名:コンテナ内のコピー元 ホストのコピー先

docker container cp [options] ホストのコピー元 コンテナIDまたはコンテナ名:コンテナ内のコピー元
```
### 不要なイメージ・コンテナを一括削除

```
docker image/container prune[options]
```

### 不要なDockerリソースを一括削除

```
docker system prune
※利用されていないDockerコンテナやイメージ、ボリューム、ネットワークといった全てのDockerリソースを一括で削除する場合
```

### コンテナ単位でのシステムリソースの利用状況を確認する
```
docker container stats [opiotns] [表示するコンテナID...]
```

※topコマンドのDocker版のようなもの


### Dockerコンテナのシェルの中に入る
```
docker exec -it コンテナ名 bash
```

### Dockerコンテナの内部IPアドレスを確認する

１．実行中のコンテナに入る

```
docker exec -it コンテナID/コンテナ名 /bin/bash
```

２．コンテナ内で以下のコマンドでIPアドレスを確認する

```
hostname -i
```

### Dockerコンテナの内で公開しているポート番号が外部から見てどのポート番号にマッピングされているか調べる

例）Docker コンテナ内の Web アプリケーションがポート番号 `5000` で動作しているとして、それが、Docker ホスト側から見て、どのポート番号にマッピングされているかを調べる場合

```
docker port container_name 5000
```



### Docker コンテナのログを取得

```
docker container logs コンテナID/コンテナ名
```

---

## MariaDB Docker コンテナ作成

### DBサーバーインスタンスの静止
```
docker run --name 任意のコンテナ名 -e MYSQL_ROOT_PASSWORD=rootユーザーに設定するパスワード -d mariadb:タグ名（バージョン名）
```

### MariaDBのインスタンスに外部から接続
```
docker run --name コンテナ名 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=rootユーザーのパスワード -d mariadb:tag --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci


docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=new_mariadb -e MYSQL_USER=kotsubo -e MYSQL_PASSWORD=kotsubo -d mariadb:latest --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci


docker run --name mariadb -p 3306:3306 --env-file /home/kotsubo/DockerLearning/.env -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=kotsubodb -e MYSQL_USER=kotsubo -e MYSQL_PASSWORD=kotsubo -d kotsubodb:1.0 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

#### ●DockerのMySQLイメージ起動時に渡す環境変数

| 環境変数                     | 内容                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| MYSQL_ROOT_PASSWORD          | この変数は必須のもので、MySQLにおけるスーパーユーザである`root`アカウントに設定するためのパスワードを指定します。<br />`root`ユーザはデフォルトで作成され`MYSQL_ROOT_PASSWORD`変数により指定されたパスワードが設定されます。 |
| MYSQL_DATABASE               | この変数はオプションで、イメージの起動時に作成するデータベースの名前を指定します。もしユーザ名とパスワードが指定された場合（下記を参照）はユーザはこのデータベースへのスーパーユーザアクセス権（`GRANT ALL`に相当）を与えられます。 |
| MYSQL_USER<br>MYSQL_PASSWORD | これらの変数はオプションで、新規ユーザの作成とそのユーザのパスワード設定に使用されます。このユーザは`MYSQL_DATABASE`変数で指定されたデータベースに対してスーパーユーザとしての権限（上記を参照）を与えられます。 |
| MYSQL_ALLOW_EMPTY_PASSWORD   | この変数はオプションで、`yes`を設定することで、`root`ユーザに空のパスワードを設定してコンテナを起動することを許可します。 |
| MYSQL_RANDOM_ROOT_PASSWORD   | オプションの変数で、`yes`を設定することで、`root`ユーザのための初期パスワードを（`pwgen`を利用して）ランダムで生成します。生成されたパスワードは標準出力に表示されます。（`GENERATED ROOT PASSWORD: ...`） |
| MYSQL_ONETIME_PASSWORD       | （`MYSQL_USER`で指定されたユーザではなく）rootユーザにおける初回のログインのパスワード変更を強制するために一度でパスワードを期限切れにするための設定を行います。 |

参考ページ：https://hub.docker.com/_/mariadb　「Enviroment Variable」より



## VirtualBoxの仮想マシン上のポートフォワーディング設定

1. VirtualBoxの仮想マシンの「設定」→「ネットワーク」→アダプター１のタグの「高度」→「ポートフォワーディング」をクリックする

![](C:\Users\USER\Desktop\設定1.png)



2. 右側のプラスボタンをクリックしてポートの設定を行う
 ![](C:\Users\USER\Desktop\設定2.png)

   ※名前は任意のものでOK

   参考サイト：

https://8oclockis.blogspot.com/2018/04/virtualbox.html


## TaraTermへの接続

![image-20200424114552683](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200424114552683.png)



![image-20200424114700852](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200424114700852.png)

## MySQL Workbenchへの接続
![image-20200424113435872](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200424113435872.png)



---

## Django Dockerコンテナ作成

参考サイト：https://djangobrothers.com/blogs/django_docker/

### Dockerコンテナ内のディレクトリを作業ディレクトリと共有してコンテナを起動する

```
 docker run -itd -p 127.0.0.1:8000:8000 -v ホストディレクトリの絶対パス:コンテナの絶対パス イメージ名 --name  コンテナ名前（任意）
 
 例）
docker container run -itd -p 8000:8000 --env-file /home/kotsubo/DockerLearning/.env -v /home/kotsubo/DockerLearning/Django/src:/code --name django_kotsubo django_kotsubo:1.0

docker container run -itd -p 0.0.0.0:8000:8000 --env-file /home/kotsubo/DockerLearning/.env -v /home/kotsubo/DockerLearning/Django/src:/code --name django_kotsubo django_kotsubo:1.0
```

※ホストのディレクトリをDockerのコンテナから参照できるようにする。

参考サイト：
https://qiita.com/homines22/items/2730d26e932554b6fb58
https://qiita.com/Yarimizu14/items/52f4859027165a805630



### 認証情報を環境変数に格納する

参考サイト：

https://e-tec-memo.herokuapp.com/article/172/



### 設定ファイルを開発用と本番用に分割する

参考サイト：
https://medium.com/@kjmczk/django-multiple-settings-2a4c15c7c7b0
https://qiita.com/okoppe8/items/e60d35f55188c0ab9ecc



![](C:\Users\USER\Desktop\VB_Django_port設定.png)



---

## VS codeとの接続

![image-20200428094857802](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200428094857802.png)