# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:18:36 2020

@author: 梦之起点
"""

import matplotlib.pyplot as plt
import pandas as pd
l=[]
newcases=[]
world=[]
spain=[]
covid_data = pd.read_csv("full_data.csv")
#read the 'csv' file


print(covid_data.iloc[0:15:3,:])


for i in range (0,int(covid_data.describe().iloc[0,0])):
    if covid_data.iloc[i,1]=='Afghanistan':       
        l.append(True)
        
    else:
        l.append(False)
    if covid_data.iloc[i,1]=='World':       
        world.append(True)
        
    else:
        world.append(False)
    if covid_data.iloc[i,1]=='Spain':       
        spain.append(True)
        
    else:
        spain.append(False)
#use the boolean to confirm the location of some specific concties
      


print(covid_data.loc[l,'total_cases'])
print('The mean of new cases: ', (covid_data.describe().iloc[1,0]))
print('The median of new cases: ', (covid_data.describe().iloc[5,0]))
#the 'discribe()' is also a .csv file, so we could use the function loc and iloc
#use the discribe() to get the mean and median

newcases=covid_data.loc[world,'new_cases']

plt.boxplot(newcases,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False)
plt.title('Worldwide New Cases ')
plt.show()
#draw the boxplot

world_dates=covid_data.loc[world , 'date']
world_new_cases=covid_data.loc[world ,'new_cases']
world_new_deaths=covid_data.loc[world,'new_deaths']
#use the variebles to describe the x-axis and y-axis


plt.plot(world_dates, world_new_cases, 'b+')
#choose the x-axis, y-axis and the color
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
#choose the x-axis, y-axis and the direction
plt.title('New Cases')
plt.ylabel('Number Of Cases')
plt.show()

plt.plot(world_dates,world_new_deaths,'r+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('New Deaths')
plt.ylabel('Number Of Deaths')
plt.show()

spain_dates=covid_data.loc[spain,'date']
spain_new_cases=covid_data.loc[spain ,'new_cases']
spain_total_cases=covid_data.loc[spain ,'total_cases']

spain_new_cases=covid_data.loc[spain,'new_cases']
plt.plot(spain_dates,spain_new_cases,'y+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('Spainish Tendency')
plt.ylabel('Number Of New cases')
plt.show()

spain_total_cases=covid_data.loc[spain,'total_cases']
plt.plot(spain_dates,spain_total_cases,'g+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('Spainish Tendency')
plt.ylabel('Number Of Total cases')
plt.show()
#use the same way to draw the plot of spanish tendency.







