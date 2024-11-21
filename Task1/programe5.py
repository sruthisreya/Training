word=input("enter sentence:")
count={}
for i in word.split():
    count[i]=count.get(i,0) + 1
print(count)