#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 19:00:14 2019

@author: chakra
"""

#A dictionary is a collection which is unordered, changeable and indexed. 
#In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#accesing items
#can access by give key
print(thisdict["model"]) #will print mustang

#can also use get() method
x=thisdict.get("year")
print(x)

#change year to 2010
thisdict["year"]="2010"
print(thisdict)

#loop through dictionary
#print all key
for x in thisdict:
    print(x)
print("----------------------")
#print all values
for x in thisdict:
    print(thisdict[x])
print("----------------------")    
#You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
  print(x)
print("----------------------")

#Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
  print(x, y)
  
#Check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword:
#Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Dictionary Length
#To determine how many items (key-value pairs) a dictionary has, use the len() method.
#Print the number of items in the dictionary:
print(len(thisdict))

#Adding Items
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Removing Items
#There are several methods to remove items from a dictionary:
#The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#he popitem() method removes the last inserted item (in versions before 3.7, 
#a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


#The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.


#clear items emptys the dictonaries
thisdict.clear()
print(thisdict)

#Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#making a copy with dict() methods
mydict = dict(thisdict)
print(mydict)

#NESTED DICTONARIES EXAMPLE
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


#The dict() Constructor
#It is also possible to use the dict() constructor to make a new dictionary:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
#----------------------------------------------------------------------------------------------------------
'''Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary'''
