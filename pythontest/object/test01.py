# pythonのコメントは#以降。
# 字下げ、スペースを厳密にチェックしてプログラムの構造判定に使うので書式チェッカのエラーに注意。
# pythonの中で書いてる人間が勝手に名前を付けられるものは全部オブジェクトとして定義されている。
# 予約語や処理キーワードは変更できないのでオブジェクトではない、と判断してよい。
print('print and strings method test:')
print('test1')
print("test2")
print('test2"a')
print("test3'b'")
# クォートの文字として"も'も使えるが、一番外側のクォート文字のみが文字列指定のためのものとして認識される。
# 外側のクォート文字と同じ文字さえ使わなければ、内部の文字列で別のクォート文字を使える。
# そのためにクォート文字を二種類定義して識別して使えるようにしているらしい。
print('''test aaa
bbb\n\tccc''')
# トリプルクォートで指定すると改行文字をそのまま入力もできるしエスケープシーケンス付きで記述もできる。
# docstringはdefで定義する定義関数のヘルプ情報として、help()メソッドに関数を渡すと表示できるとのこと。
# defの行の後からトリプルクォートで囲った文字列を実際の関数実装の前に書くだけだが、できる限り書いておいた方が後で楽になる。
def add(a,b):
    '''
    add(a,b)
      aとbを加算した値を返す関数
    :param a:int 加算対象
    :param b:int 加算対象
    :return:int aとbの加算結果
    '''
    return a + b
help(add)
print('raw strings print test:')
# 生(raw)の文字列として扱いたい場合は文字列のクォートの前にrを付ける。
# 文字列処理によってエスケープシーケンスなどに処理される\文字列を特に処理せずそのままprintで使うのに必須。
# これをつけないと\\などのエスケープシーケンスを考慮した文字の変更が必要になる。(rを付けるとあらかじめ処理してくれる。)
raw_str = r'C:\Users\deepinsider\Documents\work\data.txt'
print(raw_str)
# raw_str # この処理系では単純な評価の結果は標準出力に出てこない、のでこの行は特に機能しない。
print('formatted strings print test:')
# python 3.6以降で利用可能。
# {}でくくった中に変数を指定することで、{}に指定した書式に合わせて表示してくれる。
# :の後にformat指定で>3などで文字列の幅指定も可能。end='' なども使えるっぽい。
x = 1
y = 100
result = f'{x} + {y} = {x + y}'
# フォーマット文字列指定内で演算するとその結果を変数にいれなくともそのまま出力できる。便利そう。
# fを前置するのではなくformat()メソッドを呼ぶことで置換箇所{}にformatメソッドで指定した内容を突っ込める。
print(result)
result2 = 'x + 2*y = {}'.format(x + 2 * y)
print(result2)
# {}を対象数分だけ指定して対応する数だけformatメソッドで指定すると、前から割り当てて表示してくれる。
result3 = '{} * {} = {}'.format(x,y,x * y)
print(result3)
# {}内に0から始まる引数番号を記入してラベル付けすることも可能。
result4 = '{0} / {1} = {2}'.format(x,y, x / y)
print(result4)
# {}内に適当なキーワードを名称として付けると、そのキーワード=変数として指定可能。formatメソッド内はキーワード=変数で指定できる。
# キーワードとの明確な対応を指定するので指定順は並んでいなくてもよい。
result5 = '{x} + {y} = {add_value}'.format(add_value = x + y,x=x,y=y)
print(result5)
# 置換するフィールド内の右詰めなどの書式設定も可能。
# 例 :を付けた後で>3,end=''(最小文字幅3文字、右寄せ、endで指定した文字で文字埋め)
print(f'{x:0=+8} + {y:<8} = {x + y:$^8}' %{x:1,y:100})

# cのprintf形式に類似した出力書式指定も可能。その場合、フォーマットの''などのあとに%を指定する必要がある。
# cの指定キーワードと少し違う扱いがある場合があるので、その詳細は使用時に確認すること。
# 指定要素の区切りは%をつけるまでは空白、そのあとの要素わたしは(A,B)つまりtuple形式で複数要素を渡す。
print('%5d' % 556)
print('%-6d %s' % (556,'AAA'))
# 指定要素には辞書形式も使える。この場合はフォーマット指定部にラベル名を付け、要素の位置指定側を%(ラベル名)て指定する。
print('%(x)+.2e + %(y)+.2f : %(z)08.2f' % {'x':1.1,'y':-2.2,'z':-1.1})

print('bool method test:')
print(bool('0'))
print(bool('1'))
print(bool(1))
print(bool(0))
print(bool('false'))
print(bool('null'))
testvalue = ''
print(bool(testvalue))

print('int and operator test:')
print(100 *5 + 40 *10)
var = 1 + 1
print(var)
print(1+4)
print("python test : ",var)
# listは不定長のデータをまとめて格納する形式、要素のデータを書き換えることが可能。
# 大量のデータを扱う場合には負荷やコストが高いので、データが固定の場合はtupleで生成して扱うのが良い。
print('list test:')
checkl = [1,2,4,5]
print(checkl)
print(checkl[1])
checkl[3] = 4
print(checkl)
# listは要素の追加、挿入が可能、index, 値の形式でinsert()で挿入、追加は規定済みのindex範囲より大きな値を指定。
# len()で要素数をカウントできる。
checkl.insert(2,3)
print(checkl)
checkl.insert(8,10)
print(checkl)
# listの要素削除はdel リストオブジェクト[index]で行う。削除した要素はindexが詰められて整列されなおす。
del checkl[0]
print(checkl)
print(checkl[0])
# for文はリストオブジェクトから要素を取り出す処理を要素数分だけループできる。
print('for extraction from list test:')
for i in checkl:
    print(i)
# すでにリストから要素を取り出しているので、リスト要素指定はいらない。
# 変数に要素そのものが入るので、ここでcheckl[i]などとすると取り出した要素をindexとして使って再度リスト内の要素を探すことになる。
# for文にrange()メソッドを組み合わせると、任意の繰り返し回数の処理ができる。
countj = 0
print('loop test:', countj)
for j in range(5):
    countj += 1
    print(countj)
print('loop test: end')
print('collection test:')
testfig = 'AABBDC'
print(testfig[2],testfig[4])

# dictionaryはkey:valueのペアで作成したリストになる。dictionaryは{}でくくり、key:valueとして要素を指定する。
# 要素の取り出しはkeyを指定して取り出す。登録済みのkey以外はつかえない。(連想配列的？)
# dictionaryへの追加は dictionary名[key]=valueの形式で追加できる。
# 要素の削除はdel dictionary名[key]で行う。listと似た形式になっている？
# -> コレクションというフレームワークでdel, insert()やlen()、要素参照の[]での指定、inや==,!=の演算子での判定、
#    for文による要素取り出しループが実装されている。文字列も同様に要素参照の[]で何文字目を取り出すか指定できる。
#   -> 順番に並べているlistやtuple(index numberで指定してアクセス可能)にはシーケンスという概念が付随して定義されている。
#      シーケンスオブジェクトはオブジェクト全体の大小比較(<,<=,>,>=)が可能。
#      ただし比較するのは全体ではなく要素個別に比較して最後の要素までスイープして比較し最終的な値での大小を返す。
# コレクションはアンパックできる。アンパックとは要素をコレクションから個別の変数として一括指定で取り出すこと。
# 文字列もコレクションなのでアンパックで一文字ずつに分解できる。
# アンパックは取り出した要素を入れる変数名を,区切りで左辺に並べて記載し、=でつないだ右辺にコレクションを書く。
# アンパック時は通常要素すべてを格納する変数が必要だが、_(アンダースコア)に不要な要素を突っ込んでやることが可能。
# python3から*変数名で、取り出したい要素より後の要素をリストにまとめて*を追加した変数に格納することが可能になる。
# また、アンパック時の変数の並びを左辺に、右辺に変数を並び替えて代入することで、変数と値の入れ替え、スワッピング代入が可能。
print('dictionary test:')
dicl = {1:'apple', 2:'orange', 3:'banana'}
print(dicl)
print(dicl[1])
a,b,_ = dicl
print(a)
print(_)
# スワッピング代入　要素の並びを変更するのではなくaの値をbに、bの値をaに入れ替える。
# 他の言語のように変数の内容を一度退避して再度変数に代入することなく一括で変数の内容を入れ替えられる。
print('swapping variable insertion test:')
a,b = b,a
print(b,a)
print(a,b)
# zip()メソッドではコレクションを複数まとめて取り扱える。コレクションの種類は混在してよい。
# ただしdictionaryではkeyとvalueのどちらを使うかを明確に意識することに注意。
# zipで複数のコレクションをまとめられるが、全部の要素を個別の変数にfor文などで取り出すことができる。
print('zip method test:')
for x,y in zip(checkl, testfig):
    print(x,y)

# print(dicl['apple'])
del dicl[2]
print(dicl)
# dictionary内にキーが登録済みかはin演算子で判定可能。
print(1 in dicl)
print(2 in dicl)
# dictionaryのアンパックではkeyしか取り出せない？ -> ただのアンパックではkeyのみ取り出す。
# value取り出しはdictionaryのメソッドvalues()を使う。
print('dictionary un-pack test:')
akey, bkey = dicl
print(akey)
print(bkey)
avalue, bvalue = dicl.values()
print(avalue, bvalue)

print('tuple test:')
checkt = ('平成','元年')
print(checkt)
print(checkt[0])
print(checkt[1])
# checkt[0] = '令和'
# tupleは要素の変更不可、tuple自体を新しい値を使って再生成する必要あり。
# tupleは要素を固定的に扱えるデータ、大量のデータを作って処理するのに向いているが変更不可。
# 変数などのオブジェクトをまとめて入れられるが、入れた時点でのデータは変更できない、
# 変更するならtupleを作り直す必要がある
era, year = checkt
print(era)
print(year)

checkt = ('令和','元年')
print(checkt)
engscore = 10
japscore = 50
matscore = 60
checktl = (engscore, japscore, matscore)
print(checktl)
engscore = 80
print(engscore)
print(checktl)
# import文によってライブラリなどに準備されている関数やオブジェクトなどを参照できる。
print('import module and calender test:')
import calendar
calendar.prmonth(2022,2)
print(1,2,"A","漢字")
# 関数定義はdef 関数名():で定義する。戻り値はreturnで返す。
# 関数内で使わない変数は全部グローバル変数、関数内で定義、宣言したものはローカル変数となる。
# ただしscopeはモジュール内に限定される。
# importはモジュール内に他のモジュールの参照を可能にするための機能。
print('define method test:')
def countup():
    c1 = 1
    c1 += 1
    return c1
print(countup())
print('type method test:')
print(type(countup))

print('lambda test:')
hello = lambda x: print('hello ' + x)
hello('world')
checkcomment = lambda y: print('check value: ' + y)
checkcomment('comment')
result = filter(lambda a: int(a)%2 == 0,'0123456789')
for number in result:
    print(number)

print('list function with function in list test:')
inlista = []
for num in range(19):
    inlista.append(num)
print(inlista)
inlistb = [num for num in range(15)]
print(inlistb)
print([num*3 for num in range(4)])
print([num*num for num in range(13) if num%2 == 0])
for row in [[x * y for x in range(1,10)] for y in range(1,10)]:
    print(row)
print('nested statement and formated printout test:')
result = []
for x in range(1,10):
    z = []
    for y in range(1,10):
       z.append(x*y)
    result.append(z)
for row in result:
    for column in row:
        print(f'{column:>3}', end='')
    print()

print('if statement test:')
flag1 = "false"
if flag1 == "true":
    figure=input("文字列の入力をしてください ")
    print("入力文字列 ", figure, " を出力します")
elif flag1 == "false":
    print("プログラムを完了します")
    print(1>2)
else:
    print("プログラムを終了します")
# if文,for文などは行末に:で認識させる。
# if-elseはペアとして使ってelse ifはなくelifになる。