
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


