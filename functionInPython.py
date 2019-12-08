#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 02:01:55 2019

@author: chakra
"""

''' A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.  '''


#use def to define a function

def myfirstfun():
    a=22
    b=77
    c=b*a-b
    print(c)
#calling functions   
myfirstfun()


#functions with parameter

def mysecondfun(fname):
    print(fname + " naught")

mysecondfun("chakra")
mysecondfun("neopaney")

#default value parameters
#if no parameters are passed, default will be assigned
print("------------default parameters-------------------------")
def funtwo(country="NEPAL"):
    print("i am from " + country)

funtwo()
funtwo("BHUTAN")
funtwo("USA")
    
print("----------passing list as parameters-------------------")

fruits=["apple","banana","grapes"]
def listasparam(fruits):
    for x in fruits:
        print x

food=["momo","chowmin","thukpa"]
listasparam(food)
listasparam(fruits)

print("------------------RETURN VALUE---------------------------")

def thervalue(x):
    return 44*x

#here we are printing it, coz function doesnot have print it only has RETURN
print(thervalue(4))
    
#KEYWORDS ARGUMENTS
#You can also send arguments with the key = value syntax.

#This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#Arbitrary Arguments
#If you do not know how many arguments that will be passed into your function, 
#add a * before the parameter name in the function definition.

#This way the function will receive a tuple of arguments, and can access the items accordingly:
#If the number of arguments are unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#The pass Statement
#function definitions cannot be empty, but if you for some reason have a -
#function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass








