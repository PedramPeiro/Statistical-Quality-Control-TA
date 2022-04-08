# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 12:24:17 2022

@author: Pedram Peiro
"""
def divs(num):
    if num==1: 
        return [1]
    
    else:
        divisor=[1,num]
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                divisor.append(i)
                if i != num/i:
                    divisor.append(int(num/i))
        return sorted(divisor)

# print(divs(98))