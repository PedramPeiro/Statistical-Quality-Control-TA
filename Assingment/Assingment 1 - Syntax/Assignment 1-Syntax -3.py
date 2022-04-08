# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:24:57 2022

@author: Mr. Pedram
"""

def Quadratic_Equation_Solver(a,b,c):
    
    print('{}x^2 + {}x + {}'.format(a,b,c))
    delta=b**2-4*a*c
    
    if delta>0:
        x1=(-b-delta**0.5)/(2*a)
        x2=(-b+delta**0.5)/(2*a)
        return [x1,x2]
    elif delta==0:
        return [(-b-2*delta**0.5)/(2*a)]
    else:
        return 'there is no real root for this equation'


