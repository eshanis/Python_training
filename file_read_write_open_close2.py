# to write more than one line to file in dynamic way


fd = open("test.txt","w")
no=int(input("enter number of lines to be inserted: "))
for i in range(no):
	line=input()
	fd.write(line) #fd.write(input())
	fd.write("\n")
fd.close()





