# Write a generator function to yield squares of numbers from 1 to n.

n=int(input("enter number:"))
def square(n):
    for i in range(1, n+1):
        yield i*i
for j in square(n):
    print(j)