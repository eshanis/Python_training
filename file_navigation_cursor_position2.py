print("========= readline by line to find cursor =============")
fd = open("test.txt","r")
print(fd.readline())
print(fd.tell())
#fd.close()

print("========= read to move cursor to required position ============")

fd = open("test.txt","r")
print(fd.tell())
fd.seek(19,0)
print(fd.tell())
print(fd.read())

print("====== to write after moving the cursor =============")


fd = open("test.txt","r+")
print(fd.tell())
fd.seek(19,0)
print(fd.tell())
fd.write("your name is Jack?")
fd.seek(0,0)
print(fd.read())
fd.close()


print("=========  FILE OBJECT ATTRIBUTES  =========================")
#FILE OBJECT ATTRIBUTES

#fd.closed - will return true if file is open
#fd.mode   - to check current mode, read. write etc.
#fd.name    - returns the file name


fd = open("test.txt","r+")
print("file name: " , fd.name)
print("file mode: ", fd.mode)
print("file status: ", fd.closed)
fd.close()
print("file status: ", fd.closed)