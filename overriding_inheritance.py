#OVERRIDING (INHERITANCE)

#More than one function that has the same name in its function signature/parameter

# single inheritance - one base class and many derived
#      Book
#Physics  Chemistry

# multiple inheritance - more than one base class
#Physics  Chemistry
#      Science


# Hybrid inheritance - combination of above two

class Book:
	def subName(self): #5 if subName is not present in any other class then this is called
		print("common bookname")

class Physics(Book):
	def subName(self): #3 if subName not present then chemistry is called
		print("Physics Book")

class Chemistry(Book):
	def subName(self): #4 if subName not present then Book is called
		print("Chemistry Book")

class Science(Physics, Chemistry):
	def subName(self): #2 if subName not present here then Physics is called
		print("Science Book") #1

obj = Science()
obj.subName()

print()
print("==============================")

class Book:
	def subName(self): #5 if subName is not present in any other class then this is called
		print("common bookname")

class Physics(Book):
	def subName(self): #3 if subName not present then chemistry is called
		print("Physics Book")

class Chemistry(Book):
	def subName(self): #4 if subName not present then Book is called
		print("Chemistry Book")

class Science(Physics, Chemistry):
	def subName2(self): #2 if subName not present or different like subName2 here then Physics is called
		print("Science Book") #1

obj2 = Science()
obj2.subName()