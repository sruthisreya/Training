list1=["apple","banana","cherry","date","elderberry"]
list2=[]
for i in list1:
    if(len(i)>5):
        list2.append(i)
    else:
        print("no items")
print(list2)