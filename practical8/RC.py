# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:49:08 2020

@author: 梦之起点
"""
reseq=[]
re=''
seq = 'ATGCGACTACGATCGAGGGCCAT'
for i in range (0,len(seq)):
    if seq[i]=='A':
      reseq+= 'T'
    elif seq[i]=='C':
      reseq+= 'G'
    elif seq[i]=='T':
      reseq+= 'A'
    else:
      reseq+= 'C'
#get the complementary chain

reseq.reverse()
reseqs=''.join(reseq)
#use list function to reverse the complementary chain and than change it into str

print(reseqs)