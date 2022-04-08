# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 21:09:20 2022

@author: Mr. Pedram
"""

def list_to_dic(color , code):
    dic1=dict()
    tot_list=[]
    for col,co in zip(color,code):
        dic1['color_name']=col
        dic1['color_code']=co
        tot_list.append(dic1)
    return tot_list
