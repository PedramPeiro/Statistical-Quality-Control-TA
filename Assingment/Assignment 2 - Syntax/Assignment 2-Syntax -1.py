# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 21:05:38 2022

@author: Mr. Pedram
"""

def Factorial_Calculator(num):
    ans=1
    while num>0:
        ans=ans*num
        num=num-1
    return ans

print(Factorial_Calculator(6))