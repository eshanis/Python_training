#INHERITANCE
#one class aquires property of another class
# check for "is a" relationship
#if not no inhertance
# if "has a " relation then it is composition NOT inheritance

#1 SINGLE INHERITANCE
# ONE BASE CLASS AND ONE CLASS DERIVED FROM BASE CLASS
"""
class Base(object):
	pass

class Derived(Base):
	pass
"""
print("+++++++++++++++++++++++++")

#example Employee - Developer has "is a " relation

class Employee:
	def __init__(self):
		self.__fname = input("enter fname: ")
		self.__lname = input("enter lname: ")
		self.__email = self.__fname + "." + self.__lnam+"@mail.com"
		print("Employee")

class Developer(Employee):
	def __init__(self):
		self.__plang = input("Enter plang: ")
		print("Developer")

dev = Developer() #??

print("++++++++++ if no constructor in derived class (Developer) +++++++++++++++++")

class Employee:
	def __init__(self):
		self.__fname = input("enter fname: ")
		self.__lname = input("enter lname: ")
		self.__email = self.__fname + "." + self.__lname+"@mail.com"
		print("Employee")

class Developer(Employee):
	def func(self):
		self.__plang = input("Enter plang: ")
		print("Developer")

dev = Developer() #?? # it goes to the Developer class bcoz by default
                      # if there is not constructer in derived class then will got to base class

print("++++++++++ explicitly called both classes +++++++++++++++++++++")

#base class constructor and derived class constructor needs to be called
#this has to be done explicitly
#implicity only derived class will be called if it has a constructor

class Employee:
	def __init__(self):
		self.__fname = input("enter fname: ")
		self.__lname = input("enter lname: ")
		self.__email = self.__fname + "." + self.__lname+"@mail.com"
		print("Employee")

class Developer(Employee):
	def __init__(self):
		#super()  ==> goes to immediate Base class
		super().__init__()
		#self.__init__()  # another option in place of super()
		self.__plang = input("Enter plang: ")
		print("Developer")

dev = Developer()

print("+++++++++ to display the info using getters ++++++++++++")
class Employee:
	def __init__(self):
		self.__fname = input("enter fname: ")
		self.__lname = input("enter lname: ")
		self.__email = self.__fname + "." + self.__lname+"@mail.com"
		#print("Employee")
	def email(self):
		return self.__email
	def fullName(self):
		return self.__fname+ " " + self.__lname

class Developer(Employee):
	def __init__(self):
		super().__init__()
		self.__plang = input("Enter plang: ")
		#print("Developer")

	def display(self):
		print("Full Name: ", super().fullName())
		print("Email: ",self.email()) # or super.email
		print("Skill: ", self.__plang)

dev = Developer()
dev.display()

