# LPIC-Level2 学習メモ



## ランレベル：init

![<img src="/mondai3/img/jpg/kk28723.jpg">](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6201/kk28723.jpg?X-Amz-Expires=600&X-Amz-Date=20210424T072747Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210424%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=2f44b187ab70d6e43cc60a85417e7c54d6bbf84485127a657412ac8c61045507)



## ランレベル変更コマンド

![image-20210424163253537](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210424163253537.png)

ランレベルを変更するコマンドとして使う場合には telinit も init も全く同じものと思って問題ありません。





![image-20210424164216444](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210424164216444.png)



## カーネルパラメータの表示、更新、一覧

![image-20210424164937776](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210424164937776.png)

## systemctl のサブコマンド

![image-20210424165157444](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210424165157444.png)



## ipコマンド

ipコマンドは非常に広範囲を対象としていて、ifconfigがネットワークインターフェース操作を主としていたのに対し、ifconfigと同様の範囲だけでなく、routeやarpといったコマンドの範囲も関係しています。

書式

```
ip [オプション] オブジェクト コマンド
```

主なオプション

```
「-4（IPv4を指定）」「-6（IPv6を指定）」
※これらのオプションは、指定したアドレスがIPv4、IPv6のどちらであるか明確であれば省略が可能です。
```

![image-20210424170235124](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210424170235124.png)



### カーネルイメージが格納されているパーティションを指定

```
set root='(hdディスク番号,パーティション番号)'
例) set root='(hd0,3)'
```



## nmapコマンド

nmap は、詳細が不明なネットワークの構造を調査したり、セキュリティ上の問題がないかを検査する目的で、ネットワークのスキャンを行うことができるコマンドです。このコマンドを利用することで、指定したホストのポートに対して総当たりでパケットを送りつけ、どのようなポートが待ち受け状態にあるかを調べることができます。

```
nmap [スキャンタイプ] [オプション] 対象
```

スキャンタイプ

![image-20210424185913253](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210424185913253.png)

オプション

![image-20210424185933446](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210424185933446.png)

※network mapperの略です。サーバで開いているポートをスキャンするなど、セキュリティモニタリングに使われます。
https://cha-shu00.hatenablog.com/entry/2018/08/01/182920#:~:text=network%20mapper%E3%81%AE%E7%95%A5%E3%81%A7%E3%81%99,%E3%83%A2%E3%83%8B%E3%82%BF%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%AB%E4%BD%BF%E3%82%8F%E3%82%8C%E3%81%BE%E3%81%99%E3%80%82

## nmap 以外のネットワークに関連したユーティリティ系コマンド

![image-20210424183550048](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210424183550048.png)

※ss : ss は socket statistics の略



## unameコマンド オプション



![image-20210424184250864](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210424184250864.png)



## /etc/fstab のオプション

![image-20210424184730433](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210424184730433.png)



## EXTLINUX

EXTLINUXはファイルシステムext2/ext3/ext4/btrfsからLinuxを起動する**ブートローダ**です。
GRUBの代わりのブートローダとして使われることがあります。

EXTLINUXをシステムにインストールするには以下のように「extlinux」コマンドを実行します。

```
extlinux -i|--install ディレクトリ
```



## vmstat

vmstatコマンドは、物理メモリやスワップ領域の詳細な情報や、プロセスやCPUの統計情報などを表示します。

```
vmstat [表示間隔(秒) [回数]]
```

![image-20210424193207847](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210424193207847.png)

r : 実行待ちのプロセス数

b: I/O待ちなどで割り込み不可のスリープ状態にあるプロセスの数

## RAID アレイの状態を確認

Linux システム上で ソフトウエアRAID アレイを作成するには mdadm コマンドを利用し、RAID アレイの状態を確認するには仮想ファイル /proc/mdstat を参照します。

## 同じネットワーク内の IP アドレスと MAC アドレスの対応関係を調べることができるコマンド

arp

ip neigh show

---

## GRUB Legacyの設定ファイル

* /boot/grub/menu.lst や /etc/grub.conf 等(ディストリビューションによって違う)

## GRUB2の設定ファイル

* /boot/grub/grub.cfg

  しかし、「grub.cfg」ファイルを直接編集することはありません。**<u>設定内容は「/etc/default/grub」ファイルおよび「/etc/grub.d」ディレクトリ内のファイルに記述し、「grub-mkconfig（またはgrub2-mkconfig）」コマンドで、設定対象の「grub.cfg」を指定して内容を反映させます。</u>**

GRUB Legacy と GRUB2 では設定ファイルおよび設定方法が異なります。

### 【GRUB Legacyの場合】
GRUB Legacyの設定ファイルは **/boot/grub/menu.lst**、ディストリビューションによっては **/boot/grub/grub.conf** です。

以下は GRUB Legacy の設定ファイル /boot/grub/menu.lst の抜粋です

![image-20210429133742858](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429133742858.png)

<u>一番はじめの部分に 項目=値 という形式で書かれているのは、全般的な設定です</u>。
<u>title とそれに続けてインデント（字下げ）されている部分はひとまとまりで、ひとつの起動設定になっています</u>。
つまりこの部分を複数セット記述すれば、起動時にそれらの設定のうちから選んで起動させることができます。

それぞれの項目は以下のように使用します。

**・title**
各設定の名前を指定する項目
ここで設定した名前が GRUB の起動時メニューに表示されます。

**・root**
<u>カーネルイメージや初期 RAM ディスクイメージの含まれているパーティションを指定する項目</u>
kernel や initrd の項目に記述したパスは、この root に指定したパーティション上のパスと見なされます。
パーティションを指定するには、「root (hdディスク番号,パーティション番号)」のように指定します。その際、<u>番号はどちらも**0**から数えます</u>。

例）
1番目のディスクの1番目のパーティション　→　root (hd0,0)
1番目のディスクの2番目のパーティション　→　root (hd0,1)
2番目のディスクの2番目のパーティション　→　root (hd1,1)

**・kernel**
カーネルイメージファイルを指定する項目
この kernel のパスは、root の項目で指定したファイルシステムにおけるパスとして記述します。カーネルイメージファイルのパスに続けて、起動オプションを指定することができます。

主な起動オプションは以下のとおりです。

![image-20210429133910900](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429133910900.png)

**・initrd**
初期 RAM ディスクイメージファイルを指定する項目
kernel と同じく、root で指定したファイルシステムにおけるパスとして記述します。

### 【GRUB2の場合】
<u>GRUB2の設定ファイルは、標準では「**/boot/grub/grub.cfg**」（CentOS7では「**/boot/grub2/grub.cfg**」）です</u>。一般的なBIOSを使ったシステムは、これに該当します。UEFIを使ったシステムの場合は、ディストリビューション等によって違いますが、一般的には「/boot/efi/EFI/***/grub.cfg」です。***はディストリビューションによって違う値が入ります。CentOSでは「centos」、RHELでは「redhat」、Ubuntuでは「Ubuntu」です。
しかし、「grub.cfg」ファイルを直接編集することはありません。<u>設定内容は「**/etc/default/grub**」ファイルおよび「**/etc/grub.d**」ディレクトリ内のファイルに記述し、「**grub-mkconfig（またはgrub2-mkconfig）**」コマンドで、設定対象の「grub.cfg」を指定して内容を反映させます。</u>
なお、「update-grub」コマンドは「grub-mkconfig」の標準である「grub-mkconfig -o /boot/grub/grub.cfg」を実行するため、BIOSの場合のように、GRUB2の標準のディレクトリ構成である場合は「update-grub」コマンドも使えます。
なお、UEFIにおけるgrub.cfgの記述は、基本的な構文はほぼBIOSの場合と同じですが、詳細はディストリビューションによって扱いが異なる場合がありますので詳しくは個々のディストリビューションをご確認ください。

GRUB2の全体的な設定は /etc/default/grub ファイルに記述します。

![image-20210429134310711](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429134310711.png)



また、カーネルイメージ、ルートパーティションの指定などは /etc/grub.d ディレクトリ内のファイルで行います。

以下は カスタムの設定を記述するファイル /etc/grub.d/40_custom の例です。
![image-20210429134349416](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429134349416.png)

menuentry とそれに続く「{}」で囲まれている部分はひとまとまりで、ひとつの起動設定になっています。
つまりこの部分を複数セット記述すれば、起動時にそれらの設定のうちから選んで起動させることができます。

それぞれの項目は以下のように使用します。
**・menuentry**
各設定の名前を指定する項目（<u>GRUB Legacy の title に相当</u>）
引用符内に名前を設定します。

**・set root='(hdディスク番号,パーティション番号)'**
カーネルイメージや初期 RAM ディスクイメージの含まれているパーティションを指定する項目（<u>GRUB Legacy の root に相当</u>）
<u>GRUB Legacy と異なり、パーティション番号は**1**から数えます。</u>

例）
1番目のディスクの1番目のパーティション　→　(hd0,1)
1番目のディスクの2番目のパーティション　→　(hd0,2)
2番目のディスクの2番目のパーティション　→　(hd1,2)

**・linux**
カーネルイメージファイルを指定する項目（GRUB Legacy の kernel に相当）
GRUB Legacy同様の起動オプションを指定できます。

**・initrd**
初期 RAM ディスクイメージファイルを指定する項目（GRUB Legacy の initrd と同様）

なお、UEFIの場合、ディストリビューションによっては、カーネルイメージの指定や、初期RAMイメージの指定が「linuxefi」や「initrdefi」となっている場合があります。

---

## routeコマンド

route コマンドの使い方を説明します。

表示
route

追加
route add [-host|-net] 宛先アドレス gw ゲートウェイのIPアドレス

削除
route del [-host|-net] 宛先アドレス [gw ゲートウェイのIPアドレス]

追加・削除の場合の宛先アドレスは、以下の形式等が可能です。
IPアドレス/プレフィックス
IPアドレス netmask サブネットマスク

デフォルトゲートウェイ設定
route add default gw デフォルトゲートウェイのIPアドレス

## ipコマンド
ipコマンドは、ifconfigなどの旧来のネットワークコマンドに代わるコマンドです。
ipコマンドは様々な用途に使用できますが、ここでは基礎的なインターフェイスの設定やルーティングの設定について記載します。

以下はipコマンドの書式です。

ip オブジェクト オブジェクトに必要な構文

ここでは、最も基本的な例として、addressオブジェクトとrouteオブジェクトの例をとりあげます。
なお、<u>オブジェクト名は省略した入力が可能で、addressオブジェクトは「addr」や「a」のように指定できます</u>。

ip address コマンドの書式

アドレス表示
ip address show(list) [インターフェイス名]

アドレス設定 追加・削除
ip address { add | del } 宛先アドレス/プレフィックス dev インターフェース名

## ip route コマンドの書式

ルート表示
ip route [show(list)]

ルート設定 追加
ip route add 宛先アドレス via ゲートウェイのアドレス

ルート設定 削除
ip route del 宛先アドレス [via ゲートウェイのアドレス]
routeコマンド同様、削除の場合は、識別が可能な場合は宛先アドレスだけでの削除も可能です。

追加・削除の場合の宛先アドレスは、以下の形式が可能です。
IPアドレス/プレフィックス

デフォルトゲートウェイの追加と削除
ip route { add | del } default via デフォルトゲートウェイのアドレス
または
ip route del default

## modprobeコマンドのオプション

modprobe コマンドは依存関係を自動的に解決してカーネルモジュールのロード・アンロードが行える便利なコマンドです。

![image-20210425123809946](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210425123809946.png)

---

## iSCSI

SCSI（Small Computer System Interface）とは、PCやサーバに直接接続されたハードディスクなどの周辺機器を制御し、データ転送を行うための規格の一つです。このSCSIの機能をTCP/IPネットワーク上で利用できるようにしたものがiSCSI（Internet Small Computer System Interface）という規格です。

SCSI（Small Computer System Interface）とは、PCやサーバに直接接続されたハードディスクなどの周辺機器を制御し、データ転送を行うための規格の一つです。この<u>SCSIの機能をTCP/IPネットワーク上で利用できるようにしたものがiSCSI（Internet Small Computer System Interface）という規格です</u>。

iSCSIを導入するメリットとして、記憶装置とサーバ間のネットワーク（SAN：Storage Area Network）を構築する際、高価なファイバーチャネルではなく、既存のネットワークインフラを使用できること、記憶装置を他のネットワーク機器と同様のネットワーク上で統合管理が可能になること、などが挙げられます。

SCSI（iSCSI）では通常、ホスト側をイニシエータ、デバイス側をターゲットと呼びます。<u>サーバをiSCSIイニシエータとして動作させるには**iscsid**デーモンを起動する必要があります。また、iSCSIイニシエータからiSCSIターゲットへアクセスし、デバイスとして使用可能にするには**iscsiadm**コマンドを利用します。</u>なお、<u>iscsidデーモンとiscsiadmコマンドの設定ファイルは「**iscsid.conf**」です</u>。

![image-20210425131349162](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210425131349162.png)

必要な主な作業は以下のとおりです。

1. iSCSIターゲットの一覧取得およびローカルデータベースへの登録（iSCSIターゲットのあるサーバへ接続）

   ※iSCSIイニシエータでは、iscsiadmコマンドで接続先のiSCSIターゲットの一覧を取得し、ローカルデータベースへ登録する必要があります。
   そのためには、discoveryモードで「-t sendtargets」と「-p IPアドレス[:ポート]」を指定します。「-p」はiSCSIターゲットのある接続先サーバを指定するオプション、「-t sendtargets」は接続先の全てのiSCSIターゲットを、iSCSIイニシエータのローカルデータベースに自動的に登録するオプションです。

   ```
   例）サーバ「192.168.1.9」にあるiSCSIターゲットの一覧を取得し、ローカルデータベースに登録する場合
   # iscsiadm -m discovery -t sendtargets -p 192.168.1.9
   ```

2. 登録済みiSCSIターゲットへログイン

   ※ローカルデータベースに登録されているiSCSIターゲットをデバイスとして使用可能にするには、iSCSIターゲットにiscsiadmコマンドでログインする必要があります。そのためには、nodeモードで「-l」オプションを指定します。

   ```
   例）ローカルデータベースに登録されている全てのiSCSIターゲットへ一括でログインする場合
   # iscsiadm -m node -l
   ```

   

ローカルデータベースに登録する際の「node.startup」の値は、設定ファイル「iscsid.conf」で指定できます。
・自動でログインを行う場合（デフォルト）
node.startup = automatic

・自動ログインを行わない場合
node.startup = manual

---
## initramfs

initramfs 形式のイメージは cpio アーカイブを gzip 圧縮したものです。
<u>initramfs 形式の初期 RAM ディスクイメージをgunzip コマンドで解凍した後、cpio コマンドでアーカイブからファイルへの書き出しを行えば、イメージ内のディレクトリ・ファイルを参照することができます。</u>

**参考**

初期 RAM ディスクは、システム起動時に仮の環境としてまずメモリ上にファイルシステムを展開し、そこでカーネルを動作させてから本来のファイルシステムをルートにマウントし直す、といった段階的なブートを実現する機能です。
各種モジュールや機能を実現するためには、本来のファイルシステムが使用できなければなりませんが、システム起動直後にはファイルシステムにアクセスできる環境が整っていません。つまり、カーネルが起動の最終段階で、本来のファイルシステムにアクセスでき、必要なモジュールをロードしたり、複雑なシステム、例えばLVMサブシステムなどを使用できるようにしたりするお膳立てをすることになります。
高度な機能を使うにはまずカーネルを動作させなければならないので、仮の環境でまずカーネルを動かして、それから本来の環境をブートさせようという発想です。
そのためには仮のファイルシステム環境そのものを保存したイメージファイルが必要になりますが、その形式に2種類があります。initrd 形式と initramfs 形式です。
現在では cpio アーカイブを gzip で圧縮した initramfs 形式の方がよく利用されています。

![image-20210425131846958](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210425131846958.png)

また、initramfs 形式の初期 RAM ディスクは **dracut** コマンドでも作成できます。

```
書式：dracut 出力ファイル名 カーネルバージョン

以下は実行例です。
\# dracut initramfs.img `uname -r`
```

---

### ファイルシステムの種類

![image-20210425132457425](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210425132457425.png)

上記の各ファイルシステム間の移行は、原則としては現行のデータをバックアップし、新しいファイルシステムを作成したのち、バックアップからコピーをするような形になりますが、一部のファイルシステム間では、コマンドにより変換が可能です。
例えば、<u>ext2ファイルシステムはtune2fsコマンドを使ってext3に変換が可能ですし、ext3ファイルシステムからbtrfsファイルシステムへの変換はbtrfs-convertというコマンドがあります</u>。これらの場合も、万が一のためのバックアップは必要ですが、新たにデータを手動でコピーすることなく、新しいファイルシステムに移行することができます。
なお、ファイルシステムの変換ができる場合でも、変換の逆は必ずしも可能ではないことに注意してください。

---

### LVM (Logical Volume Manager)

LVM (Logical Volume Manager) は、物理的な記憶デバイスの領域（物理ボリュームと呼ぶ。Physical Volume の頭文字を取り PV と略す）を複数まとめてひとつの大きな仮想的な領域（ボリュームグループと呼ぶ。Volume Group の頭文字を取り VG と略す）とし、そこから仮想的なパーティション領域（論理ボリュームと呼ぶ。Logical Volume の頭文字を取り LV と略す）を切り出すことで、従来の物理的なパーティションを用いた方法よりも柔軟に記憶領域を管理することができるようにする仕組みです。

LVM を構成する手順は以下の通りです。

1. fdisk コマンドによる LVM 用パーティションの作成
2. pvcreate コマンドによる PV の作成
3. vgcreate コマンドによる VG の作成
4. lvcreate コマンドによる LV の作成
5. mkfs コマンドによるファイルシステムの作成
6. ファイルシステムのマウント

LV のデバイスファイルは **/dev/VG名/LV名** となります。
作成した LV を実際に使うためには、このデバイスファイルを指定してファイルシステムを作成し、マウントを行います。

![image-20210429200404966](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429200404966.png)

なお、create とつくコマンドの他にも、多くの pv, vg, lv 系コマンドが存在します。

![image-20210425133226998](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210425133226998.png)



### lvcreateコマンド

lvcreate コマンドの書式は次のようにします。

![img](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6460/k28875.jpg?X-Amz-Expires=600&X-Amz-Date=20210427T153609Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210427%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=01f387c9968df5a2a08fac36e5876a9c0e4b819f24a97d591840657aa77fa04c)

![img](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6461/kk28875.jpg?X-Amz-Expires=600&X-Amz-Date=20210427T153609Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210427%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=d921feff46291f1a615a1188d5c6c16f8464cc8859ae968e34ebdf73de9fa01c)

---

## /proc ディレクトリ

「/proc」ディレクトリはプロセス、ハードウェアおよびシステムリソースなどの情報を扱うための擬似的なファイルシステムです。そのため、ハードディスク上にファイルは存在せず、システムが起動する際にメモリ上に作成されます。

![image-20210425154052320](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210425154052320.png)

---

## btrfsファイルシステム

btrfsファイルシステムを操作するコマンドは「btrfs」です。
btrfsはスナップショットを特徴とするファイルシステムですが、スナップショットをとる単位として、subvolumeを作成します。

btrfsは比較的新しいLinuxのファイルシステムで、**サブボリューム（subvolume）**を構成し**スナップショット**などの機能を持っています。
btrfsでは、スナップショットをとる単位として、サブボリュームを作成します。
また、既にext3などで作成されているファイルシステムでも、**btrfs-convert**コマンドを使ってbtrfsに変換することが可能です。

![image-20210425154626420](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210425154626420.png)

---

## /etc/inittab のアクション指定子



![image-20210425160858369](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210425160858369.png)

**/etc/inittab** は以下の形式の行が並べられて構成されます。

![image-20210425161136252](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210425161136252.png)

![image-20210425161022578](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210425161022578.png)

---

## Udev関連コマンド

「**udevd**」は「**udev**」と呼ばれる仕組みのためのデーモン（常駐プログラム）です。
udevはデバイスファイルを動的に管理するための仕組みで、ハードウェアがシステムに接続された際に対応するデバイスファイルを作成する役割を持っています。
なお、ハードウェアの検出はudevの役割ではなくカーネルが行っており、デバイスが追加・削除される都度、カーネルからイベントが送信され、udevdはカーネルからその情報を受け取ることで動作しています。このイベントを「uevent」といいます。

![image-20210429131425835](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429131425835.png)

①デバイスを接続します。
②カーネルが仮想ファイルシステム sysfs（/sys）にデバイス情報を作成します。
③カーネルがudevdにデバイス情報を通知します。（uevent）
④udevdが/sysのデバイス情報を確認します。
⑤udevが/devにデバイスファイルを作成します。

udevのメイン設定ファイルは「/etc/udev/udev.conf」です。「/etc/udev/rules.d」ディレクトリ内には、デバイスファイルの作成に関する個別の設定ファイル（ルールファイル）が入っています。

udevに関連したコマンドには以下のようなものがあります。
![image-20210429131447761](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429131447761.png)

Ubuntuなどの新しいディストリビューションでは、udevadmコマンドはudevcontrol、udevinfo、udevmonitorコマンド等を統合したコマンドとして使用されます。サブコマンドに「control」、「info」、「monitor」のように指定することで、上表の統合前の各コマンドに相当する機能を使うことができます。
お手元のシステムでudevmonitorコマンド等が利用できない場合は、udevadmコマンドに統合されていないか調べてみると良いでしょう。

---

## リソースの測定およびプロセスのPIDを確認する際に利用する主なコマンド

![<img src="/mondai3/img/jpg/k29132.jpg">](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6153/k29132.jpg?X-Amz-Expires=600&X-Amz-Date=20210425T141051Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210425%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=dcab47af6922c42296d7b2902f6b394dc1772e7a764c39491406b0fed84f7a23)

---

## カーネルをアップグレードする際、自動的にカーネルモジュールをリビルドできる機能

<u>**DKMS(Dynamic Kernel Module Support)は**、カーネルとカーネルモジュールの依存関係による問題を解消し、カーネルのアップデート時に、自動的にカーネルモジュールを更新するための機能です。</u>
リナックスカーネルをアップデートした際、カーネルモジュールもこれに対応しなければなりません。DKMSは、カーネルアップデートの際に、カーネルとは独立して自動的にカーネルモジュールをコンパイルし、インストールします。 現在、多くのディストリビューションがDKMSをパッケージに含んでいます。DKMSはカーネルヘッダを必要とします。
また、手動によりdkmsコマンドを使ってモジュールを構成したり、対象のカーネルモジュールの状態を表示することも可能です。
主要な設定ファイルは各モジュールの設定を行うdkms.confと、全体の設定を行う/etc/dkms/framework.confになります。

以下は、dkms statusコマンドでDKMSによって構成されるカーネルモジュールの状態を表示させたものです
![【図を表示2】](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6408/kk29245.jpg?X-Amz-Expires=600&X-Amz-Date=20210425T141716Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210425%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=3126f181bdf130abf081077fa43a645be358a16a57f04614d9ab9e3aaad68063)

---

## /etc/fstab のオプション

/etc/fstab のオプション部分には、以下のようなオプションが指定できます。
![<img src="/mondai3/img/jpg/kk28776.jpg">](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6225/kk28776.jpg?X-Amz-Expires=600&X-Amz-Date=20210425T142839Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210425%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=c6cdd1426870c556cbe946621274b2ce75ea8e9fc0d630116c7d433256648fac)

### defaults : async, auto, exec, nouser, rw が指定されるのと同じ設定

---

## tcpdump

各プロトコルがどのような通信を行うのかや、不審な通信が行われていないか等を調べる目的で、ネットワークインタフェース上を流れるパケットを監視（パケットキャプチャ）したいことがあります。
Linux では tcpdump コマンドを使うことでパケットキャプチャを行うことができます。
なお tcpdump はユーザ権限で利用できてしまうとセキュリティ上問題があるため、通常 root 権限でのみ実行できます。

```
tcpdump [オプション] [監視対象の条件式]
```

「監視対象の条件式」部分では以下のような指定を組み合わせて使うことができ、条件に合致したパケットのみが表示されます。
条件式を何も書かなかった場合は、すべてのパケットが対象になります。
![<img src="/mondai3/img/jpg/kk28956.jpg">](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6308/kk28956.jpg?X-Amz-Expires=600&X-Amz-Date=20210425T143151Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210425%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=e058490c566f0eaf38580762c1dca0d4003a42704c65bb123aea5fb3de64bb4f)

```
例) tcpのパケットを監視する場合
tcpdump tcp
例) udpのパケットを監視する場合
tcpdump udp
例）TCP の 21 番を監視する場合
tcpdump port 21
例)IPアドレス192.168.0.100に関する80/TCPのパケットを監視する場合
tcpdump tcp port 80 and host 192.168.0.100
```

条件式は複数のものを組み合わせて利用することも可能です。

また tcpdump の他にも多くのネットワークに関連したユーティリティ系コマンドがあるので、以下にまとめておきます。
![<img src="/mondai3/img/jpg/k28950.jpg">](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6305/k28950.jpg?X-Amz-Expires=600&X-Amz-Date=20210425T143151Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210425%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=e29d5dbc604aae4fc75e8ef4931f0e0b00d376558291ddc290122b6d7c6f0962)

---

## TCPラッパー

<u>**TCPラッパー**とはネットワークサービスに対するアクセス制御を行うプログラムです</u>。デーモン名は**tcpd**、使用するライブラリはlibwrapです。このライブラリをサポートしない（ライブラリにリンクされていない）ものは制御できませんが、多くの主要なネットワークサービスはこのライブラリに対してリンクされていますので、たいていのサービスはTCPラッパーでの制御が可能です。
<u>TCPラッパーには「**/etc/hosts.allow**」「**/etc/hosts.deny**」という二つの主要なファイルがあり、「/etc/hosts.allow」ファイルでアクセス許可の設定を行い、「/etc/hosts.deny」ファイルでアクセス拒否の設定を行います。</u>
「/etc/hosts.allow」と「/etc/hosts.deny」ファイルの変更内容は編集後、TCPラッパーのデーモンであるtcpdや、アクセス制御対象のサービスを再起動しなくても変更内容は反映されます。

tcpdは始めに「/etc/hosts.allow」ファイルをチェックします。条件にマッチした場合はその時点でアクセスを許可し、「/etc/hosts.deny」ファイルはチェックしません。条件にマッチしなかった場合は、「/etc/hosts.deny」ファイルをチェックします。「/etc/hosts.deny」ファイルの条件にマッチすればその時点でアクセスを拒否します。マッチしなかった場合はアクセスが許可されます。
つまり、両方のファイルに記述がない場合はアクセスが許可されることになります。通常は、「/etc/hosts.deny」ファイルに「ALL : ALL」と記述して全てのアクセスを拒否し、「/etc/hosts.allow」ファイルで接続を許可する設定を行います。
「ALL」は全てのサービスまたはホストを表すワイルドカードです。

「/etc/hosts.allow」と「/etc/hosts.deny」ファイルの書式は以下のとおりです。

**サービス名 : ホスト名|IPアドレス**

192.168.10.0/24のようなネットワークを指定する際は以下のように記述します。
192.168.10.　(<u>※末尾に「.」(ドット)が必要</u>)
または
192.168.10.0/255.255.255.0

※末尾に

また、「/etc/hosts.deny」ファイルを使用せずに、「/etc/hosts.allow」ファイルのみでアクセス制御の設定を行うことも出来ます。

この場合の「/etc/hosts.allow」ファイル書式は以下のとおりです。

サービス名 : ホスト名|IPアドレス : ALLOW|DENY

例）192.168.10.0/255.255.255.0からの接続を全て許可し、それ以外は全て拒否する場合。
ALL : 192.168.10.0/255.255.255.0 : ALLOW
ALL : ALL : DENY

---

## systemctl
systemdにおいて、主要な管理コマンドに「systemctl」コマンドがあります。
systemctlコマンドは非常に広範囲をカバーするコマンドで、systemdの処理単位であるユニットや、ユニットの集合体であるターゲットの操作から、OS全体にかかわる操作（OSの再起動や緊急モードの実行など）まで、様々な用途に用いられます。
ここでは、例として、ユニットの基本的な制御、ランレベルに相当するターゲットの変更等について言及します。

systemdにおいて、サービスは、ユニットとして制御されます。ユニットは、所定の位置に配置された定義ファイルで定義され、依存関係などを基に動作が決定されます。通常、ユニットの定義ファイル名はユニット名と同じです。

コマンドの書式は以下のとおりです。

```
systemctl サブコマンド [ユニット名|定義ファイル名]
```

ユニットに関わる主なsystemctlサブコマンドは以下のとおりです。
![image-20210429215038679](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429215038679.png)

以下は、コマンドの実行例です。dkms.service（Dinamic Kernel Modoule Support）の状態を確認しています。
※拡張子を省略すると、「.service」として扱われます。
![image-20210429215112915](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429215112915.png)

次の例は、httpd.serviceの自動起動が解除（disabled）されているのを確認した後、システムの起動時にサービスが自動起動（enable)するように設定しています。

![image-20210429215200683](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429215200683.png)

また、ターゲットはユニットの集合体ですので、ユニットに対するコマンドが同じように使える場合もあります。
以下は、「systemctl status」コマンドで、ターゲットである「default.target」の状態を表示させた例です。
トのランレベルに相当します。

![image-20210429215301627](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429215301627.png)

以下は、各ランレベルとそれに相当するターゲットを対比したものです。
![image-20210429215331786](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429215331786.png)

「default.target」は、正確にはターゲットそのものではなく、デフォルトのランレベルとするターゲットのシンボリックリンクになっています。上記の例では「default.target」はランレベル5に相当する「graphical.target」のシンボリックリンクとなっているため、「systemctl status default.target」で「graphical.target」の状態が表示されています。

以下の例では、現在の「default.target」の内容を確認し、デフォルトで起動するターゲットを「graphical.target」から「multi-user.target」へと変更しています。シンボリックリンクが削除され、再度作成されています。

![image-20210429215404666](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429215404666.png)

「systemctl isolate」コマンドは、引数にターゲット名をとり、そのターゲット以外のユニット、ターゲットを停止し、指定したターゲットを実行します。
こうした動作から、事実上ランレベルの変更（SysVinitにおける「init」コマンドに相当）と同等な使用方法に用いられるコマンドです。

以下は、起動中の「graphical.target」（default.target）から即座に「multi-user.target」に変更した例です。
![image-20210429215612779](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429215612779.png)

なお、ランレベル1やランレベル6に該当する「rescue.target」や「poweroff.target」などの、システム全体の起動・停止に関わるターゲットへの移行は、isolateサブコマンドとは別に、以下のサブコマンドが用意されています。

システム全体の起動・停止に関わるサブコマンドは以下のとおりです。
![【図を表示7】](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6434/kkkkkkk31516.jpg?X-Amz-Expires=600&X-Amz-Date=20210425T144926Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210425%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=51f8595e1608d14ee910e93883cc4c83e902809b3de24d7b5d0ff902bff61b6f)

例えばレスキューモードに移行する場合、「systemctl rescue」とします。
これは「systemctl isolate rescue.target」とほぼ同じですが、特段のオプションを指定しない場合、ローカルシステムの全てのユーザーに警告メッセージが送信される点が異なります。

以下は実行例です。
最初にdefault.targetとrescue.targetの状態を確認してから、「systemctl rescue」コマンドでレスキューモードに変更しています。
![【図を表示8】](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6435/kkkkkkkk31516.jpg?X-Amz-Expires=600&X-Amz-Date=20210425T144926Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210425%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=257d91e787419b08ba38349a6aee1e67dd053a37f23f79950590cc938cdb8c13)

なお、レスキュー（rescure）モードはSysVinitにおけるシングルユーザーモードに該当しますが、緊急（emergency）モードはより最小限の環境を提供し、レスキューモードでも起動できないような時にシステムの修復を試みるためのモードです。
root ファイルシステムのみを読み込み専用でマウントし、他のローカルファイルシステムのマウントは実行しません。ネットワークは使用せず、必須サービスのみを起動します。

---

## free

設問の図を出力するコマンドは「free」です。

freeコマンドはメモリやスワップ領域の使用状況を表示します。

その他の選択肢は出力結果が異なりますので、誤りです。

参考：
freeコマンドはメモリやスワップ領域の使用状況を表示します。

以下はfreeコマンドの実行例およびその表示項目です。
![<img src="/mondai3/img/jpg/k28646.jpg">](https://ping-t-data-tokyo.s3.ap-northeast-1.amazonaws.com/uploads/question_image/file/6131/k28646.jpg?X-Amz-Expires=600&X-Amz-Date=20210425T145307Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZCJ2QHLF73X4YH6P%2F20210425%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=ae599d7f80ca5b1eeae80d8a5af2794111fb53aa655a8e0b068d45253435c872)

「Mem」行
・total　物理メモリの総量
・used　使用中の物理メモリのサイズ
・free　空いている物理メモリのサイズ
・shared　共有メモリサイズ(現在は使用されていないため、常に0)
・buffers　バッファキャッシュのサイズ
・cached　ページキャッシュのサイズ

「-/+ buffers/cache」行
・used　バッファキャッシュとページキャッシュを含まない、使用中の物理メモリのサイズ
・free　バッファキャッシュとページキャッシュを含む、空いている物理メモリのサイズ

「Swap」行
・total　スワップ領域の総量
・used　使用中のスワップ領域のサイズ
・free　空いているスワップ領域のサイズ

---

## オートマウント

Linux には、CD/DVD などのメディアやその他の必要な時だけマウントすればよいファイルシステムを、普段はアンマウント状態にしておいて、マウントポイント内にアクセスがあった時には自動でマウントするという仕組みがあります。
この仕組みを**オートマウント**といい、**automount** デーモンというプログラムによりこの仕組みが実現されます。

オートマウントを利用するためにはあらかじめ、どのディレクトリにどのデバイスをどのようなファイルシステムとしてマウントするのか、設定しておく必要があります。
<u>メインの設定ファイルは **/etc/auto.master** です。これはマスターマップと呼ばれ</u>、その内容は以下のようになっています。

![image-20210427235514206](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210427235514206.png)

**左のフィールドから順に、マウントポイント、マップファイル、オプションを指定します**。オプションは任意です。

マウントポイントの指定方法は、「直接マップ」「間接マップ」の二つの方式があります。
マスターマップにおいて、<u>直接マップでのマウントポイントは、常に「/-」という表記で記載されます。</u>
<u>間接マップでのマウントポイントは、個別のマップファイルに対して、マウントの起点を提供します。</u>ここでは /auto と指定しているので、/auto が自動マウントの起点になります。

<u>**マップファイル**というのは **/etc/auto.master** とはまた別の設定ファイルで、どのデバイスをどのような名前でマウントするのかといった個別のマウント設定を行単位で列挙します。</u>上のマスターマップの例では、/etc/auto.directや/etc/auto.cdromがマップファイルとして指定されています。

マップファイルの書式は以下のとおりです。

マウント名 [マウントオプション] ロケーション（マウントするリソースやデバイス）

例えば、/etc/auto.directの中身は、次のようになっています。

![image-20210427235424462](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210427235424462.png)

直接マップの場合、マップファイルに書かれた1番左のマウント名が絶対パスとなり、マウントポイントとなります。この例の場合、マウントポイントは/mnt/NFSです。

以下は、/etc/auto.cdrom の中身の例です。
![image-20210427235332643](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210427235332643.png)

間接マップの場合、実際にマウントされるパスは、/etc/auto.master で指定するマウントポイントと、マップファイルで指定するマウント名を合わせたものになります。つまり上記の例ですと、/auto/cdrom が自動マウント先となります。

マウントオプション部には mount コマンドや /etc/fstab で設定できるマウントオプションと同じものが使えるほか、-fstype というファイルシステムの種類を指定するオプションが使えます。この例ですと、CD-ROM の形式である ISO9660 としてマウントを行うという設定になっています。-fstypeのデフォルトはNFSです。

ロケーションは、NFSなどによるファイルシステムの場合、/etc/fstabのマウント同じように、NFSサーバ名:マウントされるパス のように指定します。ローカルシステムの場合は、コロン (:) の後にデバイスファイルを指定します。

以上により、例えば/auto/cdrom にアクセスすると自動的に /dev/cdrom が /auto/cdrom に ISO9660 としてマウントされ、利用可能になります。
なお automount デーモンは必要に応じてマップファイルを自動的に再読込するので、マップファイルを編集した場合には、デーモンの再起動は必要ありません。
但し /etc/auto.master を編集した場合には、設定を反映させる為にデーモンの再起動（/etc/init.d/autofs reload など）が必要です。

---

カーネルイメージについては **zImage** と **bzImage** の違いをしっかりと覚えておきましょう。

zImage と bzImage の具体的な制限の違いで重要な点は、<u>zImage は 512KB 以下のイメージしか扱えないという点です</u>。
これは歴史的な経緯で、古いアーキテクチャの仕様に合わせたものだったからです。その後の環境に対応させるために bzImage が開発されました。なのでこちらは 1MB を超えるサイズについても扱えるようになっています。
具体的には、zImage はローメモリと呼ばれる限られたメモリ空間のみを利用し、bzImage はハイメモリ（ユーザースペース）空間を利用できます。
bzImage は zImage と同様に、gzipで圧縮されています。
現在の主流である 2.6 系や 3.x 系のカーネルでは bzImage 形式を使います。

---

### make installをルート権限なしで実行する方法

**./configureに--prefixオプションをつけて、実行ユーザー自身のホームディレクトリを指定する**

make installコマンドでは、ファイルを適切なディレクトリに配置（インストール）します。
インストール先のディレクトリにアクセス権が無い場合には、make installの前にsuコマンドでrootユーザなどの適切な権限を持つユーザになるか、sudoコマンドを用いてroot権限でmake installを実行します。（sudo make install）
別の方法として、./configure実施時に、--prefixを使ってインストール先を実行ユーザーの権限のあるディレクトリに変更して実行することでも対応できます。

例)user1のホームディレクトリをインストール先に指定する

```
./configure --prefix=/home/user1
```

---



## mdadm

Linux システム上で RAID を構築・管理するには、**mdadm** コマンドを利用します。
mdadm には複数のモードがありますが、その中で RAID 情報の表示など雑多な機能を扱うのは Misc モードです。以下のようなオプションを指定すると、自動的に Misc モードとして動作します。

![image-20210429011437859](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429011437859.png)

```
例) デバイス /dev/md0を停止する
mdadm -S /dev/md0
```

※　RAID デバイスには通常は MD（Multiple Device） デバイスと呼ばれる **/dev/md0, /dev/md1** 等を使います。

---

## tune2fs コマンド

ext2/ext3/ext4 の設定を後から行うことができるコマンドは tune2fs です。

![image-20210429012029800](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429012029800.png)

参考：
ファイルシステムを作る mkfs 系コマンド、ファイルシステムをチェックする fsck 系コマンドの他にも、多くのユーティリティコマンドが存在します。
以下の表のコマンドはすべて、作成済みのファイルシステム（デバイス）を引数に取って動作します。

![image-20210429012132464](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429012132464.png)



---

**/usr/src/linux/kernel/カーネル本体のソース**

---

## RockRidge形式

RockRidge 形式は ISO9660 形式のファイル名制限などを緩和するため、独自の拡張を施した CD 系メディア用のフォーマットです。UNIX 系 OS で利用されます。

Linux でこのファイルシステムイメージを作成するには、mkisofs コマンドに -R オプションを指定します。

![image-20210429012844916](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429012844916.png)

---

## rsync

rsyncはネットワーク経由でデータをコピーできるコマンドです。
sshを利用して、安全に離れたホストとデータを同期できますので、遠隔地へのバックアップによく利用されます。

```
sync [オプション] 送信元 送信先
```

![image-20210429013038725](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429013038725.png)

rsyncの構文の送信元や送信先の部分は、ユーザ名やホスト名などを細かく指定できます。
特に遠隔地にバックアップする場合、送信先についての情報が必要です。

```
送信先（送信元）の指定：[ユーザ名@][ホスト:]ディレクトリ
```

例えば、ローカルホストのdirディレクトリを、リモートホスト（ホスト名remote）の/home/yamadaディレクトリへ、yamadaユーザとしてバックアップする場合は、以下のように送信先を指定します。
例） rsync -avz dir yamada@remote:/home/yamada

---

## netstat コマンド

netstat は実行システム上のネットワーク状態について、様々な情報を表示することができるコマンドです。
各ネットワークインタフェースの状態、ポートの待ち受け状態、ルーティングテーブルの状態、パケット数統計など、多岐にわたる情報が取得できます。

```
netstat [オプション]
```

![image-20210429013320220](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429013320220.png)



## SS(socket statistics)コマンド

<u>**ss**コマンドは、**netstat**の後継となるコマンドで、ネットワークに関連した様々な情報を表示します</u>。オプションはnetstatと必ずしも同じではないので、注意が必要です。
現時点では完全にnetstatの代替とはなっておらず、試験でも両方出題の可能性があります。
また、両コマンドとも、さらに複雑なオプション等でTCPのステートによるフィルタなど、非常に多機能にわたっていますが、両方の使い方、使い勝手には差があり、ある程度はどちらも理解しておくことが必要になると考えられます。

コマンドの書式は以下のとおりです。

```
ss [オプション]
```

![image-20210429132915610](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429132915610.png)

---

## /etc/hosts 

/etc/hosts ファイルの書式は以下のとおりです。

ネットワーク内全体で新しいホスト名を利用可能にするには DNS の設定を行う必要がありますが、自分が使うクライアントマシン上でのみ有効なように設定を行うだけならば、/etc/hosts を利用します。
/etc/hosts にはデフォルトでは自分自身を指すホスト名 localhost などが定義されているだけですが、この設定を活用すれば、小さなネットワークであれば DNS を使わずにホスト名で相互にアクセスできる環境を作ることも可能です。

```
IPアドレス ホスト名 [ホスト名...]
```

![image-20210429014323473](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429014323473.png)

---

## automount デーモン

### 特定デバイスを必要な時だけ自動でマウントし、利用できるようにする機能

Linux には、CD/DVD などのメディアやその他の必要な時だけマウントすればよいファイルシステムを、普段はアンマウント状態にしておいて、マウントポイント内にアクセスがあった時には自動でマウントするという仕組みがあります。
この仕組みをオートマウントといい、automount デーモンというプログラムによりこの仕組みが実現されます。



<u>デバイスを認識しデバイスファイルを作る</u>のが **udev**、<u>必要な時にデバイスファイル上のファイルシステムをマウントする</u>のが **automount** です。

---

## tarコマンド

### tarコマンドの主なオプション

![image-20210429115606562](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429115606562.png)

---

##  **UEFI **

・UEFI(Unified Extensible Firmware Interface)

UEFIは、BIOS（レガシーBIOS）に替わる新しい基本ファームウエアで、BIOSにおける様々な制限（※）を乗り越えることを目的として、規格が定められています。
※CPUのモードが16ビットのリアルモードしか使えない、メモリ空間に制限がある、など
GUIでのマウス操作もサポートしており、BIOSよりも高機能化しています。
元々は、EFIというインテルとHPが提唱した規格の発展形であり、現在は、UEFIForumのもとで開発されています。

BIOSを置き換えることを目的に開発されたものですが、現状は、BIOSと完全に排他使用というわけではなく、実装によってBIOSと共存するような形の使用も多くあります。
当然その場合には、BIOSの制約を受けてしまうため、本来のUEFIの機能を利用するには、完全にBIOSの置き換えとして使用するのが望ましいと言えます。しかしながら、長らく続いたBIOS時代の遺産もまだまだ多く、BIOSと併存させることで、既存の環境を生かす構成が多く見られます。また、広義の意味で、UEFIをBIOSとして扱うものあります。

従来、BIOSでは、機器をいったん停止し、再起動時に設定を確認・変更を行っていましたが、UEFIでは、OSから直接に設定を参照・変更できるようになっています。
また、取り入れられている技術的にも様々なメリットがあり、その一つに、大容量ストレージに容易に対応できることがあげられます。近年、ハードディスクをはじめとするストレージの大容量化が著しいですが、レガシーなBIOSでは、この点においても不利で、2TB以上のものは扱えない場合が多くなっていました。現在では、ストレージ側の進歩とそれに伴うソフトウエアの進歩により、必ずしもBIOSの制限で2TBが利用できないわけではありませんが、基本仕様の古さによる機器や設定上の制約があり使いにくさは否めません。UEFIでは、こうした制約は大幅に解消され、大容量ストレージを容易に扱えるようになっています。これは、<u>パーティション・フォーマット等に関する面で、従来の**MBR(Master Boot Record)**を用いた形式から、**GPT（GUIDパーティションテーブル）**を用いた方式に変更することにより、起動時の領域や容量の制限などが大幅に拡張されていることが要因となっています</u>。

**・EFI System Partition (ESP）**
ESPはUEFIシステムにおいて、物理的なマシンを起動し、ファームウエアが読み込まれた後、その後の起動シーケンスで最初にアクセスされる領域になります。ESPは「/boot/efi」にマウントされます。
マザーボードの実装により差はありますが、規格としては、FAT16またはFAT32でフォーマットされている必要があります。

**・UEFIブートマネージャー**
UEFIでは、マシン起動後にファームウエアが読み込まれると、ハードウエアを初期化し、UEFIブートマネージャーを起動します。UEFIブートマネージャーは起動情報（OSをどこからどのようにロードするか）を管理するプログラムであり、役割としては、BIOSでのブートローダーのような役割を実行します。多くの場合は、ブートローダーを起動エントリに持ち、そちらに制御を渡しますが、環境によってはブートローダーなしでの起動も可能です。

**・efibootmgr**
efibootmgrはUEFIブートマネージャーの起動エントリをOS上から操作するコマンドです。
上記のESPに格納されたブートローダーなどのプログラムを管理し、起動パラメータをブートローダーに渡したり、起動順序を変更したりなど、起動エントリの変更や設定を行います。
UEFIは、BIOSと同様にブートローダーを登録することもできますが、UEFI自体にブートローダーと同様の機能をもたすことができます。こうした機能もefibootmgrで操作可能です。
ESPに格納されたブートローダーをUEFIから見ると拡張子.efiがついたファイルとなっていて、efibootmgr上でも、EFIアプリケーションとして扱われます。

以下はefibootmgrコマンドの実行例です。
オプションを付けずに実行すると現在のブートエントリーを表示します。

![image-20210429121300276](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429121300276.png)

**・UEFI shell**
UEFIでは、UEFIシェルと呼ばれるシェル環境を持っており、OSを起動せずにハードウエア周りの設定を行うことができ、デバイスドライバや、TCP/IPスタックも利用できます。
以下はUEFI shellでバージョンを表示させた例です。

![image-20210429121324916](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429121324916.png)

---

##  カーネルモジュール

カーネルモジュールとは、カーネルで扱うべき色々な機能を独立した部品のようなものです。モジュールとしてカーネルから切り離すことでカーネル本体のサイズを小さくし、必要な機能だけをロードしたり、不要な機能はアンロードするというように使用できます。
ファイルとしてのカーネルモジュールは通常 /lib/modules/ 以下にカーネルのバージョンごとのディレクトリがあり、その中に .ko という拡張子で配置されています。

カーネルモジュールを実行時に操作するコマンドには、以下のようなものがあります。

![image-20210429200920771](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429200920771.png)

モジュールによっては動作するための条件として他のモジュールを必要とすることがあります。これを依存関係といいます。
insmod, rmmod コマンドの引数にモジュール名（.ko は含まない）を指定するとロード・アンロードがそれぞれ行えますが、依存関係に問題がある場合は失敗します。そのため依存しているモジュールを先にロードしておいたり、アンロードしたいモジュールに依存しているモジュールを先にアンロードしたりといった順序管理が求められます。

そうした依存関係の解消をすべて人間がやるのは手間なので、自動で行ってくれるコマンド modprobe が存在します。オプションを指定しないとロードが、-r オプションを指定するとアンロードが行えます。
modprobe はモジュールの依存関係を保存しているファイル modules.dep を参照して動作します。modules.dep を最新の情報に更新するためには、depmod コマンドが使えます。

---

## その他のブートローダ

**・systemd-boot（UEFI）**
systemd-bootはsystmd独自のUEFIブートマネージャーで、UEFIで動くEFIアプリケーションの1つです。systemd-bootを使用するにはシステムがUEFIモードで起動しており、ESPパーティションにアクセスできることが必要です。また、ESPにsystemd-bootのバイナリが必要です。

**・U-boot（UEFI）**
U-boot（Universal Boot Loader）はオープンソースの組み込み用のブートローダーです。サイズの制約に対応するため分割されたステージに分けられる仕様となっています。他の多くのブートローダーが起動時にメモリアドレスなどを自動的に配置するのに対し、U-bootでは明示的に指定することが必要です。U-bootのコマンドは低レベルのコマンドで、カーネルをブートするにも複数のステップが必要です。それゆえ、逆に自由度は高くなっています。

**・isohdpfx.bin（BIOS・MBR）**
ISOLINUXは、CDROMやDVDROMなどのオプティカルメディアからの起動のみをサポートするシステムですが、USBスティックなどで、ISOLINUXイメージのMBRコードを使ったブートを可能にし、ブロックデバイスの動作を提供するのが、Isohybridと呼ばれるシステムです。
MBRコードとしてSYSLINUXのMBRコードである「isohdpfx.bin」が使われます。

**・efiboot.img（UEFI）**
UEFIでISOLINUXを使ってブートする際に使われるイメージで、FAT16で作成されています。

**・/EFI/BOOT/bootx64.efi（UEFI）**
UEFIのブートマネージャーであり、標準ではUEFI起動時に読み込まれます。

**・Secure Boot（UEFI）**
UEFIには、システム起動にあたって、署名の確認を行い、起動を制限するSecureBootと呼ばれる機能があります。X.509証明書を使って、署名の識別を行います。Windows8以上のWindows搭載PCは初期状態でSecureBootが有効になっているものもあり、LinuxのインストールにはSecureBootの無効化が必要になる場合があります。

**・shim.efi（UEFI）**
<u>セキュアブート時に最初に読み込まれるUEFIアプリケーションです</u>。UEFI　CA（マイクロソフト）の署名を受けておき、他のブートローダー等の署名検証の役割をすることにより、セキュアブート時の起動を可能したUEFIバイナリです。

**・grubx64.efi（UEFI）**
grubを起動するUEFIアプリケーションです。

---

## AHCI(Advanced Host Controller Interface)

AHCIは、IDEに比べてはるかに高速なシリアルATA (SATA)を活かせるインターフェース仕様として登場した規格で、インテルが策定しています。IDEとの互換性を重視したSATAの規格IDEとの互換性を重視したSATAの規格SATA1.0では速度より互換性が重視され、性能は犠牲となりましたが、SATA2.0でAHCIは規格化され、SATA本来の機能・性能を満たすことができるようになりました。

AHCIでは、ホストのストレージとメモリ間のデータ交換などについて定義されています。
これにより、システムの設計、開発者の負担を減らすことができ、ホットスワップなどの機能が利用できるようになりました。
なお、AHCIも、設計当初からある程度の年月が経ち、現在のハードディスクドライブの主流な接続形態となり、ストレージ接続の標準仕様とも言うべき規格となりましたが、近年急速に普及しているSSDに関しては、AHCIの規格に合わせて対応がなされたため普及に一役買ったものの、SSDの本来の速度性能はハードディスクをはるかに上回っており、AHCI自体がボトルネックとなりつつあります。

**・SSD（Solid State Drive）**
ディスク、という名前がついていますが、実際にはフラッシュメモリに属する機器です。ハードディスクのようなディスクドライブを模した動きをすることから、ディスク、という名称になっています。ハードディスクの速度面を大幅に改善する記憶装置として登場し、ここ数年で非常に大きな進化を遂げ、価格も下がり普及期に入ってきました。インターフェイスの仕様なども、普及を考慮し、ハードディスクと同じ規格が用いられてきましたので、基本的な使用感には差異が少なく、使用に対する障壁は低いですが、取り扱いの留意点にはディスクドライブと違う面もあります。

SSDの特徴として、以下のことがあげられます。

長所
・ランダムアクセス性能に優れる
・省電力・静音
・非接触メディアであるため、耐振動・衝撃性が高い

短所
・高価（ただし、飛躍的に価格は下がってきている）
・書き込み消去により素子が劣化するため、寿命がある（ただし、現実的にはあまり大きな制約にはなっていない）
・故障時のデータ復旧の技術はハードディスクのようには確立されていない

ハードディスクの置き換えとしての側面が重視されたこともあって、インターフェイスはSATAを使用するAHCIによるものが主流として普及しましたが、次第にインターフェイスがボトルネックとなってきています。
こうした背景から、PCI Expressバスを使ったNVMeという規格が生まれてくることになりました。

・NVMe
NVM Express (NVMe) は PCI Express バスから SSD に接続するための規格です。
SATA規格で普及したSSDですが、速度的な制約がボトルネック化しつつあるため、より高速なインターフェイスを必要としたことから発生した規格です。
既存の汎用的に使用されているPCI Expressを使用することで、インターフェイスとしての互換性を高め、フラッシュメモリのストレージに最適化されたバスとして、規格されています。バスとしての基本性能はSATA規格に比べ大幅に向上しています。例えば、上記のAHCI接続は旧来のHDDを前提としたバスであり、キューは1つで、1キューで32命令、という実行制限があるのに対し、NVMeでは、65535キューで65535命令、というように、大きな差があります。
現時点ではPCI Express Gen3 x4などの製品が主流ですが、SATAの規格が規格自体の上限に達しようとしているのに対し、NVMeでは、PCI Expressのレーン数を重ねることなどで、さらなる性能向上も可能となっています。また、NVMeの仕様もそうした拡張に耐えうるものとなっています。

---

システムに接続されている物理的なデバイスにアクセスする方法として、/dev 内の仮想ファイル（デバイスファイル）があります。
記憶装置のデバイスファイルは、接続の形態や位置によって以下のような名前になります。

![image-20210429223914755](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429223914755.png)

---

## systemd 主要ユニット

![image-20210429224752856](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210429224752856.png)

---

## arpコマンド

IP アドレスと MAC アドレスの対応関係は、ARP キャッシュというテーブルとしてシステム内に保持されています（ARP キャッシュについての詳細は解説下部の「参考」をご覧下さい）。
ARP キャッシュに関する操作を行うコマンドは arp です。

```
arp [オプション]
```

主要なオプションは以下の通りです。

![image-20210430011431619](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210430011431619.png)

---

## iwconfig コマンド

無線 LAN インタフェースに関連した設定のためには、iwconfig というコマンドが用意されています。

```
iwconfig インタフェース名 操作内容
```

「操作内容」としては、以下のようなものが指定できます。

![image-20210430011807378](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210430011807378.png)

実例を示します。
![image-20210430012149795](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210430012149795.png)

## iw コマンド

無線関連の情報取得・設定を行うiwconfigを置き換えるコマンドとしてiwコマンドがあります。
ifconfigコマンドとiwconfigコマンドの関係と同じように、インターフェイスに関するip設定などはipコマンドで行います。
なお、無線LAN関係は近年大きく変化していますが、その変化の一つに暗号化分野があります。現在ではあまり安全と言えなくなったWEPに替わってWPAを使う場合は、WPAのクライアントプログラムである「wpa_supplicant」などが必要になります。（※詳細は試験範囲外のため省略します。）

主なオブジェクト、コマンドは以下の通りです。
![image-20210430012339220](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210430012339220.png)

## iwlist コマンド

iwlistとは、「Wireless tools for Linux」（wireless-tools）に搭載されている、無線LANインターフェースをスキャン／情報収集するためのコマンドです。
端末の周囲で稼働しているアクセスポイントのESSID*を調べたいときや、現在接続しているアクセスポイントの接続レートを確認したいときなどに利用できます。

```
iwlist [インターフェース名] パラメーター [ESSID] 
```

Linuxでは無線LANインターフェース（のデバイス）名は「wlan0」「wlan1」のように「wlan」から始まるのが一般的です。(※有線LANは「eth0」「eth1」）「ifconfig」コマンドや「cat /proc/net/wireless」などで「/proc/net/wireless」の内容を出力すれば、端末周囲にあるインターフェース名を調べることができます。

### iwlistコマンドで使用可能なアクセスポイントを表示する

```
iwlist インタフェース scan[ning]
例)
iwlist wlan0 scan
iwlist wlan0 scanning
```



---

## ifconfig コマンド

ネットワークインタフェースに関する操作を行うコマンドとして ifconfig があります。

```
ifconfig インタフェース名 操作内容
```

「操作内容」としては、以下のようなものが指定できます。
![image-20210430120301506](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210430120301506.png)

