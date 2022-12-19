# Python 101

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# print(type(x)) # int
# print(type(y)) # float
# print(type(z)) # complex

# ----------------------------------
# Integers
xi = int(1)   # x will be 1
yi = int(2.8) # y will be 2
zi = int("3") # z will be 3

# ----------------------------------
# Floats
xf = float(1)     # x will be 1.0
yf = float(2.8)   # y will be 2.8
zf = float("3")   # z will be 3.0
wf = float("4.2") # w will be 4.2


# ----------------------------------
# Complex
# Complex numbers are written with a "j" as the imaginary part:
xc = 3+5j
yc = 5j
zc = -5j

print(type(xc))
print(type(yc))
print(type(zc))


# Casting in python is therefore done using constructor functions:
  # int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
  
  # float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
  
  # str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

