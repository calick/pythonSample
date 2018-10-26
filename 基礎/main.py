# coding: UTF-8

### 文字列操作 ###
# 大文字に変換
print("Hello".upper())
# 小文字に変換
print("Hello".lower())
# 文字列の置き換え
print("Hello".replace("l","1"))

### 繰り返し ###
# 変数に代入した回数分表示
num = 3
for i in range(num):
    print("count : " + str(i))

# 10以上13未満の数値を表示
for i in range(10,13):
    print("count : " + str(i))

# 0から3の倍数を表示
for i in range(0,10,3):
    print("count : " + str(i))

# 負の数を指定することもできる
for i in range(10,0,-3):
    print("count : " + str(i))

# リストに入った文字列の分だけ表示
list_string = ["AAA","BBB","CCC"]
for s in list_string:
    print("string : " + s)

# 逆順にする場合はreversed()関数を利用する
for s in reversed(list_string):
    print("string : " + s)

### 複数リスト ###
# zip関数では複数の要素を順番に取得可能
list_string = ["AAA","BBB","CCC"]
list_num1 = [1,2,3]
for s,n in zip(list_string,list_num1):
    print(s,n)

list_num2 = [4,5,6]
for s,n1,n2 in zip(list_string,list_num1,list_num2):
    print(s,n1,n2)

### 演算子 ###
# 演算の優先順位はParentheses(カッコ)、Exponents(累乗)、Multiplication(掛け算)、Division(割り算)、Addition(足し算)、Subtraction(引き算)
# 足し算
print("1+1="+str(1+1))
# 引き算
print("2-1="+str(2-1))
# 掛け算
print("2*3="+str(2*3))
# 割り算
print("4/2="+str(4/2))
# 累乗
print("2**3="+str(2**3))
# 割り算の余り
print("5%2="+str(5%2))
# 整数の割り算切捨て
print("5//2="+str(5//2))

### 関数 ###
## 関数は１つのことをすべきである。そのことを徹底すべきだ。
## たったそれだけのことに特化すべきだ。
# 必須引数
def greeting(x):
    print("Hello "+ x)
result=greeting("TOM")
print("返り値がない場合はNONEが返る")
print(result)
# オプション引数
def greeting(x="TARO"):
    print("Hello "+ x)
result=greeting("TOM")
result=greeting()

### 組み込み関数 ###
# 文字列の長さをカウントする
str_count=len("abcdefg")
print(str_count)
# 数値を文字列に変換する
str_100=str(100)
print(str_100)
# 文字列を数値に変換する
int_100=int("100")
print(int_100+int_100)
# 浮動小数点オブジェクトを返す
float_100=float(100)
print(float_100)

### 変数のスコープ ###
# 関数からグローバル変数への書き込み
x=10
def f():
    global x
    x+=1
    print(x)
f()
f()

### 例外処理 ###
try:
    print(2/0)
except ZeroDivisionError:
    print("0で割れない")
try:
    print(2/"a")
except TypeError:
    print("Invalid value.")
# exceptは並べて記載することも可能
try:
    print(2/"a")
except(ZeroDivisionError,NameError,TypeError):
    print("Invalid value.")

### ドキュメンテーション文字列 ###
def add(x,y):
    """
    加算
    :param x:int.
    :param y:int.
    :return: int sum of x and y.
    """
    return x+y
print(add(1,2))

### コンテナ ###
# リスト(好きな順番でオブジェクトを保存しておけるコンテナ)
# 変更可能（ミュータブル）
color=["red","bule","yellow"]
print(color)
print(color[1])
color.append("black")
print(color)
color.pop()
print(color)
try:
    color[4]
except(IndexError):
    print("IndexError")
try:
    number=[]
    number.pop()
except(IndexError):
    print("IndexError")
print("yellow" in color)
print("white" in color)

str_color="brown"
if str_color in color:
    print(str_color + " is exist.")
else:
    print(str_color + " is not exist.")

# タプル(好きな順番でオブジェクトを保存しておけるコンテナ)
# 変更不可能（イミュータブル）
# タプルは一度作成したら新しい要素を追加できない＆要素の変更もできないので都市の座標などのように不変(変わって欲しくない)値を扱うのに利用する
numbers=("one","two","three")
print(numbers)
# 要素が１つだけの場合、要素の最後にカンマを付ける。カンマがないと、Pythonは数値演算の優先順位を決めるためのカッコだと認識してしまう。
number=("one",)
print(number)
# 既存のタプルが変更されているのではなく、新しいタプルが生成されていて、オブジェクト id が変わるため以下の書き方での追記は可能
number+=("two",)
print(number)
try:
    number[1]="zero"
except(TypeError):
    print("TypeError")

# 要素の中身を確認する
numbers=("one","two","three")
print("two" in numbers)
print("four" in numbers)

# 辞書
# ２つのオブジェクトを関連付けて保持するコンテナで、片方のオブジェクトを格納時や取得時のキーとして扱い、もう片方のオブジェクトをバリューとしてキーにマッピングして保持する。
# keyをstring
numbers={
    "1":"one",
    "2":"two",
    "3":"three"
}
print(numbers)
print(numbers["2"])
x=3
try:
    print(numbers[x])
except(KeyError):
    print("KeyError")
x="3"
print(numbers[x])
# keyをint
numbers={
    1:"one",
    2:"two",
    3:"three"
}
x=1
print(numbers[x])
# 要素の中身を確認する
print(1 in numbers)
print(4 in numbers)
# 要素の追加
numbers[4]="four"
print(4 in numbers)
# 要素の削除
del numbers[1]
print(numbers)





