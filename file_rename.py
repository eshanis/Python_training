import os

os.rename("Sample.txt", "demo.txt")

fd = open("demo.txt","r")
print(fd.read())
fd.close()