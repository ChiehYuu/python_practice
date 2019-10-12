#This code is just for learning 

#Lesson1 Variables Testing

#基礎代數－數值
price_1 = 80                                                                        #數值變數(整數)
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

#打印特殊字元測試
print("\'","\"","\\","\n","\t")                                                     #常用打印特殊字元(單引號，雙引號，斜線，換行，Tab)

#布林資料測試
flag = bool                                                                         #布林資料型態(True or False)用於假設判斷
flag = True

#假設代數
alpha = 140                                                                         #整數，三位字元
bravo = 253.42                                                                      #浮點數，六位字元，兩位小數，一位小數點，三位整數
charlie = "hello world"                                                             #字串，十一位字元，一位空白格

#打印測試

#格式化輸出測試一：整數不完全輸出
print("%2s_顯示為兩位字元" % alpha )                                                
print("%5s_顯示為五位字元" % alpha )

#格式化輸出測試二：整數輸出小數位
print("%4.1s_顯示為四位字元，其中一位為小數，測試整數" % alpha)                     
print("%4.2s_顯示為四位字元，其中兩位為小數，測試整數" % alpha)

#格式化輸出測試三：浮點數不完全輸出
print("%4.1f_顯示為四位字元，其中一位為小數，測試浮點數" % bravo)                   

#格式化輸出測試四：浮點數下探實際值以下輸出
print("%7.4f_顯示為七位字元，其中四位為小數且兩位小數為下探值" % bravo)             

#格式化輸出測試五：浮點數上探實際值以上輸出
print("%9.1f_顯示為九位字元，其中一位為小數，整數位有三位上探值" % bravo)           
print("%9.2f_顯示為九位字元，其中兩位為小數，整數位有兩位上探值" % bravo)
print("%9.3f_顯示為九位字元，其中三位為小數，整數位有一位上探值" % bravo)
