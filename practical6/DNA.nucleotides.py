# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:40:21 2020

@author: 梦之起点
"""
import matplotlib.pyplot as plt
#input the necessary library

a=0
t=0
c=0
g=0
seq='ATGCTTCAGAAAGGTCTTACG'

for i in range (0,len(seq)):
    if seq[i]== 'A':
        a+=1
    elif seq[i]== 'T':
        t+=1
    elif seq[i]== 'C':
        c+=1
    else:
        g+=1
#calculate the quantity of each nucleotides
        
        
print('The number of A: ',a)
print('The number of T: ',t)    
print('The number of C: ',c)
print('The number of G: ',g)

#draw a pie chart
labels = ['A', 'T','C','G']
sizes = [a, t, c, g]
colors = ['pink', 'yellow', 'gray', 'green']
explode = (0.05, 0, 0, 0)
plt.title('pie of the four DNA nucleotides')
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                                labeldistance=1.1, autopct='%2.0f%%', shadow=False,
                                startangle=90, pctdistance=0.6)

plt.axis('equal')
plt.show()
