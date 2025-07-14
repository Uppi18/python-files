from operator import true


# Function definition
def greet():
    print("Hello!")

# Function call
greet()   # Output: Hello!

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Output: Hello, Alice!
greet("Upendra")
# output; Hello, upendra

#Function call

print("Prime numbers from 0 to 100:")

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # check till square root of num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')

