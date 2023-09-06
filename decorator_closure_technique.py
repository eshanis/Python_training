#CLOSURE TECHNIQUE
#1.IMPLEMENTED WITH THE HELP OF NESTED FUNCTIONS
#2. FUNCTIONALITY :
#Technique/ process where the outer function holds value of inner function even after going out of scope.
# value is retained
def expo(func):		    #4 func=add
	def inner(n1,n2):   #8
		return func(n1,n2)**2 #9 indirectly holding the func add,  #12 , #13
	return inner	    #5
                        #func is called here it won't get executed
                        # unless it is called
                        #here expo func goes out of scope

def add(n1,n2):             #10 add(,)
	return n1+n2        #11 return

def mult(n1,n2):
	return n1*n2

num1=int(input("enter num1: ")) #1
num2=int(input("enter num2: ")) #2
closfun1=expo(add)	        #3   #6 closfun1 is inner
print("pow of sum: ", closfun1(num1,num2)) #7 inner(num1,num2)

closfun2=expo(mult)	           #6 closfun1 is inner
print("pow of mult: ", closfun2(num1,num2)) #7 inner(num1,num2)