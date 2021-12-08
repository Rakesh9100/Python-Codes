>>> ##Class - Collection of Data members and member functions OR Blueprint of an object OR Generic pointer to the object

>>> class demo:
	print("hello")
hello

>>> ##Object

>>> class demo:
	print("hello")
	obj=demo()
hello

>>> ##Data Members

>>> class area:
	length=0
	width=0
	obj=area()
	print(obj.length)
	print(obj.width)
0
0

>>> class area:
	length=0
	width=0
	obj=area()
	obj.length=int(input("Enter the Length: "))
	obj.width=int(input("Enter theWidth: "))
	print(obj.length)
	print(obj.width)
	
Enter the Length: 10
Enter theWidth: 25
10
25

>>> ##Member Function

>>> class rectangle:
	length=0
	width=0
	def area(self):
		print(self.length)
		print(self.width)
		obj=rectangle()
		obj.area()

0
0

>>> class sample:
	x=30
	def show(self,x):
		x=50
		print(x)
		print(x)
		obj=sample()
		obj.show(10)

50
50

>>> class sample:
	x=30
	def show(self,x):
		#x=50
		print(x)
		print(x)
		obj=sample()
		obj.show(10)

10
10

>>> class sample:
	x=30
	def show(self,x):
		x=50
		print(x)
		print(self.x)
		obj=sample()
		obj.show(10)

50
30

>>> ##Self Parameter: Whenever we want to access the instance variable (Variable declared inside the class and outside the member function)

>>> class demo:
	def method1(self):
		print("Hello")
	def method2(self):
		print("Hii")
		self.method1()
		obj.demo()
		obj.method2()

Hii
Hello

>>> ##Private Data Member

>>> class person:
	def _init_(self):
		self.name="RR"
		self.accno=241232
	def display(self):
		print("Name:",self.name)
		print("Account No:",self.accno)
		obj=person()
		obj.display()

Name: RR
Account No: 241232

>>> ##Object as a function argument

>>> class test:
	a=0
	b=0
	def __init__(self,x,y):
		self.a=x
		self.b=y
	def compare(self,other):
		if self.a==other.a and self.b==other.b:
			return True
		else:
			return False
			obj1=test(10,20)
			obj2=test(10,30)
			obj3=test(10,20)
			print("Case 1:",obj1.compare(obj2))
			print("Case 2:",obj1.compare(obj3))

Case 1: True
Case 2: False
