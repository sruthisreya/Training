dict1={
    "name":"sruthi",
    "age":22,
    "place":"kochi",
    "city":"kakkanad"
}
print(dict1)
print(dict1.keys())
print(dict1.items())

for x in dict1:
    print(x)
for y in x:
    print(y)

dict1["color"]="red"
print(dict1)

dict1.update({'color':'green'})
print(dict1)

mydict=dict1.copy()
print(mydict)

for x in dict1.values():
  print(x)

for x in mydict.keys():
  print(x)

for x, y in mydict.items():
  print(x, y)