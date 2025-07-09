 # Logical operators are used to combine conditional statements.
 # They return True or False based on the logic applied.

 # AND OPERTOR

a = 10
b = 5
print(a > 5 and b < 10)   # True and True → True
print(a > 5 and b > 10)   # True and False → False

1-1=1
1-0=0
0-1=0
0-0=0

# OR OPERTORS
# Returns True if at least one condition is true.

a = 10
b = 5
print(a > 5 or b > 10)    # True or False → True
print(a < 5 or b > 10)    # False or False → False

# NOT OPERTORS
# Reverses the result.
# If a condition is True, not makes it False, and vice versa.

x = True
print(not x)     # False

y = False
print(not y)     # True

z = 5 > 3
print(not z)     # not True → False
