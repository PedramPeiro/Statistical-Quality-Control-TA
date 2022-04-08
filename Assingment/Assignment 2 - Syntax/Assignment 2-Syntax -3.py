# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 21:15:32 2022

@author: Mr. Pedram
"""

def counter():
    numbers=[]
    summation=0
    average=0
    count=0
    while True:
        string=input('enter a number: ')
        if string=='done':
            break
        number=float(string)
        numbers.append(number)
        
        #sum
        for i in numbers:
            summation+=i
            count+=1
            
        average=summation/count
    
    return (summation,average , count)    


print(counter())