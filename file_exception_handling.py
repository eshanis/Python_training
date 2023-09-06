#FILE WITH EXCEPTION HANDLING

try:
	fd = open("test.txt","r+")
except FileNotFoundError as e:
	print(e, "this file does not exist")
else:
	print(fd.read())
finally:
	fd.close()


print("======= when file does not exist ================")

#FILE WITH EXCEPTION HANDLING

try:
	fd = open("test2.txt","r+")
except FileNotFoundError as e:
	print(e, "this file does not exist")
else:
	print(fd.read())
finally:
	fd.close()