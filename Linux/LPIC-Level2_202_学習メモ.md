# LPIC-Level2 (202) 学習メモ



## NFSサーバー

NFSサーバでエクスポートするディレクトリの設定は「/etc/exports」ファイルで行います。
ディレクトリのアンエクスポートは「/etc/exports」ファイルを利用する以外にも、exportfsコマンドで行う事ができます。

### 書式
```
exportfs [オプション] [ホスト名：ディレクトリ名]
```
### オプション
![image-20210514002632086](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210514002632086.png)

参考サイト：
https://www.ibm.com/docs/ja/aix/7.1?topic=e-exportfs-command

---

## POP、IMAPの違い

「POP」では、メールをいったんスマホやパソコンにダウンロードして取り込むと、サーバーからは無くなってしまう（何日間は消さずに残すという設定もできる）。郵便局の私書箱から手紙を取ってきたら、私書箱の中は空っぽなるのと同じだ。だが、「IMAP」では、ダウンロードするのはメールのいわばコピー（キャッシュ）で、メール本体はサーバーにいつまでも残ったままなのだ。つまり、**ユーザーのメールはサーバーが管理してくれる**というわけだ。

#### IMAPとは

IMAP(Internet Message Access Protocol)とは、メールサーバー上のメールを管理するプロトコルの事で、現在のバージョンは4なので、IMAP4とも呼ばれています。

![IMAPとは](https://www.jpita.or.jp/pc/swfu/d/imap4.jpg)

IMAPでは、メールはサーバー上に保管され、閲覧などの必要性がある場合だけ取り出す仕組みです。メールサーバー上に複数のフォルダーを作り、メールの管理やメール検索などの機能もサーバー側で行うことができます。

メールサーバーにメールを保存しておくので、複数のパソコンからメールサーバーにアクセスして、自分のメールを読むことができます。また、POPのようにメールをすべてダウンロードする必要がないため、ネットワークにかかる負荷も軽減できます。

![[check]](https://www.jpita.or.jp/pc/image/face/check.png)IMAPはメールの送信はできません。メールの送信はSMTPを用います。

#### POPとは

POP(Post Office Protocol)とは、メールサーバーに保管されているメールを取り出すために利用する、最もベーシックなプロトコルです。現在のプロトコルバージョンが3なので、POP3とも呼ばれています。

![POPとは](https://www.jpita.or.jp/pc/swfu/d/pop3.jpg)

POPでは、メールサーバー上のメールをダウンロードする基本的な手順だけが決められています。通常の利用方法では、メールは端末側にダウンロードし、端末側で管理します。

メールは端末に保管されるので、フォルダーに分類したり、検索する機能は、すべて端末側のソフトウェアで行います。ISPなどのメールアドレスを利用する場合、ほとんどPOPが使われています。



![IMAPとPOPの違い](https://www.jpita.or.jp/pc/swfu/d/imap.jpg)



参考サイト：https://time-space.kddi.com/ict-keywords/kaisetsu/20170824/2081

https://www.jpita.or.jp/pc/index.php?201301014

---

## Devecot

ユーザのメールボックスに配信されたメールにリモートからアクセスできるようにするソフトウェアとしてMRA（Mail Retrieval Agent）が存在します。MRAは主にPOP3/POP3SやIMAP/IMAPSを扱うソフトウェアのことを指します。
![【図を表示】](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6614/k30255.jpg?X-Amz-Expires=600&X-Amz-Date=20210613T053336Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210613%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=9a41206a5616d712e7598e91d0da6a19db6c4af76fd5b2a0068cc6429e9dd8c8)

POP3もIMAPもリモートサーバ上のメールボックスにアクセスするプロトコルですが、以下の点が大きく異なります。

■POP3（Post Office Protocol - Version3）/POP3S（POP3 over SSL/TLS）
・リモート（サーバ）のメールボックスからローカルにメールをコピーしてくる。基本的にはコピー時に削除を行うため、リモートにメールは残らず、メールをコピーしたローカルのMUAはリモートと切断したオフライン状態でも、ローカルに取得済みのメールにアクセスできる。
・POP3は110/tcpのウェルノウンポートを使用。
・SSL/TLSに対応したPOP3Sは995/tcpを使用。

■IMAP（Internet Message Access Protocol）/IMAPS（IMAP over SSL/TLS）
・メールは基本的にリモート（サーバ）上に保存される。そのためメールボックス内の検索処理もサーバ上で動作することになる。メールをローカルに保存せずに済むので、複数の端末からメールボックスにアクセスしてもメールの処理状況（未読管理など）が変わらない。
・IMAPは143/tcpのウェルノウンポートを使用。
・SSL/TLSに対応したIMAPSは993/tcpを使用。

以下は代表的なMRAであるDovecotの説明と設定例です。

■Dovecot（ダブコット）
POP3/IMAPをサポートする、多くのディストリビューションで導入されているMRA。Maildir及びmbox形式のメールボックス、SSL/TLS対応のPOP3SおよびIMAPSもサポートしている。

以下は設定ファイルである「dovecot.conf」の例です。（Dovecot1.x）
![【図を表示2】](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6611/kk30255.jpg?X-Amz-Expires=600&X-Amz-Date=20210613T053336Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210613%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=c83df94f6a844fd7235ec7e69f110a12e06e7477291019fe6c2261a867985c3b)
なお、上記はDovecot1.xの設定例であり、「dovecot.conf」に設定が集約されていますが、Dovecot2.xの設定は、デフォルトでは「/etc/dovecot/dovecot.conf」＋「/etc/dovecot/conf.d/*.conf」となっていて、例えば、上の例で取り上げられている項目のうち、「mail_location」は「10-mail.conf」に記述、「mechanisms」は項目名が「auth_mechnisms」に変更され、「10-auth.conf」に記述されています。

・Dovecot1.xとDovecot2.xの設定の違いについて
上述の「mail_location」ように「conf.d」配下のファイルに記述場所が変更になっても、記述方法そのものは変わらない項目も多いですが、一方、Dovecot1.xとDovecot2.xでは記述方法が違ったり、設定項目の名前が違ったりする場合もあります。例えば、Dovecot2.xでは、「protocols」の記述について、imapsはimapに、pop3sはpop3に含まれることになりました。Dovecot2.xでprotocolsにimapsやpop3sを記述してDovecotを起動するとエラーとなります。設定項目の名前も記述方法も違う例としては、SSL/TLSを使用する際の基本的な項目があります。
以下はDovecot2.xの「10-ssl.conf」に設定するSSL/TLSを使用する際の基本的な項目です。（対比用に、「dovecot.conf」に記載されるDovecot1.xの記述についても触れています。）
![<img src="/mondai3/img/jpg/k31758.jpg">](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6612/k31758.jpg?X-Amz-Expires=600&X-Amz-Date=20210613T053336Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210613%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=e9c04e4145086b8fbf72fa152b724eb19f53e66ee3eda3bd12f6dc49f93bc859)

以下は「10-ssl.conf」を表示させたものです。
SSL/TLSを有効にし、サーバ証明書と秘密鍵を指定しています。
![<img src="/mondai3/img/jpg/kk31758.jpg">](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6613/kk31758.jpg?X-Amz-Expires=600&X-Amz-Date=20210613T053336Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210613%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=c39ea5870c8da853cd18986d1da24f27e97e69797036addad02067cc5f3f4e74)
なお、この例ではサーバ証明書と秘密鍵を同じファイルに格納しています。（設定項目は別ですが、それぞれに同じファイルを指定することで使用可能です。ただし、鍵が一緒ですのでファイルの扱いには注意が必要です。）

・doveconf
Dovecotの設定内容を表示できるコマンドです。上記のように「conf.d」配下の複数のファイルに渡る設定内容を、ファイル1つ1つ確認するのは大変ですし、間違いやすくもなります。doveconfは、こうした場合でも、コマンド1つで設定全体を確認できます。また、標準以外の設定だけを表示することも可能です。

コマンドの書式は以下のとおりです。

doveconf [オプション]

以下は主なオプションです。
![【図を表示4】](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6615/kkkk30255.jpg?X-Amz-Expires=600&X-Amz-Date=20210613T053336Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210613%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=1687acc35dbf473746ae972d31f6c86559b079dc02498fe724796c88dccff356)

以下はコマンドの実行例です。
設定ファイルに「/etc/dovecot/dovecot.conftest」を指定して、標準以外の設定を表示しています。
表示されている中で、例えば「auth_mechanisms」や「disable_plaintext_auth」は、「/etc/dovecot/dovecot.conftest」に記述の項目ではなく、「/etc/dovecot/conf.d」配下の「10-auth.conf」に記述されている内容ですが、「10-auth.conf」など個別のファイルを指定しなくても標準以外の設定であることが確認できます。
![【図を表示5】](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6616/kkkkk30255.jpg?X-Amz-Expires=600&X-Amz-Date=20210613T053336Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210613%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=1b1387d091b8d9dfdc2fb17e8ff8976a9e94d0a2e385bad051c601df94772a3b)

・doveadm
Dovecotの設定の再読み込みや、プロセスの停止など、さまざまな管理が行えます。

コマンドの書式は以下のとおりです。

doveadm サブコマンド

主なサブコマンドは以下のとおりです。
![【図を表示6】](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6617/kkkkkk30255.jpg?X-Amz-Expires=600&X-Amz-Date=20210613T053336Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210613%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=970bb6c8dfe398b65c951cdcdd02bd80214f9d5ff741a6582ad5f4805c10b66b)

以下はコマンドの実行例です。
ユーザー「mailuser2」のメールボックスを表示させ、「test」フォルダを作成しています。
![【図を表示7】](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6618/kkkkkkk30255.jpg?X-Amz-Expires=600&X-Amz-Date=20210613T053336Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210613%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=33b27867056149e999cbd3837ec1c32c21d909e7f8b31dc30d58c81170521609)



---

## Apache

### Apacheの制御用コマンド
Apacheの制御用コマンドには、RedHat系では「apachectl」、Debian系では「apache2ctl」コマンドがあります。
apachectl(apache2ctl)コマンドの書式およびサブコマンドは以下のとおりです。

```
apachectl [サブコマンド]
apache2ctl [サブコマンド]
```

![image-20210515105738745](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210515105738745.png)

Apacheを終了するには以下のように起動スクリプトを使用する方法もあります。

```
・RedHat系：　/etc/init.d/httpd stop
・Debian系：　/etc/init.d/apache2 stop
```

systemdの場合は、例えばRedhat系の場合は、以下となります。

```
systemctl stop httpd.service
```



### Apacheの設定ファイル「httpd.conf」のログ関連のディレクティブ

![image-20210515110009244](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210515110009244.png)



### BASIC認証

BASIC認証を導入するための主な作業は以下のとおりです。

・**htpasswd**コマンドを使用しパスワードファイルの作成およびユーザの登録を行う
パスワードファイル名は通常「.htpasswd」が使われます。設置場所は外部からアクセス出来ない場所を選びます。

htpasswdコマンドの書式とオプションは以下のとおりです。

```
htpasswd [オプション] ファイル名 ユーザ名
```

![image-20210516063624294](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516063624294.png)

なお、パスワードの変更およびユーザの追加はオプションなしで行います。

・必要であれば、グループファイルの作成およびグループの登録を行う
グループファイル名は通常「.htgroup」が使われます。作成は手作業で行います。グループファイルの書き方は以下のとおりです。

```
グループ名：ユーザ名 ユーザ名 ･･･
```

・Apacheの設定ファイルhttpd.confまたは、外部設定ファイル.htaccessでユーザ認証によるアクセス制限を加えたいディレクトリの設定を行う

以下は**httpd.conf**のBASIC認証とダイジェスト認証に関するディレクティブをまとめたものです。

![image-20210516063827174](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516063827174.png)

例1）「/home/test/html」ディレクトリへアクセスする際、test1とtest2ユーザを認証対象とする場合

```
<Directory "/home/test/html">
AuthType Basic
AuthName "Enter your ID and Password!"
AuthUserFile /tmp/.htpasswd
Require user test1 test2
</Directory>
```

例2）「/home/test/html」ディレクトリへアクセスする際、testusersグループに属しているユーザを認証対象とする場合

```
<Directory "/home/test/html">
AuthType Basic
AuthName "Enter your ID and Password!"
AuthUserFile /tmp/.htpasswd
AuthGroupFile /tmp/.htgroup
Require group testusers
</Directory>


```

なお、以下のようにするとパスワードファイルにエントリがあるすべてのユーザが認証対象となります。

```
Require valid-user
```

認証対象のユーザやグループ以外は認証が拒否されます。

### Apache 設定ファイル(httpd.conf)の主なサーバー処理関連ディレクティブ

![image-20210516162307554](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516162307554.png)



### Apache ユーザー認証

Apacheでのユーザ認証には**BASIC認証(基本認証)**と**ダイジェスト認証**があります。
BASIC認証はMIMEエンコード（簡単にデコードされやすい）を使用しているため、<u>SSLなどを併用し、セキュリティを確保しなければなりません</u>。しかし、古いブラウザでも使用できるなど広くサポートされているという利点があります。

ダイジェスト認証の場合はMD5による暗号化が行われているなど、セキュリティが確保されていますが、BASIC認証と違い<u>ダイジェスト認証をサポートしていない古いブラウザでは使用することが出来ない</u>などの制約があります。



### Apache外部設定ファイル

Apacheの設定ファイルhttpd.confでディレクトリ毎の設定を行う場合は、<Directory>セクションを利用します。しかし、例えばそれぞれのユーザが自身のホームディレクトリを公開していて、ディレクトリ（ユーザ）毎に異なる設定を行いたい場合は、管理者がディレクトリ（ユーザ）毎の設定をhttpd.confに記述するのはかなりの手間です。Apacheには、外部設定ファイルをそれぞれのディレクトリに配置することで、httpd.confの内容を上書き出来る機能が用意されています。

外部設定ファイルを使用するには以下のようにします。

・AccessFileNameディレクティブで外部設定ファイルを指定する
デフォルトの外部設定ファイル名は「.htaccess」です。

・AllowOverrideディレクティブで外部設定ファイルの利用を許可（または禁止）する
AllowOverrideディレクティブで指定するパラメータによって、外部設定ファイルで使用できるディレクティブを制限することが出来ます。なお、AllowOverrideディレクティブは、外部設定ファイルを許可するディレクトリの設定を行う<Directory>セクション内に記述する必要があります。

・外部設定ファイルを許可したディレクトリに外部設定ファイルを配置する
外部設定ファイルの書式はhttpd.confと同じです。使用できるディレクティブが制限されている場合を除き、<Directory>セクションで記述が可能な設定を外部設定ファイルでも設定することが出来ます。

以下はhttpd.confの外部設定ファイルに関するディレクティブをまとめたものです。

![image-20210517223531865](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210517223531865.png)

例）全てのユーザのホームディレクトリ「/home/*」において、外部設定ファイル「.htaccess」による設定をすべて許可する場合
```
AccessFileName .htaccess
<Directory "/home/*">
AllowOverride All
</Directory>
```



### バーチャルホスト

Apacheには1台のサーバで2つ以上のWebサイトを管理できるバーチャルホストという機能があります。

バーチャルホストには以下の2つの種類があります。

#### ・名前ベースのバーチャルホスト
**ひとつのIPアドレスに複数のドメイン名を設定するバーチャルホストのことを名前ベースのバーチャルホストといいます。**
<u>**名前ベース**の場合、Listenディレクティブではなく、**NameVirtualHostディレクティブ**で受け付けるIPアドレスの設定を行います</u>。これでひとつのIPアドレスを複数のバーチャルホストで共有する事を示します。また、異なるドメイン名で同じIPアドレスを返すようにDNSを設定（CNAMEで別名を作成）する必要があります。
なお、IPアドレスではなく、「*」（80番ポートの場合は*:80、など）を指定することで、全てのインターフェイスに対して名前ベースのバーチャルホストでサービスを行うことができます。

例1)IPアドレス192.168.1.105で「www.abc.com」と「www.xyz.com」を管理する場合

```
NameVirtualHost 192.168.1.105

<VirtualHost 192.168.1.105>
ServerName www.abc.com
DocumentRoot /var/www/virtual/abc
</VirtualHost>

<VirtualHost 192.168.1.105>
ServerName www.xyz.com
DocumentRoot /var/www/virtual/xyz
</VirtualHost>
```

例2)上記の例で、特定のインターフェイスではなく、すべてのインターフェイスの80番ポートで同様のバーチャルホストをサービスする場合

```
NameVirtualHost *:80

<VirtualHost *:80>
ServerName www.abc.com
DocumentRoot /var/www/virtual/abc
</VirtualHost>

<VirtualHost *:80>
ServerName www.xyz.com
DocumentRoot /var/www/virtual/xyz
</VirtualHost>
```

#### ・IPベースのバーチャルホスト
**複数のIPアドレスにそれぞれ異なるドメイン名を設定します。**<u>受け付けるIPアドレスの設定は**Listenディレクティブ**を使用します。</u>

例）IPアドレス192.168.1.105で「www.abc.com」を、IPアドレス192.168.1.106で「www.xyz.com」を管理する場合

```
Listen 192.168.1.105:80
Listen 192.168.1.106:80

<VirtualHost 192.168.1.105>
ServerName www.abc.com
DocumentRoot /var/www/virtual/abc
</VirtualHost>

<VirtualHost 192.168.1.106>
ServerName www.xyz.com
DocumentRoot /var/www/virtual/xyz
</VirtualHost>
```



---

## Squid

### Squidの設定ファイルsquid.confの主な設定項目

![image-20210515110306847](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210515110306847.png)



###  squid.confのaclの書式と主なACLタイプ

**書式**

```
acl acl名 aclタイプ 文字列|ファイル名

例）ユーザhogeを認証対象として、ACL名passwordを定義する場合
acl password proxy_auth hoge
```

**主なACLタイプ**
![image-20210516064729037](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516064729037.png)

参考：
SquidでBASIC認証を使用してユーザ認証を行うには以下のような設定が必要です。

・設定項目auth_paramで認証方式(basic)、認証プログラムおよびパスワードファイルを指定する
・設定項目aclでaclタイプproxy_authを使用して認証対象を定義する
・設定項目http_accessで認証対象の認証を行う事を設定する

それぞれの設定項目の書式は以下のとおりです。

auth_param 認証方式 program 認証プログラム パスワードファイル
acl acl名 proxy_auth ユーザ名
http_access deny|allow [!]acl名 ...

例）パスワードファイル「/usr/local/passwd」に記載されているユーザ全員をBASIC認証の対象とする場合
なお、認証プログラムは「/usr/local/squid/libexec/ncsa_auth」とする。

auth_param basic program /usr/local/squid/libexec/ncsa_auth /usr/local/passwd
acl password proxy_auth REQUIRED
http_access allow password

設定項目aclの「proxy_auth」で認証対象を「REQUIRED」と指定すると、パスワードファイルに記載されているユーザ全員が認証対象となります。
なお、認証対象外のユーザは認証が拒否されます。

参考サイト：
https://www.atmarkit.co.jp/ait/articles/0904/08/news120_2.html


---

## SAMBA

### 【Sambaの提供するドメインとSambaの変遷】

Sambaは、バージョンアップするごとにWindowsの様々な機能をオープンソースで実現してきたプログラムですが、それゆえ機能や用語にLinuxではなじみの薄いものも少なくありません。ドメインやドメインコントローラという用語もその1つと思われます。

Samba4で実現した機能の中で最も大きなものは、WindowsのActive Directoryでドメインコントローラになれることです。
**Active DirectoryとはNTドメインに変わるネットワーク管理システムのことです。**
**NTドメインとは<u>ネットワーク上のWindowsマシンをまとめる単位</u>のことで、<u>ドメインにログオンしたユーザはドメイン内の共有リソースに認証を行うことなくアクセスすることが出来ます</u>。ドメインコントローラと呼ばれるサーバで、ドメインに属するマシンのアカウントを管理します。**
これまで、Samba3でもドメインコントローラの機能は持っていましたが、この場合のドメインはNTドメインを指し、WindowsNT時代のドメイン管理手法を実現するものでした。<u>Windows2000以降、Windowsドメインの管理手法はActive Directoryを使ったドメイン管理であり</u>、Linuxでも機能の実現が待たれていたものの1つです。Active Directoryは、標準の技術の組み合わせだけでなく、マイクロソフトの独自拡張があるため、Linuxの汎用のサービスの組み合わせでは実現できませんでした。
<u>Samba4では、マイクロソフトからの協力も得てこれらの独自拡張にも対応し、Active Directoryのドメインコントローラ（ADドメインコントローラ）を構成できるようになりました。</u>
従前の試験ではSamba3までが対象でしたので、Sambaによるドメインコントローラと言えばNTドメインを指しましたが、Samba4からは「NTドメイン」「ADドメイン」2つの可能性がありますので注意が必要です。

Samba3とSamba4の具体的な違いを確認します。

### デーモン
Sambaの各サービスについては、<u>**Samba3**</u>までは以下の各デーモンが提供していました。

![image-20210515113155966](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210515113155966.png)

Samba4がADドメインコントローラとして稼働する場合は、起動するプログラムが「samba」というプログラムに統一されています。必要に応じて「samba」プログラムから上表の各機能が呼び出されます。
一方、Samba4であっても、旧来のSamba3のファイルサーバ等の機能のみを使ってADのメンバーサーバになるように構成した場合は、sambaではなく、Samba3同様上記の各デーモンをそれぞれ起動することになります。
なお、ディストリビューションによってはADドメインコントローラとして構成できるSambaのパッケージは用意されていない場合もあります。例えば、CentOSでyumを使って提供されるパッケージでは、現時点ではADドメインコントローラになる機能は提供されていません。
なお、ADドメインコントローラの状態でもファイルサーバ機能等は提供できますが、一部制約が出て、非推奨の使い方となります。

**・機能**
Samba3とSamba4では、ドメインコントローラ機能や名前解決の機能など、一見共通している機能が実装されていますが、それぞれに相違がありますので注意しましょう。デーモン（プログラム）以外の主な相違点は、以下の通りです。

![image-20210515113331753](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210515113331753.png)

**・ドメインコントローラ**
前述のとおり、Samba4 はADドメインコントローラとして機能できます。

**・認証方法**
ユーザの認証方法は、NTドメインではチャレンジレスポンス方式を利用したNTLMv2認証が使用されます。一方、ADドメインでは、認証にKerberosを使用します。Kerberos認証には、1つの認証でユーザが複数台のサーバへアクセスすることが出来るなど、様々な機能があります。（Kerberos認証についての詳細はLevel3の範囲ですのでここでは割愛します。）

**・名前解決**
NTドメインでは名前解決にNetBIOS名とIPアドレスを対応付けるWINSを利用するため、Samba3はWINSサーバの機能を持ちます。<u>ADドメインではDNSとの連携が求められるため、Samba4ではDNSとの連携が可能になりました</u>。外部のDNSサーバを利用することも可能ですが、自らがDNSサーバとして動作することもできます。

**・情報ストア**
ADドメインでは情報の保管場所としてLDAPを使用しますので、Samba4ではLDAPも内蔵しています。

**・ファイルサーバ機能**
Samba4では、ファイル共有プロトコルのSMB2に加えて、パフォーマンスの改善や暗号化などの機能が追加されたSMB3（Windows 8およびWindows Server 2012から搭載）対応となりました。

**・その他（管理ツール）**
ドメインコントローラを管理するために、Samba4では「samba-tool」とサブコマンド群が準備されています。ドメインコントローラ構築時にはsamba-toolコマンドの使用が必須となりますが、その後の管理はWindowsServerと同様GUIのツールでも行えます。

### Samba設定ファイル(/etc/samba/smb.conf)

Sambaの設定ファイル「**/etc/samba/smb.conf**」には3つの特別なセクションである**[global]**、**[homes]**、**[printers]**セクションと、個々の共有の設定を行う任意の名前のセクションがあります。

以下は[global]セクションのログ設定に関わる部分の記述例です。

![image-20210516065835159](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516065835159.png)

#### [global]セクションで使用されるログ設定に関わる主な設定項目

![image-20210516065738812](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516065738812.png)



---

## sendmail / Postfix

### 「Postfix」のメールキュー関連コマンド

![image-20210515211441713](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210515211441713.png)



### 「sendmail」のメールキュー関連コマンド

![image-20210515211906225](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210515211906225.png)



### 参考：

電子メールを処理するソフトウェアには以下の3つがあります。

**・MUA(Mail User Agent)**
ユーザがメールを送受信するためのプログラムです。
作成されたメッセージは**SMTP（Simple Mail Transfer Protocol）**を使用して**MTA**に渡されます。また、メールを受信する際は**POP（Post Office Protocol）**や**IMAP(Internet Message Access Protocol)**を使用します。
例)Windowsメール、iOSメール、Mozilla ThunderbirdMozilla Thunderbird
参考サイト：https://e-words.jp/w/%E3%83%A1%E3%83%BC%E3%83%AB%E3%82%BD%E3%83%95%E3%83%88.html



**・MTA(Message Transfer Agent)**
メールの配信と受信を行うプログラムです。
MTAは受信したメールが自サーバ宛のメールかどうかを判別します。自サーバ宛のメールは**MDA**へ渡し、自サーバ宛ではないメールは他の**MTA**に転送します。転送先のMTAはDNSサーバに問い合わせ（MXレコードを参照）して決めます。MTA間のメールの送受信はSMTPを使用します。
例）sendmail、Postfix、qmail
参考サイト：https://xtech.nikkei.com/it/article/COLUMN/20060419/235638/


**・MDA(Mail Delivery Agent)**
自サーバにあるMTAから受信したメールを、それぞれのユーザのメールスプールに配送するプログラムです。

![image-20210516215100113](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516215100113.png)

**MUA**はパソコンの中に存在し、**MTA**と**MDA**はSMTPサーバーの中に存在する。
参考サイト：https://wa3.i-3-i.info/word11121.html

**Postfix**はLinuxでよく使用される**MTA（Message Transfer Agent）**です。sendmail（MTAの1つ）と互換性があり、設定が容易でセキュリティーが高いことが特徴です。

Postfixの主な設定ファイルは「/etc/postfix/main.cf」です。main.cfでは「設定項目 = 値」という形式で設定内容を記述していきます。
Postfixの設定ファイル「/etc/postfix/main.cf」の書式と主な設定項目には以下のものがあります。

### Postfixの設定ファイル「/etc/postfix/main.cf」の書式と主な設定項目

設定項目 = 値[,値]

![image-20210516215516632](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516215516632.png)


main.cf内では以下の記述もできます。
・「#」で始まる行はコメントとして扱う
・値を「$設定項目名」とすることで、他の設定項目に指定した値を参照できる
・一つの設定項目に複数の値を指定する場合はカンマ（,）で接続する
・改行して空白（スペース）で始めることで、直前の行からの継続として扱う

また、Postfixは複数のデーモンから構成されており、これらデーモンの設定を「**/etc/postfix/master.cf**」ファイルで行います。
master.cfの書式はmain.cfとは異なり、以下のように8つのフィールドがあり、各行でそれぞれのサービス（デーモン）の設定を行います

![image-20210516215808124](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516215808124.png)

以下はmaster.cfの各フィールドをまとめたものです。
![image-20210516215742564](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516215742564.png)

chrootを「y」とすることで、指定したデーモンをchroot jailモードで起動させることができ、セキュリティを向上させることができます。なお、master.cfの編集以外にも必要な作業はありますが、それらを自動的に設定するためのスクリプトが用意されており、これを使うことでchroot jail環境の構築作業を簡略化することができます。
例えばCentOS7では「/usr/share/doc/postfix-2.10.1/examples/chroot-setup/LINUX2」にchroot jail環境構築用のスクリプトが用意されています





---

## LDAP (Lightweight Directory Access Protocol)

### ディレクトリサービスとは

**ディレクトリサービス**とは、ネットワーク上の資源とその所在や属性、設定などの情報を収集・記録し、検索できるようにしたシステム。そのような機能をを提供するコンピュータやソフトウェアのことを「ディレクトリサーバ」（directory server）という。

参考サイト：https://e-words.jp/w/%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9.html#:~:text=%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%A8%E3%81%AF%E3%80%81%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF,%E3%80%8D%EF%BC%88directory%20server%EF%BC%89%E3%81%A8%E3%81%84%E3%81%86%E3%80%82

### LDAPとは

**LDAP**とは、インターネットなどの[TCP/IPネットワーク](https://e-words.jp/w/IPネットワーク.html)で[ディレクトリサービス](https://e-words.jp/w/ディレクトリサービス.html)にアクセスするための**通信プロトコル**の一つ。

参考サイト：https://e-words.jp/w/LDAP.html



### OSI (Open Systems Interconnection) 参照モデル

<img src="C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516114409856.png" alt="image-20210516114409856"  />

![image-20210516114605350](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516114605350.png)

参考サイト：https://www.itmanage.co.jp/column/osi-reference-model/



### slapdのコマンドラインオプション

![image-20210516121611619](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516121611619.png)

**参考URL**
[OpenLDAP 2.3 MAN ページ　「SLAPD」：オプション](http://www5f.biglobe.ne.jp/~inachi/openldap/man23/man8/slapd.8.html#lbAE)
[OpenLDAP　Manual Pages「slapd(8C)」：OPTIONS](http://www.openldap.org/software/man.cgi?query=slapd&sektion=8&apropos=0&manpath=OpenLDAP+2.4-Release)

### SLAPD access ディレクティブ

<u>クライアントからLDAPサーバを操作する際、要求者が何者であるのかを確認するための認証作業が行われます。このことを**バインド**と言います</u>。
Linuxシステムでは認証にユーザ名とパスワードを使用しますが、LDAPではエントリのDNとそのパスワードを使用します。つまりDNはLDAPへのログイン時にユーザ名のような役割を果たします。

Linuxシステムで、ログインしたユーザのアクセス権を制限できるように、OpenLDAPでも「**slapd.conf**」の**access**ディレクティブを用いて、バインドしたDN(ユーザ)に応じたアクセス権の設定を行えます。
例えば、バインドしたDN以外のエントリに設定されているパスワードは参照・変更することが出来ないように設定できます(ユーザ自身のみが自身のエントリのパスワードを参照・変更可能)。

accessディレクティブの書式は以下のとおりです。

```
access to アクセス対象 by 要求者 アクセス権 by 要求者 アクセス権 ...
```

複数行にまたがって記述する場合は以下のように2行目以降の行頭にスペースを入れます。
なお、途中にコメントを入れることは出来ません。

```
access to アクセス対象
 by 要求者 アクセス権
 by 要求者 アクセス権
 ...
```

by以降に記述されている条件は順番に処理され、条件にマッチするとそれ以降の条件は処理されません。記述する順番には注意が必要です。

### accessディレクティブの主なパラメータ

![image-20210516120451523](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516120451523.png)

```
例1）全てのエントリのデータはユーザ自身のみが変更可能で、その他の認証済のユーザは参照のみを可能とする場合
access to *
 by self write
 by users read
 by anonymous auth
 
 例2）属性名「telephoneNumber」の値は本人のみ変更することが可能で、その他のユーザは比較にのみ使用可能とする場合
 access to attrs=telephoneNumber
 by self write
 by * compare
 
※ compareの場合は比較結果が真の場合は「TRUE」、偽の場合は「FALSE」が表示されます。
```

「by self write」で、自身のエントリ(バインドしたエントリ)の内容を変更できる権限を与えます。次の「by users read」で認証されているユーザに読み取り権限を与えます。
なお、「by users read」を「by self write」より先に記述すると、自分自身を含む認証済のユーザが「by users read」にマッチし、「by self write」が処理されなくなります。つまり、自身のエントリの内容でも変更できなくなります。したがって、「by users read」は「by self write」より後に記述します。
このように厳しい条件（要求者の範囲が狭い条件）から先に記述する事が大切です。

また、「by anonymous auth」の記述があるのは、LDAPサーバにアクセスする際は必ず認証を行う必要があるためです。認証される前のユーザの為に、anonymousを指定します。この記述がないとそもそも認証ができなくなりますので、注意が必要です。

なお、accessディレクティブでマッチする条件がない場合は、暗黙の条件「access to * by * none」が適用され、アクセスが拒否されます。
また、アクセス制御の設定を何も記述しない場合は「access to * by * read」と同じ条件が適用され、全てのデータを全てのユーザが参照できるようになっています。

上記のことから、アクセス制御が記述されていない場合は以下の設定がされているのと同じことになります。

```
access to *
 by anonymous read
 by * none
```

・すべてのエントリに対して
・全ての未認証（匿名ユーザ）に対しては参照権限を付与する
・暗黙の条件により、マッチしないものはアクセスを拒否する

※OpenLDAP2.3以降slapd.confは廃止の方向であり、ACLもslapd-configを使った新しい設定の方法もありますが、slapd-configを推奨するOpenLDAPのマニュアルでも、ACLに関しては第一の設定方法として、現時点ではslapd.confを使った設定がとりあげられており、本問題集ではslapd.confを使った方法のみ説明しています。

### グローバルセクション / データベースセクション

OpenLDAPサーバの設定ファイル「slapd.conf」には、大きく分けて<u>全体の設定を行う**グローバルセクション**とデータベース毎の設定を行う**データベースセクション**</u>があります。

**グローバルセクション**に使用する主なディレクティブは以下のとおりです。

![image-20210519232301864](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210519232301864.png)

他にも、SASL認証やSSL/TLS関連の設定はグローバルセクションに記述します

**データベースセクション**で使用する主なディレクティブは以下のとおりです。

![image-20210519232344736](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210519232344736.png)

他にも、アクセス制御やレプリケーションを設定する場合もデータベースセクションに記述します。

以下は「slapd.conf」ファイルの例です。

```
# グローバルセクション
include /etc/openldap/schema/core.schema
include /etc/openldap/schema/cosine.schema
include /etc/openldap/schema/inetorgperson.schema

pidfile /var/run/openldap/slapd.pid
argsfile /var/run/openldap/slapd.args

# データベースセクション（databaseディレクティブから開始）
database bdb
suffix "dc=my-domain,dc=com"
rootdn "cn=Manager,dc=my-domain,dc=com"
rootpw secret
directory /var/lib/ldap

access to * by * read

index objectClass eq,pres
index ou,cn,mail,surname,givenname eq,pres,sub
```

###  OpenLDAの設定方法

OpenLDAPの設定方法は、OpenLDAP2.3以降、テキストの設定ファイルから起動時に設定を読み込む一般的な方法から、LDAPを使った動的な設定方法に変更されています。
※slapd.confによる旧来の設定も現時点では可能です。

この新しい設定の方式は「**slapd-config**」と呼ばれ、LDAPのデータベース（ディレクトリ）に保存されている設定データを追加・変更・削除等することで、動的に設定を更新します。これをディレクトリベースの設定と言い、通常は設定変更による再起動等が不要となります。
設定データベースのツリー構造のルートは、DN（識別名）が「**cn=config**」で定義され、変更できません。また、標準では「/usr/local/etc/openldap/slapd.d」以下に設定データがLDIFファイルで格納されます。LDIFファイル自体はテキストファイルなので編集は可能ですが、直接編集は非推奨で、LDAPの作法に則った方法での更新が推奨されます。つまり、設定用のLDIFファイルを定義し、ldapadd、ldapdelete、ldapmodifyといったコマンドにより、データベースを更新します。

以下は、OpenLDAPのマニュアルから、slapd-configで使用される基本的なディレクティブとエントリの例を抜粋したものです。
ディレクティブの先頭の「olc」という文字は「OpenLDAP Configuration」の略です。

![image-20210530154328354](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210530154328354.png)

各エントリのdnを確認すると、全ての設定エントリが赤字で表示した「cn=config」のツリー下にあることがわかります。また、「cn=schema」の2つ目のエントリを確認すると、さらに子エントリがあり、dnが「cn=｛X}core,cn=schema,cn=config」となっていて、「cn=config」から連なる木構造となっていることがわかります。なお、ここで{X}は設定を処理する順序に関係し、Xに0から実行順に数字が入ります。

---

## SSH

### SSH接続

リモートホスト（SSHサーバ）の公開鍵はクライアントの「**~/.ssh/known_hosts**」ファイルに格納されています。
SSHではクライアントがリモートホストに接続する際、ホスト認証が行われます。これは接続先ホストが正しいホストかどうかを確認する（なりすましを防ぐ）ためです。<u>クライアントからの接続時に、リモートホストは自身の公開鍵をクライアントに送信します。クライアントは受け取った公開鍵と、クライアントの「~/.ssh/known_hosts」ファイルに格納されているリモートホストの公開鍵を比べることで正しいホストかどうかを確認します。</u>

---

## NIS (Network Information Service)

[NIS](https://e-words.jp/w/NIS.html)とは、<u>主にUNIX系OSで利用される</u>ディレクトリサービスの一つで、同じネットワークに接続された複数のコンピュータ間でシステムの設定情報を共有することができるシステム。

[ディレクトリサービス](https://e-words.jp/w/ディレクトリサービス.html)およびプロトコルの草分けの一つで、利用者や利用者のグループについての[アカウント](https://e-words.jp/w/アカウント.html)情報や、ネットワークに接続しているコンピュータの[ホスト名](https://e-words.jp/w/ホスト名.html)など、ネットワーク関連の設定情報を複数のコンピュータで共有することができる。セキュリティ機能などを改良した後継版に「NIS+」がある。

NIS (Network Information Service)とは、ネットワーク上にある複数のコンピュータの情報(ユーザ、パスワード等)を一元管理するためのシステムです。

参考サイト：https://wa3.i-3-i.info/word14258.html

https://wa3.i-3-i.info/word14259.html

---

## DHCP

### DHCPサーバの設定ファイル「/etc/dhcpd.conf」で使用される主な設定項目

![image-20210516234305130](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516234305130.png)

---

## セキュリティ

### 主なセキュリティ情報源

![image-20210516235027315](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210516235027315.png)

※セキュリティインシデントとは不正アクセス、ウィルス感染、情報漏えいなどのセキュリティに関する出来事（インシデント）のことです。

---

## DNS

**キャッシュサーバ**とは、LAN内のクライアントからの問合せに対し、クライアントに代わって他のDNSサーバに再帰的に（ルートDNSサーバから順に）問合せ、結果を回答するサーバです。その結果をキャッシュして、次回の問合せよりキャッシュ内の情報をクライアントへの回答に利用します。
また、**コンテンツサーバ**は自身が管理するゾーンに対する問合せのみ回答します。問合せ結果をキャッシュしたり、名前解決が出来ない場合も他のDNSサーバに問合せを転送しません。

**BIND**は上記2つの機能をnamedデーモンが担っていますが、<u>**[djbdns](https://linuc.org/study/knowledge/490/)**はキャッシュサーバの機能を担うデーモン（dnscache）と、コンテンツサーバとしての機能を担うデーモン（tinydns）が分かれています。</u>djbdnsはBINDより安全で設定が容易とされています。



### Bind(named)の設定ファイル 

#### /etc/named.conf の主な設定項目（ステートメント）

![image-20210530155357086](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210530155357086.png)

※**rndc(Remote Name server Daemon Control)** :bind8までに利用されていたndcコマンドを拡張し、遠隔ホストで稼働しているbind9までもコントロールできるコマンドです。

#### optionsステートメントで設定する主なオプション

![image-20210526000042183](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210526000042183.png)

以下はBIND（named）の設定ファイル /etc/named.conf 内の optionsステートメントの記述例です。

![<img src="/mondai3/img/jpg/kk29955.jpg">](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6530/kk29955.jpg?X-Amz-Expires=600&X-Amz-Date=20210525T145832Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210525%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=de0e77ad4867d3e8415431da59fa8f82d3c5227def49f57244c835e9d3c290f2)

#### 参考URL:
[サーバの実験室　「named.conf の設定」：options ステートメント](http://www.nina.jp/server/redhat/bind/named.conf.html#options)
[Red Hat Linux 9　「12.2. /etc/named.conf」：12.2.1.3. optionsステートメント](http://archive.download.redhat.com/pub/redhat/linux/9/en/doc/RH-DOCS/rhl-rg-ja-9/s1-bind-namedconf.html#S3-BIND-NAMEDCONF-STATE-OPT)

---

## iptables

iptablesとは、パケットフィルタリングやNAT（ネットワークアドレス変換）の設定を行う機能およびコマンドのことです。Linuxカーネルにはnetfilterというのパケット処理機能が組み込まれていて、iptablesはこれを利用します。
iptablesを正しく使用する為には、以下の「テーブル」や「チェイン」といった概念を理解する必要があります。

**【テーブル】**
テーブルとは、iptablesで作成するルール群（後述のチェイン）の使用目的を決定するものです。
ルールを作成する際に指定したテーブルによって、デフォルトで使用できるチェインやアクション（後述のターゲット）に制限がかかる等、ルールの使用目的（フィルタリング or NATなど）を明確化する為に用意されています。

試験で問われる主なテーブルは以下の2つです。

・**filter　パケットフィルタリング用(デフォルト)**
**・nat　NAT用**

iptablesコマンドの「-t」オプションでのテーブル指定を省略した場合、常に「filter」テーブルを選択した事になります。

**【チェイン】**
チェインとは、パケットの処理方法を定義したルール群です。チェインにルールを追加していきます。
また同時に、チェインはどのタイミングでルールを適用するかを表します。

**・INPUT**
ローカルホスト（ローカルプロセス）宛のパケットに対してルールを適用

**・OUTPUT**
ローカルホストで生成されたパケットに対してルールを適用

**・FORWARD**
ローカルホストを経由するパケットに対してルールを適用

**・PREROUTING**
入ってきたパケットの内容を書き換えるためにルールを適用

**・POSTROUTING**
出て行くパケットの内容を書き換えるためにルールを適用

テーブル「filter」を指定した場合はデフォルトで「INPUT」「OUTPUT」「FORWARD」が使用でき、テーブル「nat」を指定した場合は「OUTPUT」「PREROUTING」「POSTROUTING」が使用できます。

![image-20210518223147966](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210518223147966.png)

iptablesコマンドでルールを追加する際の書式は以下のとおりです。

```
iptables [-t テーブル名] –A チェイン ルール
```

テーブルを省略すると、filterテーブル（パケットフィルタリング用）が選択されます。

以下はiptablesコマンドの使用例です。

iptables -t filter -A INPUT -s 192.168.120.0/24 -j ACCEPT
iptables -t filter -A INPUT -s 100.1.1.0/24 -j DROP

「-t」オプションで「filter」テーブルを指定していますので、パケットフィルタリング用のルールについて操作する事を意味します。なお、「filter」テーブルの指定は省略可能です。
「-A」オプションでチェインにルールを追加します。「INPUT」チェインにルールを追加していますので、ローカルホスト（ローカルプロセス）宛のパケットに対してルールが適用されます。
「-s」オプションで送信元のIPアドレスを、「-j」オプションでターゲット（アクション）を指定しています。ターゲットとはパケットの具体的な処理方法であり、「ACCEPT」はパケットの通過を許可、「DROP」はパケットを破棄します。

つまり上記のコマンドを入力すると、ローカルホスト宛のパケットをチェックし、送信元IPアドレスが192.168.120.0/24のパケットは許可、100.1.1.0/24のパケットは破棄します。

iptablesコマンドの書式、および主なオプション、ターゲットは以下の通りです。

・iptables [-t テーブル名] –A|D チェイン ルール
指定したチェインにルールを追加(-A)または削除(-D)

・iptables [-t テーブル名] –P チェイン ターゲット
指定したチェインのポリシー(デフォルトとなるターゲット)を設定

・iptables [-t テーブル名] –L|F|X [チェイン]
指定したチェインのルールを一覧表示(-L)、チェイン内のルールを全て削除(-F)、または空のユーザ独自チェインを削除(-X)

・iptables [-t テーブル名] –N チェイン
指定した名前のユーザ独自チェインを新規作成

**ルールで使われる主なオプション**

![image-20210518223341364](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210518223341364.png)

### 主なターゲット（アクション）

![image-20210518223416462](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210518223416462.png)

---

## vsftp

### vsftpd.confの主な設定項目

![image-20210613142303755](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210613142303755.png)

参考サイト：http://linuxjm.osdn.jp/html/vsftpd/man5/vsftpd.conf.5.html

---

## PAM



以下はPAMの設定ファイル(/etc/pam.d/以下にある個々の設定ファイル）の書式と、それぞれの項目をまとめたものです。

PAMの設定ファイルの書式
モジュールタイプ コントロール モジュール [引数]

・モジュールタイプ
その行に記述されているモジュールに何をさせるのか、またはどのようなタイプの認証を行うのかを指定します。
モジュールタイプには以下の4つがあります。
![【図を表示】](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6590/k30185.jpg?X-Amz-Expires=600&X-Amz-Date=20210613T053033Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210613%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=f3fd00fd26001339d3d9cc7a64b3f879fe4cf1e79bd8c7efc008d65297abe009)

・コントロール
モジュールの実行に成功または失敗した際の処理方法を指定します。
コントロールには以下の4つがあります。
![【図を表示2】](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6591/kk30185.jpg?X-Amz-Expires=600&X-Amz-Date=20210613T053033Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210613%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=eb0c1f26f5c9509bf302434279d133f475f6007a454dd8047e617d1dfdff88b5)

・モジュール [引数]
使用するモジュールを指定します。引数がある場合は引数を指定します。
PAMのモジュールは、32ビット版は「/lib/security」ディレクトリ配下に、64ビット版は「/lib64/security」ディレクトリ配下に格納されています。モジュールを絶対パスで記述しない場合は、これらのディレクトリが参照されます。
以下は主なPAMのモジュールです。
![【図を表示3】](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6592/kkk30185.jpg?X-Amz-Expires=600&X-Amz-Date=20210613T053033Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210613%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=0b4e3e2be3ca2537ba171638aead68775f0c9062130a0a36c4064ec1d84d0ade)

以下はPAMの設定ファイルの例です。
auth required pam_securetty.so
auth required pam_unix.so nullok
auth required pam_nologin.so

この場合、pam_securetty.so、pam_unix.so nullok、pam_nologin.soと順番にモジュールが認証（auth）を実行します。requisiteやsufficientコントロールが無いため、最終行まで認証が実行され全てのモジュールが「成功」となっている場合に認証が許可されます。なお、上記例では全てのコントロールが required となっているため、いずれかの行でモジュールの実行に失敗しても最後の行までモジュールの実行を続け、その後、認証を拒否します。このようにすることで不正な侵入者に対し、どの時点で認証に失敗したのかという情報を隠す事ができます。
