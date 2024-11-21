# Function with arbitrary number of arguments
def sum_all(*args):
    total = sum(args)
    print(f"The sum of the numbers is {total}")

# Calling the function with different numbers of arguments
sum_all(1, 2, 3)
sum_all(4, 5, 6, 7, 8)


class Person:     # Class name with CamelCase convention
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("John", 30)
print(p1.name, p1.age)  # Output: John 30



my_set={1,2,3,4}
my_set.add(6)
print(my_set) 

a = 5
print("Type of a: ", type(a))

b = 5.0
print("\nType of b: ", type(b))

c = 2 + 4j
print("\nType of c: ", type(c))