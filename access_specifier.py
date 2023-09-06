# ACCESS SPECIFIER
# determines accessibility of the attribute

# 1. public
# 2. private
# 3. no protected in PYTHON

# 1 PUBLIC

# all elements are public in nature methods and attributes both unless you specify the accessibility as private

# 2. PRIVATE
# NO KEYWORK PRIVATE
# we use double underscore before the attribute or method
#eg __empDep make the public attribute private and then you cannot access outside the class.

class Employee:
	empDep = "Development"
	#__empDep2 = "IT" # this will throw an error since it is private attribute
	def __init__(self, fname, lname, salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary

	def email(self):
		return self.fname + "." + self.lname + "@mail.com"

	#def __email2(self): this will throw an error

	@property  # getter property
	def fullName(self):
		return self.fname + "." + self.lname

	@fullName.setter
	def fullName(self, name):
		self.fname, self.lname = name.split(" ")


fname = "Robin"
lname = "Sharma"
salary = 99999

emp = Employee(fname, lname, salary)  # you HAVE to pass the three arguments
print(emp.email())
print(emp.fullName)
print(Employee.empDep)  # this will print

print("=========  FOR PRIVATE METHOD =================")
class Employee:
	empDep = "Development"

	def __init__(self, fname, lname, salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary

	def __email(self):  # PRIVATE method NOW
		return self.fname + "." + self.lname + "@mail.com"

	def fullName(self):  # public method
		print(self.__email())
		return self.fname + " " + self.lname


fname = "Robin"
lname = "Sharma"
salary = 99999

emp = Employee(fname, lname, salary)
# print(emp.email())
print(emp.fullName())
# print(Employee.empDep) # this will print