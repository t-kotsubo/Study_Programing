

## データの追加挿入(INSERT)と更新(UPDATE)に使用するにメソッド
| メソッド名 | 機能 |
| ------------------ | ------------------------------------------ |
| save()             | 追加または更新                             |
| create()      | オブジェクトの作成と保存を一つの処理で行う |
| add()              | ManyToManyFieldのデータ追加                |
| update()           | 一括更新                                   |
| get_or_create()    | データを取得、なければ追加                 |
| update_or_create() | データを更新、なければ追加                 |
| bulk_create()      | 一括追加                                   |

## JSONに変換して戻す


    return JsonResponse(ret)

![image-20191114163239531](C:\Users\Takayuki.Kotsubo\AppData\Roaming\Typora\typora-user-images\image-20191114163239531.png)

