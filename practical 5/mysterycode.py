# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:17:10 2020

@author: 梦之起点
"""


# Answer: out put a random prime number from 1 to 100


from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
    n = randint(1,100)
    #input a random integer between 1 to 99
    u = ceil(n**(0.5))
        for i in range(2,u+1):
        if n%i == 0:
            p=False
#if n can be divided by a number from 2 to u, n is not a prime number. 
#So that p comes to false and generate a random integer again until n is a prime number.            
    
print(n)