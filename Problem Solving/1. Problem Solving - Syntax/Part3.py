# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 12:54:38 2022

@author: Pedram Peiro
"""

def check_strings(string_1 , string_2):
    if len(string_1) != len(string_2):
        raise Exception('the lengths of the strings aren\'t equal')
    else:
        length=len(string_1)
        count=0
        for i in range(0,length):
            if string_1[i]==string_2[i]:
                count+=1
    return count

#s1='salam'
# s2='salmam'
# print(check_strings(s1,s2))