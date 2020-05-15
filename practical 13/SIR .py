# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:02:15 2020

@author: 梦之起点
"""

import numpy as np 
import matplotlib.pyplot as plt

N=10000#the total number of prople
beta=0.3
gamma=0.05
t=1000# the total time
sus=[9999] 
inf=[1]
rec=[0]
#create the list of the people number in different time
a=[]
b=[]
inp=0
rep=0
#the number of people that been infected or recoverd.

for i in range (0,t):
    a= np.random.choice(range(2),sus[i],p=[1-beta*(inf[i]/N),beta*(inf[i]/N)])
    b= np.random.choice(range(2),inf[i],p=[1-gamma,gamma])
    #randomly pick pots

    for j in range (0,sus[i]):
        inp+=(a[j])
    for k in range (0,inf[i]):
        rep+=(b[k])
    inf.append(inf[i]+inp-rep)
    rec.append(rec[i]+rep)
    sus.append(sus[i]-inp)
    #append new number to the list
    
    inp=0
    rep=0
    #Clear out the changed number

p=np.arange(0,1001,1)
plt.figure(figsize=(3,2),dpi=150)
plt.plot(p, sus, label='susceptible')
plt.plot(p, inf, label='infected')
plt.plot(p, rec, label='recovered')
plt.title('SIR model',fontsize=10)
plt.xlabel('time',fontsize=5)
plt.ylabel('number of people',fontsize=5)
plt.tick_params(axis='both',labelsize=3)
plt.legend(loc='upper right')

plt.savefig(r'C:\Users\梦之起点\Desktop\practical 13',type='png')
    
    
    








