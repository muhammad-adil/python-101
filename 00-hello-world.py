
# Python 101

# print("Hello, World!") 

# Python uses indentation to indicate a block of code.
if 5 > 2:
  print("Five is greater than two!")

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# print(type(x))
# print(type(y))
# print(type(z))

# ----------------------------------
# Integers
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Floats
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# ----------------------------------
# Strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0' 


# // String
a = "Hello, World!"
print(a[1])
# output is 
# e

b = "Hello, World!"
print(b[2:5])
# output is 
# llo

abc = " Hello, World! "
print(abc.strip()) 
# "Hello, World!" 


# The len() method returns the length of a string:
hello = "Hello, World!"
print(len(hello))
# output is 13

# The lower() method returns the string in lower case:
hw = "Hello, World!"
print(hw.lower())
# output is  hello, world! 


# The upper() method returns the string in upper case:
e = "Hello, World!"
print(e.upper())
# output is  HELLO, WORLD! 

# The replace() method replaces a string with another string:
f = "Hello, World!"
print(f.replace("H", "J"))
# Jello, World! 

# The split() method splits the string into substrings if it finds instances of the separator:
g = "Hello, World!"
print(g.split(",")) 
# returns ['Hello', ' World!'] 


# Python Operators

# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:
    # Arithmetic operators
    # Assignment operators
    # Comparison operators
    # Logical operators
    # Identity operators
    # Membership operators
    # Bitwise operators

#-------------------------------------------------------------------------------------------------
# Python Collections (Arrays)

# There are four collection data types in the Python programming language:
#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered and unindexed. No duplicate members.
#     Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

thislist = ["apple", "banana", "cherry"]
print(thislist)
# ['apple', 'banana', 'cherry'] 


# Access Items
# You access the list items by referring to the index number:
print(thislist[1])
# banana

# Change Item Value
# To change the value of a specific item, refer to the index number:
thislist[1] = "blackcurrant"
print(thislist)
# ['apple', 'blackcurrant', 'cherry'] 


# Loop Through a List
# You can loop through the list items by using a for loop:
for x in thislist:
  print(x) 
# apple
# banana
# cherry 


# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 
# Yes, 'apple' is in the fruits list 


# List Length
# To determine how many items a list have, use the len() method:
print(len(thislist))
# 3


# Add Items
# To add an item to the end of the list, use the append() method:
thislist.append("orange")
print(thislist)
# ['apple', 'banana', 'cherry', 'orange'] 


# To add an item at the specified index, use the insert() method:
thislist.insert(1, "orange")
print(thislist)
# ['apple', 'orange', 'banana', 'cherry'] 


# Remove Item
# There are several methods to remove items from a list:
# The remove() method removes the specified item:
thislist.remove("banana")
print(thislist)
# ['apple', 'cherry'] 



