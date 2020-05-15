# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:28:38 2020

@author: 梦之起点
"""
s=''#act as a seq storage
t=False # act as a switch
DNAname='' 
import re
gene=open('mito_gene.fa','w')
DNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
for line in DNA:
    
    if line.startswith('>'):
        if s != '':
            gene.write(DNAname + '      ' +str(len(s)) +'\n')
            t=False
            s=''
        if 'Mito:' in line:
          DNAname=re.findall(r'^>[0-9A-Z]+',line)
          #find the DNA name of the mito chromosome 
          DNAname=''.join(DNAname)         
          
          t=True
          s=''
          # clear out the seq storage          
    else:
        if t==True: 
          line=line.strip()#clear out the space
          s += line
          #accumulate the seq in each line.                                 
DNA.close()
gene.close()
gene=open('mito_gene.fa')
#reopen the file because we can't print lines in the writing style

for line in gene:
    print(line)
gene.close()





       


       

          
