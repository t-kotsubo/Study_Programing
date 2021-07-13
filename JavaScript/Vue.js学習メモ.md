## Vueインスタンスの生成

全ての Vue アプリケーション は、`Vue` 関数で新しい **Vue インスタンス**を作成することによって起動されます。

```
var vm = new Vue({
//　オプション
})
```

※慣例として`vm`（ViewModelの略）をVueインスタンスの変数名としてよく使います。

### 代表的なオプション

| オプション | 機能                                            |
| ---------- | ----------------------------------------------- |
| data       | Vueインスタンスをマウントするセレクタを登録する |
| data       | Vueで管理するデータを登録する                   |
| methods    | dataを操作する関数を登録する※                   |

**※methodsで登録させた関数は`v-on` ディレクティブで呼び出すことが可能**









## ディレクティブ



### 基本的なオプションの構成

```
// 基本的なオプション構成（使用するデータやメソッド）
var app = new Vue({

  // (1) mountする要素(アプリケーションを紐付ける要素のセレクタ)
  el: '#app',
  
  // (2) アプリケーションで使用するデータ
  data: {
    message: 'Vue.js'
  },
  
  // (3) 算出プロパティ
  computed: {
    computedMessage: function() {
      return this.message + '!'
    }
  },
  
  // (4) ライフサイクルフック
  created: {
    // 行ないたい処理
  },
  
  // (5) アプリケーションで使用するメソッド
  methods: {
    myMethod: function() {
      // 行いたい処理
    }
  }

})
```

http://jsstudy.hatenablog.com/entry/What-is-el-in-Vuejs



