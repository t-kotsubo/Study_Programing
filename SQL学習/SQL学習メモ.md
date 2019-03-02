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