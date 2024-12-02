# basic closure question
# Write a function make_multiplier(n) that returns another function. The returned function should take a single argument x and return the product of x and n

def product(n):
    def mul(x):
        return x*n
    return mul
a =product(3) 
result = a(5)        
print(result)
