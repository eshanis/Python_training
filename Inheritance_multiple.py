#MULTIPLE INHERITANCE

# more than one base class
# STRUCTURE

"""
class Base1:
	pass

class Base2:
	pass

class Derived(Base1,Base2):
	pass

"""
#EXAMPLE


class Publisher:
	def __init__(self):
		self.__pName = input("Enter Publisher Name: ")
		self.__pPlace = input("Enter Publisher Place: ")
		# self.__init__() will not work. its recursive
		#super().__init__()  # this wiill work


class Author:
	def __init__(self):
		self.__aName = input("Enter Author Name: ")
		self.__aPlace = input("Enter Author Place: ")


class Book(Publisher, Author):
	def __init__(self):
		super().__init__()  # Publisher is first to called here first ie. immediate Base class
		Author.__init__(self)
		self.__bName = input("Enter Book Name: ")
		self.__bPlace = input("Enter Book Price: ")
"""
	def display(self):
		print("Author name: ", super().Author())
		print("Publisher name: ", self.Publisher())
		print("Book name: ", self.Book())
		print()
"""

book = Book()
## MRO  method resolution order

print(Book.mro())
print(Publisher.mro())
print(Author.mro())



















