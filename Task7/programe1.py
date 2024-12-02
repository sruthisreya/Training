# Write a decorator print_sequence that ensures when a function is called, it prints "Start", then executes the function, and finally prints "End".

# Example Output:
# If the function is defined as:
# @print_sequence
# def greet(name):
#     print(f"Hello, {name}!")
# And the function is called like this:
# greet("Alice")
# The output should be:
# Start
# Hello, Alice!
# End
# How would you implement the print_sequence decorator?

def print_sequence(func):
    def inside(name):
        print("Start")
        func(name)  
        print("End")
    return inside
@print_sequence
def greet(name):
    print(f"Hello, {name}")
greet("Alice")




