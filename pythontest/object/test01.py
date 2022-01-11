# pythonのコメントは#以降。
# 字下げ、スペースを厳密にチェックしてプログラムの構造判定に使うので書式チェッカのエラーに注意。
print(100 *5 + 40 *10)
var = 1 + 1
print(var)
print(1+4)
print("python test : ",var)
# listは不定長のデータをまとめて格納する形式、要素のデータを書き換えることが可能。
# 大量のデータを扱う場合には負荷やコストが高いので、データが固定の場合はtupleで生成して扱うのが良い。
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
# for分はリストオブジェクトから要素を取り出す処理を要素数分だけループできる。
for i in checkl:
    print(i)
# すでにリストから要素を取り出しているので、リスト要素指定はいらない。
# 変数に要素そのものが入るので、ここでcheckl[i]などとすると取り出した要素をindexとして使って再度リスト内の要素を探すことになる。

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
dicl = {1:'apple', 2:'orange', 3:'banana'}
print(dicl)
print(dicl[1])
a,b,_ = dicl
print(a)
print(_)
a,b = b,a
print(b,a)
print(a,b)
# zip()メソッドではコレクションを複数まとめて取り扱える。コレクションの種類は混在してよい。
# ただしdictionaryではkeyとvalueのどちらを使うかを明確に意識することに注意。
# zipで複数のコレクションをまとめられるが、全部の要素を個別の変数にfor文などで取り出すことができる。
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
akey, bkey = dicl
print(akey)
print(bkey)
avalue, bvalue = dicl.values()
print(avalue, bvalue)

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

import calendar
calendar.prmonth(2022,2)
print(1,2,"A","漢字")

def countup():
    c1 = 1
    c1 += 1
    return c1
print(countup())

flag1 = "false"
if flag1 == "true":
    figure=input("文字列の入力をしてください ")
    print("入力文字列 ", figure, " を出力します")
elif flag1 == "false":
    print("プログラムを完了します")
    print(1>2)
else:
    print("プログラムを終了します")