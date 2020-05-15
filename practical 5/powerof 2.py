# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:17:03 2020

@author: 梦之起点
"""
l=[]
num= input('please input a positive integer:')
num=eval(num)
#change the str to int

result= str(num) + '='
while num> 0 :
    l.append(num%2)
    num= int(num/2)  
# cahnge the num into binary system and store the number in a lise

for i in range(0,len(l)):
    if l[i] == 1:
        result += '2**'+ str(i) + '+'
#output the result 
        
result=result[:-1]
#delete the '+' in the end

print(result)
