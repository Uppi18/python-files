# A set is an unordered, unindexed collection of unique elements.
# Sets are useful for removing duplicates and performing set operations like union, intersection, etc.

# Set Opertors

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)             # {1, 2, 3, 4, 5, 6}
print("Intersection:", a & b)      # {3, 4}
print("Difference:", a - b)        # {1, 2}
print("Symmetric Difference:", a ^ b)  # {1, 2, 5, 6}

# Creating a set
# Creating a set
my_set = {1, 2, 3, 4}
print(my_set)

# Set with duplicate values (duplicates are removed)
set_with_duplicates = {1, 2, 2, 3, 3}
print(set_with_duplicates)
# Output: {1, 2, 3}

# Creating an empty set
empty_set = set()
