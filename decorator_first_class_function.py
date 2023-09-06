#FIRST CLASS FUNCTION:
#passing function as a parameter/argument for another function

"""
def func():
	pass
func(var)
func(first)
"""

#what can be passed as parameter for function:
#=> variable
print("++++++++++++++++++++++")
def fun():
	print("hi")

def disp():
	print("hello")

fun()
disp()
print("++++++++++++++++++++++")

def fun():
	return 10

res =fun()
print(res)

print("++++++++++++++++++++++")

def fun(mydisp): #3 mydisp=disp
	print("hi") #3
	return mydisp #4
def disp():
	print("hello")

newfun=fun(disp) #1  5 newfun=mydisp
print(newfun)   #6 newfun()

print("++++++++++++++++++++++")

#power of 2 with result add, mult

def expo(func): #2 func=add  , mult
	res=func(2,3)**2  #3 6==>5**2=25
	return res  #7

def add(n1,n2):  #4
	return n1+n2  #5  ==>res=5 then goes to the first function 5**2=25

def mult(n1,n2):
	return n1*n2  #3*2=6 then goes to first function 6**2=36

print("pow of sum: ", expo(add)) #1 8  result is 25
print("pow of mult: ", expo(mult)) #result is 36