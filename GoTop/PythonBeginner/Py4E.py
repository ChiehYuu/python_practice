# -*- coding: utf-8 -*-
import re 

name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_335075.txt"
handle = open(name)
num_list = list()
for line in handle:
    line = line.rstrip().split()
    num = re.findall('([0-9]+)',str(line))
    if len(num)<1 :
        continue
    else:
        for i in num:
            num_list.append(float(i))
            
print(num_list)      
print('Sum:',sum(num_list))