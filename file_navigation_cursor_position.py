# NAVIGATION

fd = open("test.txt","a")
no=int(input("enter number of lines to be inserted: "))
for i in range(no):
	line=input()
	fd.write(line) #fd.write(input())
	fd.write("\n")
#fd.close()

# use tell() method to return the current position of the cursor

print(fd.tell())

print("========= readline by line to fond cursor =============")
fd = open("test.txt","r")
print(fd.readline())
print(fd.tell())
#fd.close()


