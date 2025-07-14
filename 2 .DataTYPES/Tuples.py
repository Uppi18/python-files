# A tuple is a collection of ordered, immutable (unchangeable) elements.
# Used when you want to group related data and keep it unchanged.

# Basic tuple
my_tuple = (1, 2, 3)
print(my_tuple)

# Tuple with mixed data types
mixed = ("apple", 3.14, 10)
print(mixed)

# Single-element tuple (must have a comma!)
single = (5,)
print(type(single))  # Output: <class 'tuple'>

# Accessing Tuple Elements

t = (10, 20, 30, 40)

print(t[0])     # 10
print(t[-1])    # 40 (last element)
print(t[1:3])   # (20, 30)
