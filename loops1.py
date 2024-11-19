fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

  for x in range(6):
      print(x)
else:
  print("Finally finished!")

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


num =0
while num < 5:
    num = num + 1
    print('num = ', num)


number = 5
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print("Factorial is:", factorial)