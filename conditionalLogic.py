#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 23:39:13 2019

@author: chakra
"""
#Indentation
'''Python relies on indentation (whitespace at the beginning of a line) 
to define scope in the code. Other programming-
languages often use curly-brackets for this purpose.'''

#if 

a=2
b=3

if a>b:
    print("a is less than b")
else:
    print("b is bigger")
    
    


#elif and else
#elif is written with if, if the first condition is not true.
#code can have many elif
#else define if all condition are not true

x=33
y=333

if x>y:
    print("x is greater")
elif x==y:
    print("y is equal to x")
else:
    print("y is greater")
    
    
#logical condition AND, OR, NOT can be used in if statement
#nested if can also be used
    
'''if statements cannot be empty, but if you for some reason have an if statement -
with no content, put in the pass statement to avoid getting an error.'''

#Example
a = 33
b = 200

if b > a:
  pass
    

    
