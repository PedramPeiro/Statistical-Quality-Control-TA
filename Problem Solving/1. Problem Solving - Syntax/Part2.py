# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 12:48:34 2022

@author: Pedram Peiro
"""

def num_uniques(lis1):
    unique_list=[]
    for i in lis1:
        if i not in unique_list:
            unique_list.append(i)
    return len(unique_list)
        
# ili=[1,2,2,2,3,3,4,1,1,100,100,120,121,30,30,30]
# print(num_uniques(ili))