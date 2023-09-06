# COMPLEX NUMBERS

class complexNum:
	def __init__(self, real, imaginary):
		self.real = real
		self.imaginary = imaginary

	def __str__(self):
		return str(self.real) + "+" + str(self.imaginary) + "i"

	def __add__(self, other):  # self is comp1 and other is comp2
		res_real = self.real + other.real
		res_imaginary = self.imaginary + other.imaginary
		#return str(res_real) + "+" + str(res_imaginary) + "i" # this works
		#return res_real, res_imaginary  #this will return (4,7) so does not work
		return complexNum(res_real, res_imaginary) #this works and returns 4+7i


comp1 = complexNum(1, 2) #self.real=1, self.imaginary = 2
comp2 = complexNum(3, 5)
print(comp1,comp2)
comp3 = comp1 + comp2
print("comp1+comp2 = " , comp3)
print("comp1+comp2 = ", comp3, "real = ", comp3.real, "imaginary= ", comp3.imaginary)