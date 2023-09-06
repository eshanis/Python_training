print("===============to display the information for N employees========================")

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
		print()

#dev = Developer()
#dev.display()

dev=[] #dev[0] = developer1, dev[1]=developer2 ...n etc.

#n => object
n = int(input("Enter number of employees: "))
for i in range(n):
	dev.append(Developer())

for i in range(n):
	dev[i].display()

