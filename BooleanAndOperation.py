#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:43:17 2019

@author: chakra
"""
#BOOLEAN -- THE bool() functions evaluates any value if its TRUE or False
print(bool("hello")) #will print true

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.

#he following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#In fact, there are not many values that evaluates to False, -
#except empty values, such as (), [], {}, "", the number 0, and the -
#value None. And of course the value False evaluates to False.

#The following will return False:
#run with print to show false output

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})



#Functions can Return a Boolean
#Python also has many built-in functions that returns a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

#Check if an object is an integer or not:

x = 200
print("value")
print(isinstance(x, int)) #will return true
#-------------------------------------------------------------------------------
        

#PYTHON OPERATION
#Python divides the operators in the following groups:

#Arithmetic operators
#---arithematic operation are +, -, /, %, *, **(exponential), //(floor division)


#Assignment operators
#----=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=

#Comparison operators
#----are ==, !=, >, <, >=, <=


#Logical operators
#---are-- AND, OR, NOT

#Identity operators
#used to check object if they are same object or not
#----are--- IS, IS NOT

#Membership operators
#Membership operators are used to test if a sequence is presented in an object:
#are ------IN, NOT IN


#Bitwise operators
#Bitwise operators are used to compare (binary) numbers:
#are--- &, |, ^,  ~, <<, >>