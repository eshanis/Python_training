#CONTEXT MANAGER : WITH OPEN
#advantage: if you open this way, not required for you to close it manually using close()


with open("test.txt", "r") as fd:
	print(fd.read())

print("file status: ", fd.closed)

print("========== read line by line and ierate the list =======================")

with open("test.txt", "r") as fd:
	lines=fd.readlines() #returns the lines as a list
	print(lines)
	for x in lines:
		print(x)

print("=================================")
with open ("fruits.txt", "w") as fd:
	no=int(input("enter number: "))
	for i in range(no):
		inp=input()
		fd.write(inp)
		fd.write("\n")

with open ("fruits.txt", "r") as fd:
	print(fd.read())
