OVERLOADING THE OPERATOR : OPERATOR OVERLOADING

#1 special meaning for an operator
# same operatot for multiple purposes

# example
#+ ==> adding 2 +3 + 5

#but also used for CONCAT
"hi"+ " " + "world"
==>hi world

class A:
	pass

class B:
	pass

obj1 = A()
obj2 = B()

obj1 + obj2  # gives error message but can be done by operator overloading

#DUNDER METHODS :
#STARTED AND ENDS WITH DOUBLE UNDERSCORE
#PRE DEFINED METHODS

Arithmetic

__add__(self,other)
__subt__(self,other)
__mult__(self,other)
__div__(self,other)
__mod__(self,other)
__power__(self,other)
__floordiv__(self,other)