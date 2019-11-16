#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:33:02 2019

@author: chakra
"""


#A set is a collection which is unordered and unindexed. 
#In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)

#sets are unordered so that you wont know what ordered it will be displayed

#you cant access item with index  since sets are unordered
#use for loop with in to access the items

for x in thisset:
    print x;

#use if and in to check items in set
if "apple" in thisset:
    print("apple in set")
else:
    print("NO APPLE")


#or you can check with this too
print("banana" in thisset) #will display bollean

#once the SET is created you cannot change the items, but you can add new items.
#to add one items in the set, use add() methods.
#to add more than one method use uodate() methods.

thisset.add("mango")
print(thisset)

#multiple use upadte() and use ([elements here, elementshere])
thisset.update(["kiwi","avacoda","orange"])
print(thisset)

#get the length of the set use len() method
print(len(thisset))

#remove items
#To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("kiwi")
print(thisset)

#if the item to remove doesnot exist, remove() will display error message, so use discard()
thisset.discard("apple")
print(thisset)

#pop items remove any items, cant declare index since its unordered.
#the returntype is the items thats deleted from the list
x=thisset.pop()
print(x)

#clear() method is used to clean all items from the list, when cleared empty [] sets will be displayed
theset = {"apple", "banana", "cherry"}
theset.clear()
print(theset)


#tset = {"apple", "banana", "cherry"}
#del tset
#print(tset)

#Join Two Sets
#there are several ways to join two or more sets in Python.
#You can use the union() method that returns a new set containing all items-
# from both sets, or the update() method that inserts all the items from one set into another:

#The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)



#The set() Constructor
#It is also possible to use the set() constructor to make a set.
#Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#-----------------------------------------------------------------------------------------------
'''Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others'''


















