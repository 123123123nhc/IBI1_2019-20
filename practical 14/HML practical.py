# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:16:02 2020

@author: Dell
"""


import xml.dom.minidom
import pandas as pd
# import libraries

ID1 = []; Name1 = []; Defstr1 = []; Is_a1 = []; CN=[]; count = 0; childnodes_number = []
# define variables
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
#open the file and then fetch the item


def count_childnodes(a):# define a function to count the number of child nodes
    global count
    C = {}
# accumulate count
    for term in terms:
# get is_a information
        childnodes = term.getElementsByTagName('is_a')
        c = childnodes.length

        if c !=0:
           for i in range(c):

               child = term.getElementsByTagName('is_a')[i]
               C[i] = child.childNodes[0].data

               if C[i].find(a) != -1:
                    ID = term.getElementsByTagName('id')[0]
                    IDc = ID.childNodes[0].data
                    count += 1
                    count_childnodes(IDc)
    return(count) # count is the real number of child nodes
for term in terms:

       ID = term.getElementsByTagName('id')[0]
       Name = term.getElementsByTagName('name')[0]
       Defstr = term.getElementsByTagName('defstr')[0]
       #to get more information

       if Defstr.childNodes[0].data.find('autophagosome') != -1:
          I = ID.childNodes[0].data
          N = Name.childNodes[0].data
          D = Defstr.childNodes[0].data
          ID1.append(I)
          Name1.append(N)
          Defstr1.append(D)
#
          count = 0
          count_childnodes(I)
          childnodes_number.append(count)
# clear out the count and calculate the new term
my_dict = {}
information = {'id':ID1, 'names':Name1, 'definition':Defstr1, 'childnodes':childnodes_number}
df = pd.DataFrame.from_dict(information)
df.to_excel("GO task.xls")


