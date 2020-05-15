# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:05:44 2020

@author: 梦之起点
"""
num=input('please input a positive integer:')
num=eval(num)
#change the str into int

result=''

while num >=1:
  result += str(num) + '-'
  
  if num==1:
      break  
#stop the project to avoid infinite loop
      
  if num %2 == 0:
    num /= 2
    
  else:
    num= num*3+1
    
result=result[:-1]
#delete the last '-'

print(result)
#output the program access

