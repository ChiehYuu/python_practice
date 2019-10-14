#This code is just for learning 

#Lesson1 Variables Testing

#基礎代數－數值
price_1 = int(80)                                                                   #數值變數(整數)
price_2 = 80.0                                                                      #數值變數(浮點數)
print ( price_1,"\n",price_2,sep="" )

#基礎代數－字串
fruit = "水果"                                                                      #字串變數 
print ( fruit )                                                                     #打印括弧內東西  
print (fruit,"價格等於",price_1)                                                    #雙引號可以直接打印引號內容

#基礎代數－混合指定變數
price_1 = price_2 = 60.0                                                            #變數連續定義(以等號表示相同且意義也相同之變數)
print (price_1,price_2)
price_3,car = 120,"汽車"                                                            #變數練續定義(不同變數以逗號分別)
print (car,"價格為",price_3)

#輸出特殊字元測試
print("\'","\"","\\","\n","\t")                                                     #常用輸出特殊字元(單引號，雙引號，斜線，換行，Tab)

#輸出字元
print(price_1,price_2,sep="&",end="\n\t\n")                                         #連續輸出字元設定：sep設定輸出變數間要出現甚麼，end設定變數輸出完成後要怎麼結束

#布林資料測試
flag = bool                                                                         #布林資料型態(True or False)用於假設判斷
flag = True

#假設代數
alpha = 140                                                                         #整數，三位字元
bravo = 253.42                                                                      #浮點數，六位字元，兩位小數，一位小數點，三位整數
charlie = "hello world"                                                             #字串，十一位字元，一位空白格

#輸出測試

#格式化輸出測試一：整數不完全輸出
print("%2d_顯示為兩位字元" % alpha )                                                #變數中的字元若超過格式則全部輸出     
print("%5d_顯示為五位字元" % alpha )                                                #變數中的字元若少於格式則前方留白

#格式化輸出測試二：整數輸出小數位
print("%4.1d_顯示為四位字元，其中一位為小數，測試整數" % alpha)                     #若為整數，小數位無用
print("%4.2d_顯示為四位字元，其中兩位為小數，測試整數" % alpha)                     

#格式化輸出測試三：浮點數不完全輸出
print("%4.1f_顯示為四位字元，其中一位為小數，測試浮點數" % bravo)                   #若為浮點數，自標註位置起算輸出字元，向下省略，向上則全部輸出                   

#格式化輸出測試四：浮點數下探實際值以下輸出
print("%7.4f_顯示為七位字元，其中四位為小數且兩位小數為下探值" % bravo)             #若為浮點數，以下探值為起點輸出字元數，向上全部輸出

#格式化輸出測試五：浮點數上探實際值以上輸出
print("%9.1f_顯示為九位字元，其中一位為小數，整數位有三位上探值" % bravo)           #若為浮點數，以標註小數位置為起點，向上全部輸出，若格式較多則留白
print("%9.2f_顯示為九位字元，其中兩位為小數，整數位有兩位上探值" % bravo)
print("%9.3f_顯示為九位字元，其中三位為小數，整數位有一位上探值" % bravo)

#格式化輸出測試五：字串輸出
print("%8s_顯示為八位字元，字串顯示" % charlie)                                     #若為字串，小數點後表示輸出幾位前幾位字元，若無則全部輸出
print("%8.1s_顯示為八位字元，字串顯示" % charlie)
print("%8.5s_顯示為八位字元，字串顯示" % charlie)

#變數形式確認                                                                       #type為變數形式確認，可藉由直接宣告處理變數形式      
price_1 = int (90)
print(type(flag),type(charlie),type(price_1),type(12),type(250.3),type("Hello World"),sep="\n",end="\n\n") 
                                                                                    
#練習一：成績單                                                                     #貼齊格線要測試
print("| 姓名   | 座號 | 國文 | 英文 | 數學 |")
print("| %3s | %3d  | %3d  | %3d  | %3d  |" % ("王小明",10,67,88,100))
print("| %3s | %3d  | %3d  | %3d  | %3d  |" % ("李大明",15,73,77,85))
print("| %3s | %3d  | %3d  | %3d  | %3d  |" % ("吳小敏",3,95,90,80))

#計算與資料型態轉換

#假設變數
num_1 = 60
num_2 = 8.752
num_3 = True
num_4 = 1
num_5 = 0
num_6 = 6
num_7 = 0.3
num_8 = -1

#輸出測試
print(num_1 + num_2)                                                                #整數與浮點數計算，顯示浮點數
print(int(num_1 + num_2))                                                           #整數與浮點數計算，強制顯示為整數
print(num_1 + num_3)                                                                #整數與布林資料計算，布林資料True=1，False=0，顯示為整數
print(float(num_1 + num_3))                                                         #整數與布林資料計算，強制顯示為浮點數
print(num_3)                                                                        #布林資料輸出，顯示為True/False
print(num_3 - num_3)                                                                #布林資料計算，顯示為整數
print(bool(num_3-num_3),end = "\n\n")                                               #布林資料計算，強制顯示為布林資料

#布林資料測試                                                                       #除了0以外，其餘皆顯示True，無論正負
print(bool(num_1))
print(bool(num_5))
print(bool(num_6))
print(bool(num_7))
print(bool(num_8),end="\n\n")

#輸入資料                                                                           #輸入後若無限制格式則起始字元格式為字串
number_input_1 = input("請輸入你的第一個數字：")
number_input_2 = input("請輸入你的第二個數字：")
print("你輸入的數字為：",number_input_1," & ",number_input_2,sep = "",end = "\n\n")

#運算測試
cal_1 = float(input("請輸入第一個數字："))
cal_2 = float(input("請輸入第二個數字："))
add_1 = cal_1 + cal_2
sub_1 = cal_1 - cal_2
mul_1 = cal_1 * cal_2
div_1 = cal_1 / cal_2
rem_1 = cal_1 % cal_2
quo_1 = cal_1 // cal_2
exp_1 = cal_1 ** cal_2

print("兩數相加=",add_1,sep="",end="\n")
print("兩數相減=",sub_1,sep="",end="\n")
print("兩數相乘=",mul_1,sep="",end="\n")
print("兩數相除=",div_1,sep="",end="\n")
print("兩數相除，餘數為=",rem_1,sep="",end="\n")
print("兩數相除，商數為=",quo_1,sep="",end="\n")
print("次方數為=",exp_1,sep="",end="\n\n")

#布琳關係式
fun_a = 16+9==15+7
fun_b = 3+8==5+6
print(type(fun_a),fun_a,type(fun_b),fun_b,sep="_&&_",end="\n")




