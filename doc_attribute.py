# printing doc string

# __doc__ - this is an attribute NOT METHOD like init and str
# this will display everything in the comments. could be instaructions.

class Circle:
	"""This is an example fo rDoc attribute. This is where you give all the info about the method or program
	whatever info is written here, will be printed along with the program
	"""
	pi = 3.14

	def __init__(self):
		self.rad = int(input("enter radius: "))

	def area(self):
		print("Area of circle: ", Circle.pi * self.rad ** 2)

	def circum(self):
		print("Circumference of circle: ", 2 * Circle.pi * self.rad)

	def __del__(self):
		print(f"{type(self)} deleted")


obj = Circle()
obj.area()
obj.circum()
print(obj.__doc__)
