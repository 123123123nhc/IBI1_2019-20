# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:07:01 2020

@author: 梦之起点
"""
import matplotlib.pyplot as plt
# Actually I don't know whether we could change the order of the gene list,
# So I wtite both of them.
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
Min=0 ; Max=0
#used to sign the shortest and longest sequence.

for i in range (0,len(gene_lengths)):
    if gene_lengths[i]<gene_lengths[Min]:
        Min=i #find the shortest sequence
    if gene_lengths[i]>gene_lengths[Max]:
        Max=i #find the longest sequence
del(gene_lengths[Min])
del(gene_lengths[Max])

'''
the situation that we could change the order:
gene_lengths.sort()
del(gene_lengths[0])
del(gene_lengths[-1])
'''


print(gene_lengths)
gene_lengths.pop()
plt.boxplot(gene_lengths,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False)
#adjust the plot's parameter

plt.show()

