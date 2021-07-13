## TypeScriptの型

変数定義や仮引数を設定する時に型を指定する。

### 型の種類

```

boolean

number

string

any

void

Array

Object

undefined

nullable

```



### boolean、number、string

変数定義の際に変数名の後に「：」（コロン）を付けて型を指定する

```
let b: boolean = true;
let n: number = 1;
let s: string = "A";
```

代入する方が決まり切っている場合は型の指定を省略可能（型推論されるため）

```
let s: string = "A";
↓
let s = "A"

let b: boolean = true;
↓
let b = true

でもOK!
```

### void

#### 戻り値なしの場合の関数定義

```
function func(a, b) : void {
	処理
}
```

#### 戻り値ありの関数定義

```
function func(a:number, b:number) : number {
	ruturn num;
}
```

### any　(あまり使わないが、型は何でも良いという場合)…基本的に使わない

```
let a: any = 1 / "A"
```

### Array (配列)

```
let arrayS: string[] =["A", "B", "C"];
let arrayN: number[] =[1, 2, 3];
```

### Object  ：interfaceを使って定義する

```
interface Foo {
	n1: number,
	n2: number,
}
let foo: Foo = {n1:10, n2:20};
```

### undefined ：（値が入ってくるかわからない場合は「？」を付けるとエラーにならない「？」がないと値が入ってこないと「undefined」となる
```
interface Foo {
	n1: number,
	n2?: number,
}
let foo:Foo = {n1:10, n2:20};
```

### nullable：undefined （値が必ず入ってくるがnullで入ってくる可能性がある場合は「 型   |　 null」（型  or null)と表示するとエラーにならない。

```
interface Foo {
	n1: number,
	n2: number | null,
}

let foo：Foo = {n1:10, n2:null};
※この場合n2:nullであればエラーにならないが、n2の値自体のキーがないとエラーになる
```

#### ポイント：「?」はキーがなくてもOK、「| null」はキーがないとエラー
