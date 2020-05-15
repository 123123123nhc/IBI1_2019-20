# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:41:28 2020

@author: 梦之起点
"""

s=''#act as a seq storage
t=False #act as a switch. if 'mito' in line, it will changed into True
reseqs=''
reseq=[]
import re
DNAname=''
file=input('please input the file name:')
gene=open(file,'w')
#write the new file

DNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')

for line in DNA:
    if line.startswith('>'):
        if s != '':
            gene.write(DNAname + '      ' +str(len(s)) +'\n' )
            #change line between label and sequence
            for i in range (0,len(s)):
                if s[i]=='A':
                    reseq.append('T')
                elif s[i]=='C':
                    reseq.append('G')
                elif s[i]=='T':
                    reseq.append('A')
                else:
                    reseq.append('C')
            
            reseqs=reseqs.rstrip() # clear out the space
            reseq.reverse()
            reseqs=''.join(reseq)
            #get the reverse complementary chain
            
            gene.write(reseqs+'\n')        
            t=False
            #stop accumulate s when the reverse complementary chain has been output
            
            s=''
            reseq=[]
            reseqs='' #clear out the list after finishing outputting
        if 'Mito:' in line:
            DNAname=re.findall(r'^>[0-9A-Z]+',line)
            DNAname=''.join(DNAname) #change the list to str
            t=True
            #turn on the switch.
            s=''    
            # clear out the seq storage
    else:
        if t==True: 
            line=line.rstrip()
            s += line 
            # put the line into one string                     
             
gene.close()
DNA.close()





