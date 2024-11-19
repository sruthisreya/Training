thistup = ("apple", "banana", "cherry","abc", 34, True, 40, "male")
print(thistup)

print(thistup[-1])
print(thistup[-5:-1])

y=list(thistup)
y[1]="helloworld"
thistup=tuple(y)
print(thistup)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

for x in thistuple:
  print(x)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

mytup=tuple1*3
print(mytup)