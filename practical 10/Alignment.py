# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:48:39 2020

@author: 梦之起点
"""
mg=''
hg=''
rg=''
import pandas as pd# import the basic library
lib='ARNDCQEGHILKMFPSTWYVBZX'#A storage of amino acid species

score1=0
score2=0
score3=0
edit_distance1=0
edit_distance2=0
edit_distance3=0

mousegene=open('SOD2_mouse.fa')
humangene=open('SOD2_human.fa')
randomgene=open('RandomSeq.fa')
blosum= pd.read_csv("BLOSUM62 matrix.csv")

for line in mousegene:
    if not line.startswith('>'):
        mg+= line.strip()
        #fetch the DNA seq 

for line in humangene:
    if not line.startswith('>'):
        hg+=line.strip()

for line in randomgene:
    if not line.startswith('>'):
        rg+=line.strip()

def find(a):
    for i in range (0,len(lib)):
        if lib[i]==a:
            return i
#get the row number corresponding to species of amino acids


for t in range (0,len(mg)):
    score1+= (blosum.loc[find(mg[t]),hg[t]])  #find score in csv file 
print('The final score between mousegene and humangene', score1)

for t in range (0,len(mg)):
    score2 += (blosum.loc[find(mg[t]),rg[t]])
print('The final score between mousegene and randomgene', score2)

for t in range (0,len(hg)):
    score3+=(blosum.loc[find(hg[t]),rg[t]])
print('The final score between randomgene and humangene', score3)


edit_distance = 0 #set initial distance as zero
for i in range(len(hg)): #compare each amino acid
    if hg[i]!=mg[i]:
        edit_distance1 += 1
 #add a score 1 if amino acids are
    if hg[i]!=rg[i]:
        edit_distance2 +=1
    if rg[i]!=mg[i]:
        edit_distance3+= 1
#accumulate to calculate the distance

print('The edit diatance between human gene and mouse gene:', edit_distance1)
print('The edit diatance between random gene and huaman gene:', edit_distance2)
print('The edit diatance between random gene and mouse gene:', edit_distance3)











        

      

    






