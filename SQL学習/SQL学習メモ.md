# WHERE




特定のデータを取得するためには、「どこの」という意味を持つ「WHERE」というSQLを用います。「SELECT」と「FROM」で「どのテーブルのどのカラムのデータを取得するか」までは決まっていますので、「WHERE」が意味するのは、「どこのレコード（横の列）を取得するか」になります。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507180414621.png)

# WHERE(2)



「どこのレコード（横の列）のデータを取得するか」を指定するためには、左の図のように「＝」を用いて、「〇〇カラムが〇〇であるレコード」といった意味になるように条件を指定します。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507180441584.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1523346082536.png)

## 「食費」のデータを取得しよう



今回は「WHERE category = "食費"」のような条件で、「category」が「食費」であるデータを取得してみましょう。データには「データ型」と呼ばれるルールにより、「食費」のようなテキストはクォーテーションで囲む必要があります。「データ型」については、次の ページで詳しく説明します。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507180591820.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507188992729.png)

# データ型



データベースに保存されているデータには、「データ型」と呼ばれるルールがあります。「データ型」とは、テキストデータや数値データ、さらには日付データといったように「データの種類」を示すものです。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1523346283859.png)

## 日付データを取得しよう



次に「日付が2017-07-01であるデータ」を取得してみましょう。「日付」を示す「purchased_atカラム」には「日付データ」が保存されています。<u>「日付データ」はダブルクォーテーションまたはシングルクォーテーションで囲む必要があるため、忘れないようにしましょう</u>。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1523346364863.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507180835834.png)

# IS NULL・IS NOT NULL

## NULLのデータを取得する



NULLのデータを取得するためには「〜がNULLである」という意味になる、「IS NULL」というSQLを用います。図のように「カラム名 IS NULL」とすることで、「指定したカラムがNULLであるデータ」を取得することが可能です。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507184996434.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1514258312793.png)

## NULLではないデータを取得する場合

一方、「NULLではないデータ」を取得する場合は「〜がNULLでない」という意味になる「IS NOT NULL」を用います。「IS NOT NULL」も「IS NULL」と同様に、「カラム名 IS NOT NULL」のようにして使います。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507185014228.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1514258236699.png)



## NULLに関連するデータを取得するときの注意

「NULLのデータ」や「NULLでないデータ」を取得したい場合、図のように「=」は使うことができません。 

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507185039258.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507185045162.png)

---

# AND・OR演算子

## AND演算子

AND演算子を使うと、WHERE文に複数の条件を指定することができます。「WHERE 条件１ AND 条件２」のようにすることで、条件１と条件２を共に満たすデータを検索することができます。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507185369402.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507185217383.png)

## OR演算子

OR演算子は、AND演算子と同様に、複数の条件を扱います。「WHERE 条件１ OR 条件２」のようにすることで、条件１または条件２のどちらかを満たすデータを検索することができます。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/150718537930.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507185321466.png)

----

# ORDER BY

## ORDER BY

データを並び替えるためには、「〜順に並べる」という意味の「ORDER BY」というSQLを用います。またデータを並び替えるためには、図のように「（基準となる）並べ替えたいカラム名」と「並べ方」を指定する必要があります。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/150727920757.png)

## 昇順と降順

「ORDER BY」の並べ方は、「昇順」か「降順」を指定します。「昇順」は「小さい数から大きい数へ向かう順序」、「降順」は「大きい数から小さい数へ向かう順序」です。SQLでは「昇順」は「ASC」、「降順」は「DESC」と指定します。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1514258212553.png)

## ORDER BY(2)

「ORDER BY」は図のようにSQL文の末尾に記述することで、取得結果を並び替えます。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1507612312690.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1507612200955.png)

## ORDER BY(3)

「ORDER BY」はSQL文の末尾に記述すれば良いため、「WHERE文」と併用することが可能です。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/150728061155.png)

---

# LIMIT

## LIMIT

**「最大で何件取得するか」を指定するためには、「制限する」という意味の「<u>LIMIT</u>」を用います。「LIMIT」は左の図のように「 データの件数」を指定します。**

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/150718588974.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507566372729.png)

## LIMIT(2)

「LIMIT」も「ORDER BY」と同様にSQL文の末尾に記述することで、取得するデータの数を制限します。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1507612343950.png)

## LIMIT(3)

また、「LIMIT」も「ORDER BY」と同様にSQL文の末尾に記述すれば良いため「WHERE文」と併用することが可能です。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/101/1507185907819.png)

# LIKE演算子



「ある文字を含むデータ」を取得したい場合は、「〜のような」という意味を持つ、「LIKE演算子」を用います。図のようにすることで「指定したカラムが〇〇を含む（〇〇のような）レコード」という条件となります。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1546922405228.png)

## ワイルドカード



LIKE演算子を用いる際に覚えておく必要があるのが「ワイルドカード」です。コンピュータの世界で「ワイルドカード」とは、どんな文字列にも一致することを指す記号です。LIKE演算子では「％」をワイルドカードとして扱います。これにより図では「プリン」を含むデータを全て取得しています。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1546922515266.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1546922539358.png)

## 前方一致



ワイルドカードを文字列の前後どちらかにのみ置くことも可能です。図のように「〇〇%」とした場合、「〇〇」以降はどんな文字列にも一致しますので、「〇〇」で始まる文字列を検索することができます。このような検索を「前方一致」と呼びます。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1546922863693.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1546922880829.png)



## 後方一致



また、図のように「%〇〇」とした場合、「〇〇」より前はどんな文字列にも一致しますので「〇〇」で終わる文字列を検索することができます。このような検索を「後方一致」と呼びます。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1546922921935.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1547783117899.png)

# NOT演算子

​	

「〇〇を含まないデータ」や「〇〇に一致しないデータ」のような条件でデータを取得したい場合は「否定」を意味する「NOT演算子」を用います。これまで学習した演算子の前に「NOT」を置くことで、その条件を満たさないデータを取得することが可能です。

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1546923241886.png)

![img](https://d2aj9sy12tbpym.cloudfront.net/progate/shared/images/slide/sql/study/1/1546923717517.png)