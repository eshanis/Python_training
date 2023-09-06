#MULTI LEVEL

class Base1:
	def __init__(self):
		print("Base1") # 4 this is printed first

class Base2(Base1):
	def __init__(self):
		super().__init__() #3 executed first due to init it goes to Base 1
		print("Base2")     # 5 this is printed second

class Derived(Base2):
	def __init__(self):
		super().__init__() #2 executed first but due to init it goes to Base 2
		print("derived")   # 6 this is printed third

d = Derived()  #1

print("========== to show the working ======================")


class Base1:
	def __init__(self):
		print("Base1")

	def display(self):
		print("Display-Base1")  #4 goes here . if this is not there then it will
						        # go to the immediate base class which is Base1


class Base2(Base1):
	def __init__(self):
		super().__init__()
		print("Base2")

	def display(self):
		print("Display-Base2") #3 goes here . if this is not there then it will
						       # go to the immediate base class which is Base1


class Derived(Base2):
	def __init__(self):
		super().__init__()
		print("derived")


	def display(self):
		print("Display-derived") # 2 goes here . if this is not there then it will
									#go to the immediate base class which is Base2


D = Derived() #1 when this is called


