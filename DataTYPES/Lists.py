# A list is a mutable, ordered, indexed collection that can contain duplicate elements.
# Lists are one of the most commonly used data structures in Python.

# Basic list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Mixed data types
info = [25, "Alice", 3.14, True]

# Empty list
empty = []

fruits = ["apple", "banana", "cherry"]

print(fruits[0])     # apple
print(fruits[-1])    # cherry
print(fruits[1:3])   # ['banana', 'cherry']
fruits[1] = "orange"
print(fruits)        # ['apple', 'orange', 'cherry']

students = ["Amit", "Sana", "John"]
students.append("Riya")
students.remove("John")
print(students)   # ['Amit', 'Sana', 'Riya']


Method      	Description	                  Example
append(x)    	Adds item to the end	       fruits.append("grape")
insert(i,x) 	Inserts item at index i	       fruits.insert(1, "kiwi")
remove(x)	    Removes first occurrence of x  fruits.remove("banana")
pop(i)       	Removes item at index i	       fruits.pop(0)
sort()	        Sorts the list	               fruits.sort()
reverse()	    Reverses the list	           fruits.reverse()
clear()	        Removes all elements	       fruits.clear()
index(x)	    Returns index of first x	   fruits.index("cherry")