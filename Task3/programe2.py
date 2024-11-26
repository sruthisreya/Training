import shutil
f=open('source.txt',"w")
f.write("python is a high level programming language")
f.close()

f=open("source.txt","r")
read=f.read()
print(read)

shutil.copyfile('source.txt','second.txt')
