print("============= READING THE FILE ================")
fd = open("Sample.txt","r")
print(fd.read())
fd.close()

print("======== READING LINE BY LINE =================")
fd = open("Sample.txt","r")
while True:
	line=fd.readline()
	print(line)
	if line == "":
		print("end of file")
		break
fd.close()

print("============= readlines =================")

fd = open("Sample.txt","r")
print(fd.readlines())
fd.close()


fd.close()