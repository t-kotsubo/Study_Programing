
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

### コンテナを作成して起動する

```
docker container run -i -t -d -p ホスト(Ubuntu)側のポート:コンテナ側のポート --name 任意のコンテナ名 元にするイメージ名またはイメージID
```
#### ●docker container runでよく利用されるオプション

| オプション | 機能                                                         |
| ---------- | ------------------------------------------------------------ |
| -i         | docker起動後にコンテナ側の標準入力を開いたままにする※1       |
| -t         | ターミナルを有効にする ※1                                    |
| --rm       | コンテナ停止時にコンテナを破棄する                           |
| -v         | ホストとコンテナ間でディレクトリ、ファイルを共有するときに使用する |
| -d         | バックグラウンドで実行する ※2                                |
| --name     | コンテナ名を指定する                                         |

※1: -i -t もしくは-itの形でよく利用される
※2: -p ホスト側のポート：コンテナ側のポートの形式で指定する


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