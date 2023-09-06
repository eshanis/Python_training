#DECORATOR

#adding additionall functionality to an existing method without disturbing the flow of it.
#WHAT IS NEEDED:
#1. declare an outer function that is called decorator
#2. takes only ONE argument
#3. declare inner function inside the decorator (write additional logic/change here)
#4. inner function should return result of previous step
#5.  oute function should return inner function


#ORIGINAL FUNCTION:
def add(n1,n2):
	return n1+n2

def mult(n1,n2):
	return n1*n2

print(add(2,3))
print(mult(3,4))
print("+++++++++++++++++++++++++++++")
#ORIGINAL FUNCTION

def add(n1,n2):
	return n1+n2

def mult(n1,n2):
	return n1*n2

num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
print("pow of sum: ", add(num1,num2))
print("pow of mult: ", mult(num1,num2))

print("++++++++++++++++++++++++++++")
#DECORATOR FUNcTION

def deco(func):  #DECORATOR FUNCTION COMMON TEMPLATE
	def inner(n1,n2):
		return func(n1,n2)**2
	return inner

@deco     #name of the decorator to apply decorator on top of the logic
def add(n1,n2):
	return n1+n2

def mult(n1,n2):
	return n1*n2

num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
print("pow of sum: ", add(num1,num2))
print("pow of mult: ", mult(num1,num2))

print("============= CHANGE DISPLAY TO UPPER CASE USING DECORATOR =================")
#ORIGINAL
def mystring(str1, str2):
	return f"hello {str1} {str2}"

print(mystring("Daisy", "Duck"))

#CHANGED TO UPPER CASE

def deco(func):  #DECORATOR FUNCTION COMMON TEMPLATE
	def toUpper(str1,str2):
		return func(str1,str2).upper()
	return toUpper

@deco
def mystring(str1, str2):
	return f"hello {str1} {str2}"

print(mystring("Daisy", "Duck"))