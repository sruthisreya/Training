# to find type
x=5
print(type(x))


y="Hello world"
print(type(y))

x = ["apple", "banana", "cherry"]
print(type(x))


#slicing
b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[:7])

#Stringmofification
name="johnadams"
print(name.upper())

name="helloworld"
print(name.replace("o","rr"))
print(name.split(","))

#CONCATINATION
a="iam"
b="from"
c="kochi"
d=a+b+c
print(d)

#list
thislist = ["apple", "banana","mango", "cherry"]
thislist.append("orange")
print(thislist)
thislist.remove("banana")
print(thislist)

for i in thislist:
    print(i)

thislist1=[]
for i in thislist:
    thislist1.append(i)
    print(thislist1)
#listsort
thislist=["mango","banana","apple"]
thislist.sort()
print(thislist)

list2=[2,3]
for x in list2:
    thislist.append(x)
    print(thislist)

#tuple
tuple1=("hi","hello","you")
for i in tuple1:
    print(i)

print(tuple1[2])

#SET
set1={1,2,3,4,5}
set1.add("hello")
print(set1)
set1.remove(3)
print(set1)

s1={"a","b","c"}
s2={1,2,3,4}
s3=s1.union(s2)
print(s3)

#dictionary
dict1={
    "name":"sruthi",
    "age":23,
    "place":"kannur"
}
print(dict1)
print(dict1.keys())
dict1['color']="red"
print(dict1)
