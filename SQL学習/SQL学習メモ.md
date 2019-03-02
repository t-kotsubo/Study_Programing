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

