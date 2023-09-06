class Circle:
	def __init__(self, rad):
		self.rad = rad

	def __str__(self):
		return f"the result:{self.rad}"

	def __add__(self, other):
		return str(self.rad) + other.rad # to combine int and string typecaste as str


C1 = Circle(3)
C2 = Circle("variable") # to combine int and string typecaste as str in method above
print(C1, C2)

print(C1 + C2)  # will call method __add__(calling object, c2)
# OR
C3 = C1 + C2
print(C3)

# calling object = C1
# method  = __add__
# arguments = C2

var1 = Circle(700)
var2 = Circle("var2")
print(var1+var2)