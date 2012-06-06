Classes
=======

In class we have covered several built in data types in python. Strings, lists, numbers, tuples and dictionaries are all very useful. The real word data is more complex. Think about how you would deal with something complex as say your bank account. How would be break down something like this into the datatypes we have already learned. Classes give us a way to create our own datatypes in python. Of course that is not the whole story. To really understand classes we need to understand object oriented programing. 

Object Oriented Programing
--------------------------
Object-oriented programing (OOP) is a way of creating new data structures that consists of both data types and methods that work on that data type that interact together. Really what that means is that its a way to take real world objects and discribe them in code. Lets look at a more real world example. Take for example a bank account. Each bank account has an account number, customer name, and balance, But those peices of information are different for each different account. This is where classes come in. We can create one data type for bank account and use it over and over again for each customer. 
::
	class BankAccount(object):
		accountNumber = 123456
		customerName = "The Doctor"
		balance = 9999999999999

At first glace this didn't buy us us really anything. We could access out values by using mython dot notation BankAccount.accountNumber. The first thing we need to learn about classes is that the class statement creates the class object and assigns it a name. It does not actually run any code. Just like when we use def to create a function. To actually get something we can use we have to create an instance of the object.
::
	myAccount = BankAccount()
	bobsAccount = BankAccount()
	mollysAccount = BankAccount()

	myAccount.accountNumber = 1
	bobsAccount.accountNumber = 2
	mollysAccount.accountNumber = 3

	print myAccount.accountNumber
	print bobsAccount.accountNumber
	print mollysAccount.accountNumber

This creates an instance of BankAccount and assigns it to myAccount. Each instance of the object is different but they share all the methods on the class. 