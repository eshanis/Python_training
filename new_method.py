# when object is created, init method is called
# but if new method is in the class, init will never get called.
# Only new will be called

#__new__() #non static method

class Sample:

	def __init__(self):
		print("I am init")

	def __new__(self): # without this method the "i am init" is printed.
		print("I am new")

obj = Sample()

print("++++++to call init inspite of new method write your own logic ++++++++++++++++")

#to call init inspite of new method write your own logic

class Sample:

	def __init__(self):
		print("I am init")

	def __new__(self):
		print("I am new")
		var = object.__new__(self)
		print(var)
		return var

obj = Sample()
print(obj)

print("")