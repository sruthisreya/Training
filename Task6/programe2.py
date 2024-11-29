# Write a generator expression to filter out odd numbers from a list and print the resul

list1=[1,4,3,4,66,7,88,3,444,55,66,77,99,1]
odd_num=(x for x in list1 if x%2!=0)
for j in odd_num:
    print(j)