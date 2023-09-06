class Circle:
	def __init__(self, rad):
		self.rad = rad

	def __str__(self):
		return f"the result:{self.rad}"

	def __add__(self, other):
		return Circle(self.rad + other.rad)

#for int vales BOTH HAVE TO BE INT
C1 = Circle(3)
C2 = Circle(4)
print(C1, C2)

print(C1 + C2)  # will call method __add__(calling object, c2)
#OR
C3 = C1+C2
print(C3)
# calling object = C1
# method  = __add__
# arguments = C2

#for string values BOTH HAVE TO BE STRINGS
var1 = Circle("Python")
var2 = Circle("Programming")
print(var1+var2)
