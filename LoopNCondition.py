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
    

#WHILE LOOP
#With the while loop we can execute a set of statements as long as a condition is true.

#Example
#Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i =i+1  #remember to increment i, or else the loop will continue forever.

print("---------------------------------------------------------------------------------")
#With the break statement we can stop the loop even if the while condition is true:

#Example
#Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
  
#With the continue statement we can stop the current iteration, and continue with the next:

#Example
#Continue to the next iteration if i is 3:
print("-------------------------------------------------------------------------------------")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
  
#The else Statement
#With the else statement we can run a block of code once when the condition no longer is true:
print("-------------------------------------------------------------------------------------")
#Example
#Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")  
  
  
#FOR LOOP
print("------for loop-----------------------------------------------------------------")
'''A for loop is used for iterating over a sequence (that is either a list, a tuple, 
a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in 
other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, 
set etc.'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x=="apple":
      print("love apple")
      
#list[], tuples(), set {}, dict{key,value     
#Looping Through a String
#Even strings are iterable objects, they contain a sequence of characters:

#Example
#Loop through the letters in the word "banana":

for x in "banana":
  print(x)


print("------------------------------------------")
#BREAK and Continue with for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
print("------------------------------------------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


print("------------------------------------------")
#range() in for loop

'''To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, 
and increments by 1 (by default), and ends at a specified number.'''

#print from 1 till 6(excluding) with jump of 2
for y in range(1,6,2):
    print(y)

#else in for loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

#Example
#Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
#NESTED LOOP
'''  A nested loop is a loop inside a loop.
The "inner loop" will be executed one time for each iteration of the "outer loop":
Example
Print each adjective for every fruit:'''

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
print("-------------pass statement------------------------")
'''for loops cannot be empty, but if you for some reason have a for-
 loop with no content, put in the pass statement to avoid getting an error.'''

#Example
for x in [0, 1, 2]:
  pass
print("------------------------------------------------------")
































  















    
