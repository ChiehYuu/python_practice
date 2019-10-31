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

#布琳關係式                                                                        #資料輸入後儲存在變數內即為布林資料型態，以0或1表示，不會再另外儲存方程式
fun_a = 16+9==15+7
fun_b = 3+8==5+6
fun_c = 16+9!=15+7
fun_d = 3+8!=5+6
fun_e = 16+9>15+7
fun_f = 3+8>5+6
fun_g = 16+9<15+7
fun_h = 3+8<5+6
fun_i = 16+9>=15+7
fun_j = 3+8>=5+6
fun_k = 16+9<=15+7
fun_l = 3+8<=5+6

#輸出測試                                                                          #變數本身即為布林資料，故不會顯示方程式
print("此方程式的格式為：",type(fun_a),"方程式為：",str(fun_a),"顯示為：",fun_a,sep="_",end="\n")
print("此方程式的格式為：",type(fun_b),"方程式為：",str(fun_b),"顯示為：",fun_b,sep="_",end="\n")
print("此方程式的格式為：",type(fun_c),"方程式為：",str(fun_c),"顯示為：",fun_c,sep="_",end="\n")
print("此方程式的格式為：",type(fun_d),"方程式為：",str(fun_d),"顯示為：",fun_d,sep="_",end="\n")
print("此方程式的格式為：",type(fun_e),"方程式為：",str(fun_e),"顯示為：",fun_e,sep="_",end="\n")
print("此方程式的格式為：",type(fun_f),"方程式為：",str(fun_f),"顯示為：",fun_f,sep="_",end="\n")
print("此方程式的格式為：",type(fun_g),"方程式為：",str(fun_g),"顯示為：",fun_g,sep="_",end="\n")
print("此方程式的格式為：",type(fun_h),"方程式為：",str(fun_h),"顯示為：",fun_h,sep="_",end="\n")
print("此方程式的格式為：",type(fun_i),"方程式為：",str(fun_i),"顯示為：",fun_i,sep="_",end="\n")
print("此方程式的格式為：",type(fun_j),"方程式為：",str(fun_j),"顯示為：",fun_j,sep="_",end="\n")
print("此方程式的格式為：",type(fun_k),"方程式為：",str(fun_k),"顯示為：",fun_k,sep="_",end="\n")
print("此方程式的格式為：",type(fun_l),"方程式為：",str(fun_l),"顯示為：",fun_l,sep="_",end="\n")

#邏輯運算子                                                                         #測試結果：TFTFFFFFTFTFTTTT
fun_A = 3>5
fun_B = 5>3
fun_C = 6>9
fun_D = 9>6

an4_1 = not(fun_A)
an4_2 = not(fun_B)
an4_3 = not(fun_C)
an4_4 = not(fun_D)
an4_5 = (fun_A)and(fun_B)
an4_6 = (fun_A)and(fun_C)
an4_7 = (fun_A)and(fun_D)
an4_8 = (fun_B)and(fun_C)
an4_9 = (fun_B)and(fun_D)
an4_10 = (fun_C)and(fun_D)
an4_11 = (fun_A)or(fun_B)
an4_12 = (fun_A)or(fun_C)
an4_13 = (fun_A)or(fun_D)
an4_14 = (fun_B)or(fun_C)
an4_15 = (fun_B)or(fun_D)
an4_16 = (fun_C)or(fun_D)


print(an4_1,an4_2,an4_3,an4_4,an4_5,an4_6,an4_7,an4_8,an4_9,an4_10,an4_11,an4_12,an4_13,an4_14,an4_15,an4_16,sep="||",end="\n\n")

#單向判斷式

score_1 = float(input("請輸入一個數字："))

if(score_1>=60):
    print("及格",end = "\n\n")

#雙向判斷式

if(score_1>=60):
    print("及格",end = "\n\n")
else:
    print("不及格",end = "\n\n")

#多向判斷式

if(score_1>60):
    print("及格",end="\n\n")
elif(score_1==60):
    print("剛好及格",end="\n\n")
else:
    print("不及格",end="\n\n")

#練習二：巢狀迴圈－百貨公司周年慶滿額打折

money_1 = int(input("請輸入您這次的花費金額："))

if(money_1>=10000):
    if(money_1>=100000):
        money_1 = money_1*0.8
    elif(money_1>=50000):
        money_1 = money_1*0.85
    elif(money_1>=30000):
        money_1 = money_1*0.9
    else:
        money_1 = money_1*0.95
    print("您這次的消費金額為：",money_1,sep="",end="\n\n")
else:
    print("不好意思你這次消費金額不足，未能打折，金額為：",money_1,sep="",end="\n\n")


#串列測試：串列中可以包含串列可做為矩陣中之矩陣看待，作為一2*2矩陣形式呼喚
grade_1 = ["王小明",89,77,90],["孫小美",96,80,88],["李大明",76,93,70]
print(grade_1[0])
print(grade_1[1][0])
print(grade_1[2][1])
print(type(grade_1[0][1]))

#3*3測試&字典混和測試
grade_3 = [["水果",{"蘋果":15,"香蕉":20,"鳳梨":45}],["鞋子",{"NIKE":3500,"adidas":4500,"puma":2000}],["飲料",{"紅茶":15,"綠茶":15,"奶茶":25}]]
print(grade_3[0][0])
print(grade_3[0][1]["蘋果"])
print(grade_3[1][0])
print(grade_3[1][1]["adidas"])
print(grade_3[2][0])
print(grade_3[2][1]["奶茶"])

#range：等差級數，自動生成，(首項，末項，公差)，存入代數中可作為一行串列

grade_2 = range(2,9)
print(grade_2)
print(list(grade_2))
print(list(grade_2)[2])
print(range(2,9),end="\n\n")

#for loop
list_1 = range(1,31)
for number in list_1:
    print("座號為：%-3d" % number,sep="\n",end= "\n\n")

#練習三：九九乘法表

for i in range(1,10):
    for j in range(1,10):
        print("%2d x %2d = %-3d" %  (i,j,i*j),sep="",end="")
    print()                                                                 #內層for loop 完成後，換行，再繼續執行loop

#練習四：樓層命名

stage_1 = int(input("請輸入此樓層數："))
for i in range(1,stage_1):
    if (i == 4):
        continue                                                            #continue為跳過此輪迴圈繼續執行
    elif(i == 26):
        break                                                               #break為跳出迴圈繼續執行
    else:
        print("本層樓為：%3d 樓" % i,end="\n")

#練習五：找質數

prime_num = int(input("請輸入一個大於1的數字："))
print()
if (prime_num == 2):
    print("2為質數!")
else:
    for i in range(2,prime_num):
        if (prime_num % i == 0):
            print("%5d 不是質數!" % prime_num)
            break
    else:
        print("%5d為一個質數!" % prime_num)
print()

for i in range(2,prime_num):
    if (prime_num == 2):
            print("在5%d內的質數有以下這些：\n2" % prime_num)
    else:
            for j in range(2,i):
                if(i % j == 0):
                    break
            else:
                print("%5d" % i)
print()
    
#while loop
total = n =0
while (n<10):
    n += 1
    total += n
print(total)
print()

#list測試
list_test_1 = [1,2,3,4,5,6,7,8]
list_extend_1 = [9,10,11]

list_test_2 = list_test_1*2
print(list_test_2)

print(list_test_1[3:6])
print(list_test_1[1:8:2])

del list_test_2[0:8]                                                        #刪除第a~b項
print(list_test_2)

del list_test_2[0:8:2]                                                      #刪除第a~b項中間隔c的項次
print(list_test_2)

print(len(list_test_2))                                                     #串列目前的數目
print(min(list_test_1))                                                     #串列中的最小值
print(max(list_test_1))                                                     #串列中的最大值

list_test_1.append(0)                                                       #在串列最後加上括號內的值
print(list_test_1)

list_test_1.extend(list_extend_1)                                           #在串列最後加上括號內的串列
print(list_test_1)

list_test_1.insert(0,0)                                                     #在第a項前加上b值
print(list_test_1)

list_pop_1 = list_test_1.pop()                                              #將串列最後一項取出，可另存於成其他代數形式
print(list_pop_1)
print(list_test_1)

list_test_1.remove(7)                                                       #將串列中的第n-1巷刪除
print(list_test_1)

list_test_1.reverse()                                                       #將串列倒轉
print(list_test_1)

list_test_1.sort()                                                          #將串列由小至大排列
print(list_test_1)

print()

#append/insert
list_2 = [0,1,2,3,4,5,6,7,8,9]
list_2.append(10)

print(list_2[10])
list_2.insert(3,11)
print(list_2[3])

#dict

dict_1 = {"香蕉":20,"蘋果":45,"葡萄":60}
print(dict_1["香蕉"])
print(dict_1["葡萄"])
dict_1["香蕉"] = 80
print(dict_1["香蕉"])
print(len(dict_1))

dictest_1 = {"joe":30,"mary":45,"geroge":50}
print(len(dictest_1))
dictest_2 = dictest_1.copy()
print(dictest_2)
dictest_2.clear()
print(dictest_2)
print(dictest_1.get("joe"))
print("joe" in dictest_1)
print("paul" in dictest_1)

dictest_3 = list(dictest_1.items())
print(dictest_3)
print(dictest_1.items())
print(type(dictest_3))
print(type(dictest_1.items()))

print()

dictest_4 = list(dictest_1.keys())
print(dictest_4)
print(dictest_1.keys())
print(type(dictest_4))
print(type(dictest_1.keys()))

dictest_5 = list(dictest_1.values())
print(dictest_5)
print(dictest_1.values())
print(type(dictest_5))
print(type(dictest_1.values()))
print()
for i in range(len(dictest_4)):
    print("%-10s的座號為%3d" % (dictest_4[i],dictest_5[i]))

print()
print(dictest_1.setdefault("joe"))
print()


dictest_6 = dictest_1.items()
for i,j in dictest_6:
    print("%-10s的座號為%3d" % (i,j))
print()



#key value items get
list_keys_1 = list(dict_1.keys())
list_values_1 = list(dict_1.values())
for i in range (len(list_keys_1)):
    print("%5s 的價格是%5d" % (list_keys_1[i],list_values_1[i]))
print()

print(dict_1.get("香蕉"))
print(dict_1.get("鳳梨",100))




