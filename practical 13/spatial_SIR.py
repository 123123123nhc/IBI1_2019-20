# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:50:02 2020

@author: 梦之起点
"""

import numpy as np 
import matplotlib.pyplot as plt

population = np. zeros ( (100 , 100) )
#All susceptible groups were sequenced


outbreak = np.random. choice (range(100) ,2) # choose the size
population [ outbreak [0] , outbreak [ 1 ] ] = 1
# make the plot
plt.figure(figsize=(6,4),dpi=150) 
plt.imshow(population,cmap='viridis',interpolation='nearest') 
# The purple squares represent all people, and the yellow dots represent infected people

beta = 0.3
gamma = 0.05
#input the basic parameter
for i in range(0,101):   
   infectedIndex = np.where(population==1)
for i in range(len(infectedIndex[0])):
    x = infectedIndex[0][i]
    y = infectedIndex[1][i]
    for xNeighbour in range(x-1,x+2):
        for yNeighbour in range(y-1,y+2):
          
            if (xNeighbour,yNeighbour) != (x,y):
              
                if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                   
                    if population[xNeighbour,yNeighbour]==0:
                        population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    infectedIndex = np.where(population==1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        population[x,y]=np.random.choice(range(2),1,p=[1-gamma,gamma])[0] + 1   
    plt.figure (figsize=(6,4),dpi=150) 
    plt.imshow(population,cmap='viridis',interpolation='nearest')
    