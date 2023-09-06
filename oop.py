class Employee:
	pass

emp1 = Employee()
#when you print the below it gives you the memory location of the object
print(emp1)
print(id(emp1)) #id() is a function



print("============  METHOD 1 =============")

def fun():
	pass

#Method 1 : calling with the help of class name
class Sample:
	var = "hello all" # in this case the variable is called attribute
	def msg(): #static method when noparameters are present
		print("all okay")
		print("c the change")
		print(Sample.var)
Sample.msg()

print("============== METHOD 2 ====================")

#2 Method: calling with the help of object
class Sample:
	def msg(self): #static method when noparameters are present
		print("all okay")
		print("c the change")
		print("self is: ", self)
obj = Sample() #memory will be reserved
obj.msg()
print("obj is: ", obj)
#the above will give error becasue it passes the object as an object internaly
#self is a universal variable name that stores reference to the calling the current object

class Calc:
	def sum(self,n1,n2):
		sumOfTwo = n1+n2
		print("sum of two: ", sumOfTwo)
	def product(self,n1,n2):
		productOfTwo = n1*n2
		print("Product of Two: ", productOfTwo)
obj = Calc()
obj.sum(10,20) # obj.sum(obj,10,20) is what happens internally

obj2 = Calc()
obj2.product(100,20)

print(obj.sum(5,10),obj2.product(5,10))
print("obj id is: ", obj)
print("obj2 id is: ", obj2)
print ("================")
#below gives error bcoz you are asking to print name but that argument/parameter was not given when you called it
def func():
	print("hi", name)

func()

#below still gives error bcoz even though now you passed an argument, nothing to receive it
def func():
	print("hi", name)

func("Jack")

#no error below
def func(name):
	print("hi", name)

func("Jack")