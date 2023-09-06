"""
FILES

# Basic Operations:
#1. Open
#2. Close
#3. read/write
#4. update/delete

#open file
	open()

#close file
	close()

#write file
	write()
#read file
	read()
	readline()
	readlines()
# cursor movement
	seek()  # to move cursor to certain point
	tell()  # displays current cursor position


OPEN FILE

file descriptor = open("filePath", "accessMode")
FilePath:
	Absolute Path : given from root directory
	Relative Path : Just fileName is sufficient

	example:
	open("Sample.txt")  # if accessMode is not given default is "Read"

AccessMode
	r=> open file for read (default)
NOTE: when you open a file, cusror will be at th ebeginning fo your file.
	w=> open fril to write
		=>if the file is existing, and you try to open in the write mode, then file gets truncated /overwrites(existing file with data is gone and new file is created)
		=> if the file does not exist, new file is created
	x=>exclusive creating (opening file in safe mode)
		if file existing, creation fails so this is safe mode
	a=>append(only write)
NOTE: ain append mode cursor will always be at the end of the file in this mode

	b=>opne in binary mode (rb,wb,ab)=>read in binary, write in binary, append in binary
	t=>opne in text mode (default mode)
		+
		r+ => opne filein read and then write
		w+ => open file with write mode then read
		a+ => open file for write then read

		binary =>rb+, wb+, ab+


to CLOSE a file don't need file name. use file descriptor

file descriptor = open("filePath", "accessMode")

file descriptor.close()
"""

fd = open("Sample.txt", "w")
#below command creates a new file Sample.txt
fd.write("This is the write command in new sample file")
fd.write("\nThis allows us to perform write")
fd.close()

fd = open("Sample.txt","a") # to append instead of truncate
fd.write("    ")
fd.write("\nWelcome to all")
fd.write("           ")
fd.write("\nThis allows us to append the file wothout truncating")
fd.close()