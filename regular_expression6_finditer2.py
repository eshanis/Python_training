import re

fd = open("regexp_finditer.txt", "w")
# below command creates a new file Sample.txt
fd.write("This is a new sample finditer file.")
fd.write("\nI am writing something here.")
fd.write("\nThis is my mobile number 999.888.7777.6 and 777-222-3333.4")
fd.close()

# get mobile number from the file

pat = re.compile("[7-9]\d+[.-]\d+[.-]\d+[.-]\d")
with open("regexp_finditer.txt", "r") as fd:
	content = fd.read()

matches = pat.finditer(content)
for iter in matches:
	print(iter, iter.group())
	print(iter.group())