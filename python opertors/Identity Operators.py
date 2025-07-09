# Used to compare memory locations.
1. is Operator
Returns True if both variables refer to the same object.

 2. is not Operator
Returns True if both variables do NOT refer to the same object.

a = [1, 2, 3]
b = a        # `b` and `a` refer to the same list
c = [1, 2, 3]  # `c` has the same content but is a different object

print(a is b)       # True  → same object
print(a is c)       # False → different object
print(a == c)       # True  → same values
print(a is not c)   # True  → different object

