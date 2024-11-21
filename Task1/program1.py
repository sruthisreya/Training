list1=[4,5,6,7,4,5,8,9,7]
list2=[]
list3=[]
for i in list1:
    if i not in list2:
        list2.append(i)
    elif i not in list3:
        list3.append(i)
print(list3)
    
       
