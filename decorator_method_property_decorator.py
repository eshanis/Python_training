# 3. PROPERTY DECORATOR

# 1. getter => to access private elements outside of the class
# 2. setter => to set value for private elements (can access only within the class)
# 3. deleter

# 1. we can treat a method as an attribute

# to call attribute : print(className.attribute) eg print(Employee.count)
# to call method in the same way print(Employee.get_info)
class Employee:

	def __init__(self, fname, lname, salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary

	def email(self):
		return self.fname + "." + self.lname + "@mail.com"


	def fullName(self):
		return self.fname + " " + self.lname


fname = "Jack"
lname = "Black"
salary = 99999

emp = Employee(fname, lname, salary)  # you HAVE to pass the three arguments
print(emp.email())
print(emp.fullName())

print("OPTION 1 for changing name does not work as the change is at the instance level")
fname = "Jane"  # this change will not occur as the change is at the instance level
print(emp.email())
print(emp.fullName())

print("OPTIOn 2  # this will not work either since fullName is a method")
emp1 = Employee(fname, lname, salary)
emp1.fullName = "Riya Sharma"
print(emp.fullName())

print("option 3: TO MAKE A CHANGE AT INSTANCE LEVEL - THIS WORKS!!")
emp.fname = "Jane"
emp.lname = "Brown"
print(emp.email())
print(emp.fullName())

print("+++++++++++++ #Option4 - setter property to assign a new value ++++++++++++++++++++")
class Employee:

	def __init__(self, fname, lname, salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary

	def email(self):
		return self.fname + "." + self.lname + "@mail.com"

	@property  # getter property
	def fullName(self):
		return self.fname + " " + self.lname

	@fullName.setter
	def fullName(self, name):
		self.fname, self.lname = name.split(" ")


fname = "Robin"
lname = "Sharma"
salary = 99999

emp = Employee(fname, lname, salary)  # you HAVE to pass the three arguments
print(emp.email())
print(emp.fullName)  # called as an attribute and not a method NOT print(emp.fullName()

emp.fullName = "Sam Smith"  # set using setter property
print(emp.email())
print(emp.fullName)