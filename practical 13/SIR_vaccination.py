# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:49:30 2020

@author: 梦之起点
"""

import numpy as np 
import matplotlib.pyplot as plt

N=10000
beta=0.3
gamma=0.05
t=1000
sus=[9999] 
inf=[1]
rec=[0]
#create the list of the people number in different time
a=[]
b=[]
inp=0
rep=0
total=[]


#the number of people that been infected or recoverd.

for m in range (0,11):
    sus=[int(N*(1-m/10))]#the vaccination rate change the sus,rec,inf
    rec=[int(N*m/10)]
    inf=[1]
    for i in range (0,t):
        a= np.random.choice(range(2),sus[i],p=[1-beta*(inf[i]/N),beta*(inf[i]/N)])
        b= np.random.choice(range(2),inf[i],p=[1-gamma,gamma])

        for j in range (0,sus[i]):
            inp+=(a[j])#calculate the number of people that get infected
        for k in range (0,inf[i]):
            rep+=(b[k])#the number of peoplrthat that recoverd
        inf.append(inf[i]+inp-rep)
        rec.append(rec[i]+rep)
        sus.append(sus[i]-inp)
                #append new number to the list
        inp=0
        rep=0
        #Clear out the changed number    
    total.append(inf)
p=np.arange(0,1001,1)
plt.figure(figsize=(6,4),dpi=150)

plt.plot(p, total[0], label='10%')
plt.plot(p, total[1], label='20%')
plt.plot(p, total[2], label='30%')
plt.plot(p, total[3], label='40%')
plt.plot(p, total[4], label='50%')
plt.plot(p, total[5], label='60%')
plt.plot(p, total[6], label='70%')
plt.plot(p, total[7], label='80%')
plt.plot(p, total[8], label='90%')
plt.plot(p, total[9], label='100%')
#draw each plot

plt.title('SIR model with different vaccination rate',fontsize=10)
plt.xlabel('time',fontsize=8)
plt.ylabel('number of people',fontsize=8)
plt.tick_params(axis='both',labelsize=1)
plt.legend(loc='upper right')
plt.savefig(r'F:\IBI\.spyder-py3\image2',type='png')
#save the image to the specific path
