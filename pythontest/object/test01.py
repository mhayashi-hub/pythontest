
print(100 *5 + 40 *10)
var = 1 + 1
print(var)
print(1+4)
print("python test : ",var)
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