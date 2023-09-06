
#READ AND WRITE IN CSV FILE

fd=open("data1.csv","w")
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

with open("data1.csv", "r") as fd:
	print(fd.read())