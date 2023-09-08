import re
"""
with open ("rhyming.txt", "w") as fd:
	no=int(input("enter number: "))
	for i in range(no):
		inp=input()
		fd.write(inp)
		fd.write("\n")

with open ("rhyming.txt", "r") as fd:
	print(fd.read())
"""
	# condition: fetch all string that ends with "at" and not starts with "b"

pat = re.compile("[^b]at")
with open("rhyming.txt", "r") as fd:
		content = fd.read()

matches = pat.finditer(content)
print(matches)

print("++++++++++++++++++++")

pat2 = re.compile("[^b]at")  # print all except "bat"
with open("rhyming.txt", "r") as fd:
	content2 = fd.read()

matches2=pat2.finditer(content2)
for iter in matches2:
	print(iter.group())
	print(iter, iter.group())