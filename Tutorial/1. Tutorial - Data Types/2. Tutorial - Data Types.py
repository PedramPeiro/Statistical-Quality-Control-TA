# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:10:07 2022

@author: Pedram Peiro
"""

print('hello world!')
print(10)


#int
type(10)

#float
type(-1.5624)
type(1.00)

#string
type('hello')


#boolean
type(False)
type(True)

#complex
type(1+2j)

#variable
a=576
type(a)
a='576'
a="576"
type(a)
print(a)

#----------------------------------
#list

l1=[1,2,7,54.73333,'QC' , 'DS',True]
l1[0]
l1[2]
l1[3:6]
l1[1:2]
l1[:2]
l1[2:]
l1[:]
l1[-1]
l1[-3:]
l1[4]='Stats'
l1[4]
l1[4:6]=['QC' , 'ML']
l1

## functions in lista
l2=[4,6,2,9,4,66,774,33333]

len(l2)
max(l2)
min(l2)
sorted(l2)
sorted(l2,reverse=True)

## methods
l2.sort()
l2.append(9030)
l2.pop()
l2.insert(3,999)
l2.reverse()
l2.index(774)
l2.count(4)
l2.append(4)
l2.count(4)


# Tuple
t1=('hello' , 11,2,2,3,'hey')
t1[0:3]
t1[1]=12 #error
t1.index('hey')
t1.count(2)


#dictionary
d1={1:'gum' , 2:'money' , 3:'key' , 4:'wallet'}
d1[2]
d1[2:4]  #error
d1={1:'gum' , 2:'money' , 'hehehe':'key' , 4:'wallet'}
d1['hehehe']
d1['hehehe']='hahaha'

d2={1:'one' , 2:'two' , 3:'three' , 4:'four'}
list(d2.keys())

d2.values()
list(d2.values())

d2.items()
list(d2.items())
list(d2.items())[3][1]

d2[2]
d2[5]
d2.get(5)
d2.setdefault(5,'five')


#set
s={1,2,2,2,2,2,2,2,4,5}
type(s)
s[2]   #error

s1={1,2,3,4}
s2={3,4,4,4,4,4,4,5,6,7,8}
s1.union(s2)
s1.intersection(s2)
s1.issubset(s2)
{4,5,6,}.issubset(s2)
s1.difference(s2)
