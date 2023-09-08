# image file
# first save a copy of an image eg. python image in the same folder if possible
# the first open , opens the image and reads the file
# second open will open another file and write to this file. this is the copy of the image

with open("python.jfif", "rb") as imgfile:
	imgobj=imgfile.read()
	with open("pythoncopy.jfif", "wb") as newimgfile:
		newimgfile.write(imgobj)