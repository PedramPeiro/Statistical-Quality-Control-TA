# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 19:07:58 2022

@author: Pedram Peiro
"""

# sum and subtraction

1+5
a=5
b=12
a+b
c=a-b

#multiplication and division
a*b
a/b
b/a
b//a
int(11/2)

type(2*5.0)
2*5.0

#Power
3**2
pow(3,2)

25**0.5
import math as mt

mt.sqrt(25)

#sum over 2 string
'hello'+'world'
'hello'+' '+'world'

#sum over 2 list
[1,2,3]+[4,5,6,7,8,True,'ss']

#multiplication over strings
'hello '*5

#multiplication over lists
[1,2,3,4]*5

#operations over Bool
True+True+False
True*False
True+2+True-1


#----------------------------------------------
#logical operator
"<   >   <=   ==    !=  =>    in    is    not    ~"
5<10
11<=11
11<11
5==5
#5 is 5
6!=5

a=8
a==5


5 in [1,2,3,4,5,6,7,8,9]
'hello' in 'hello world'
'hello' in 'helloo world'
'hello' in 'heloo world'

'hello' not in 'hello world'

5 not in [1,2,3]


#-----------------------------------------------------
#if statement

number=26
if number == 25:
    print('number is 25')

 
if number == 25:
    print('number is 25')
else:
    print('number is not 25')


number=26
if number == 25:
    print('number is 25')
elif number==26:
    print('number is 26')   
else:
    print('number is not 25 and 26')

number=11
if number<10:
    print('lower range')
elif number<20:
    print('mid range')
else:
    print('out of range')


#----------------------------------------------------------------
True and True
True and False
True & True
True & False

True or True
True or False
False or False
True | True
True | False
False | False

#-----------------------------------------------------------------

num1=101
if num1==100:
    print('middle of the range')
elif (num1<50) or (num1>150):
    print('out of range')
elif (num1<75) or (num1>125):
    print('far from middle')
else:
    print('close to middle')

#-------------------------------------------------------------------
#while
count=0

while count<10:
    print('iteration',count)
    # count=count+1
    count+=1

count=0
while True:
    print('iteration',count)
    count+=1
    
    if count==10:
        print('the code will be stopped')
        break

num1=0
while num1<10:
    if num1==5 or num1==6:
        print('number is' , num1 , 'and is is going to be passed')
        num1+=1
        continue
        
    print(num1**2)
    num1+=1

#-------------------------------------------------------------------
#for
for num in range(0,10):
    if num==5 or num==6:
        print('number is' , num , 'and is is going to be passed')
        continue
    
    print(num**2)


lis=['hello' , 'apple' , 'stat' , 234 , 125.5]
for word in lis:
    print(word)

for i in range(len(lis)):
    print('item' , i , 'in the list is' , lis[i])

for i,word in enumerate(lis):
    print('item' , i , 'in the list is' , word)


#-----------------------------------------------------------------
#function
def add_number(num1 , num2):
    
    return num1+num2
    # res=num1+num2
    # return res

add_number(2,3)


def add_number(num1,num2,num3=10):
    return num1+num2+num3



num1=3
num2=4

add_number(num1,num2)
#-------------------------------------------------------------------
#example

def division_check(lis , num):
    result=[]
    #result=list()
    for i in lis:
        if i%num==0:
            result.append(i)
    return result

list_1=[10,12,13,14,2222,444,111]
division_check(list_1, 3)

    
    
    
    
    
    
    