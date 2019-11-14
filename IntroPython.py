# -*- coding: utf-8 -*-

print("hello")

print("some basic of python")

'''DATA  TYPE
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
-----'''

#-------------------------------------------------------------------
#getting data type of a variable

a=8
b='chakra'
print(type(a)) #this will give int
print(type(b)) #this will give str

ab= True
print(type(ab)) #this will print boll


#more example:
x=20.5 #set to float, if decimal point
d=1j #set to complex data type
e=["apple", "banana", "cherry"] #List data type
f=("chakra", "ramesh", "ram")# tuple data type
g=range(9) #range data type
h={"acb","bcd","fgfg"}#set data tyoe
i={"name":"ram", "age":55} #dict data type
xy= frozenset({"apple", "banana", "cherry"}) #frozenset
cd= b"Hello" #bytes data type
x = bytearray(5) #bytearray data type
x = memoryview(bytes(5)) #memoryview data type
#--------------------------------------------------------------

#gow to set datatype
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
yes = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	 #range	
x_x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x_ = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview
#------------------------------------------------------------
print(x_x)
print(yes)
print(x_)

#Number types in python
#THREE TYPES - NUMBER, FLOAT, COMPLEX

com=35e4
print(type(com))  #will display float

co=4+7j
print(type(co)) #will print complex

#---------------------------------------------------------------
#TYPE CONVERSION
xax = 1 # int
yy = 2.8 # float
zz=1j # complex

#convert from int to float:
a = float(xax)

#convert from float to int:
b = int(yy)

#convert from int to complex:
c = complex(zz)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

####cannot conver complex number into another data type

#----------------------------------------------------------
#RANDOM NUMBER
#python doesnot have random() function like other progrmming language
#it import random class to generate random number

import random
print(random.randrange(1,10)) #randomly prints number between 1 and 10 inclusive

#----------------------------------------------------------

#CASTING

#INTEGER casting

a=int(1)  #will print int 1
print(a)
b=int(1.9) #will print int 1, ignores .9
print(b)
c=int("7") #string "7" but prints only 7
print(c)


#float casting
p=float(1.2)  #printrs 1.2
print(p)     
q=float(1)  #prints 1.0 since its a int
print(q)
r=float("3.9")  #prints 3.9 simce its a string
print(r)


#string casting
l=str(123)
print(l)
m=str(123.00)
print(m)
n=str("chakra")
print(n)

#-----------------------------------------------------------------------

#PYTHON STRING
#string are decleared either single quote or double quote
a="chakra"
b='chakra'
#both "chakra" and 'chakra' are same

#multi line string
a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""

#OR
a='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua'''

#eithe way is same, use 3 ' or 3 "

#-------------------------------------------------------------------------
#string and array in python
#python doesnot hav char data type, it takes single letter as string 
chakra="my name is CP"
print(chakra[5])  #will print character in 5ht position


#slicing string
#prints 2 nd letter thats index 1 till index6, not 7
print(chakra[1:7]) 

#negative indexing
#Use negative indexes to start the slice from the end of the string:
#Get the characters from position 5 to position 1, starting the count from the end of the string:

b = "Hello, World!"
print(b[-5:-2])

#string length
#prints length of variable b
print(len(b))

#strip methods- removes any white space from beginning of the line
a = "  Hello, World! "
print(a.strip()) # returns "Hello, World!"

#lower case
ab="BHUTAN"
print(ab.lower())

#change lower to upper case
cd="nepal"
print(cd.upper())


#The replace() method replaces a string with another string:
#replace H with J

a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
#
a = "Hello, World!"
print(a.split(',')) # returns ['Hello', ' World!']


#CHECK STRING
#Check if the phrase "ain" is present in the following text:
#use IN or NOT IN
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


#string concatination
#adding two string togeter using +
a="cp"
b="neopaney"
c=(a+" "+b)
print(c)

#The format() method takes the passed arguments, formats them, and places -
#them in the string where the placeholders {} are:
#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#Escape Character
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
#An example of an illegal character is a double quote inside a string that is 
#surrounded by double quotes:
#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)


#Other escape characters used in Python:

"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value	
"""


#STRING METHODS
#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning





































































