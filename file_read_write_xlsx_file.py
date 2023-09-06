#read and write xlsx

fd=open("data2.xlsx","w")
line1="123, Jack Black, 123456678, mum"
line2="123, Jill White, 8888888888, mum"
line3="123, Daisy Duck, 999999999, del"
line4="123, Mickey Mouse, 5656565656, lon"

fd.write(line1)
fd.write("\n")

fd.write(line2)
fd.write("\n")

fd.write(line3)
fd.write("\n")

fd.write(line4)
fd.write("\n")

fd.close()

with open("data2.xlsx", "r") as fd:
	while True:
		line=fd.readline()
		print(line)
		if line=="":
			break
	print(fd.read())