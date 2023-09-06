# REAL TIME APPLICATION BANKING

class Account(ABC):  # abstract class so cannot create an object for Account. this is where it is used. Object will be only for Savings Account or Checking Account
	# attributes listed below
	customerName
	Mobile
	Address
	IFSC
	Branch
	Name
	AccountBalance

	# functionality listed below. withdraw will be abstract method
	deposit()
	balance()

	@abstractmethod
     withdraw()  # this will be diff for savings and current so we functionality needs to be the abstract method so you cannot create objects using this class. you have to redefine it like in the shapes example in square


class SavingAccount(Account):
	# ATTRIBUTE
	mimimumBalance = 5000

	def withdraw(): #you can create object for savingAccount separately once redefined
		pass

class CurrentAccount(Account):
	# ATTRIBUTE
	OverDraftLimit = 50,000

	def withdraw(): #you can create object for currentAccount separately once redefined
		pass