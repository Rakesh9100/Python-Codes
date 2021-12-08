>>> #Destructor

>>> class demo:
	def __init__(self):
		print("This is constructor")
	def __del__(self):
		print("This is destructor")

>>> obj=demo()
This is constructor

>>> obj1=obj
>>> print(id(obj))
2471147635424
>>> print(id(obj1))
2471147635424

>>> class demo:
	def __init__(self):
		print("This is constructor")
	def __del__(self):
		print("This is destructor")

>>> obj=demo()
This is constructor

>>> obj=obj1
This is destructor

>>> del obj
>>> del obj1
This is destructor

>>> print(id(obj))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(id(obj))
NameError: name 'obj' is not defined ##File is deleted above so this error

>>> print(id(obj1))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(id(obj1))
NameError: name 'obj1' is not defined ##File is deleted above so this error

>>> #Method Overloading

>>> class demo:
	def show(self,a):
		print("Hii")
	def show(self,a):
		x=a
		print(x)
		print("Hello")

>>> obj=demo()
>>> obj.show(10)
10
Hello

>>> class demo:
	def show(self,a):
		x=a
		print("Hii")
	def show(self,b,c):
		x=b
		y=c
		print(x)
		print(y)
		print("Hello")

>>> obj=demo()
>>> obj.show(10,20)
10
20
Hello

>>> class demo:
	result=0
	def add(self,instanceof=None,*args):
		if instanceof=="int":
			self.result=0
		if instanceof=="str":
			self.result=" "
		for i in args:
			self.result+=i
		return self.result

	
>>> obj=demo()
>>> print("Case 1:",obj.add("int",10,20,30))
Case 1: 60
>>> print("Case 2:",obj.add("str","I","like","python."))
Case 2:  Ilikepython.

>>> class demo:
	result=0 # Instance variable
	def add(self,instanceof=None,*args): #2
		if instanceof=="int": #3
			self.result=0 #4
		if instanceof=="str":
			self.result=" "
		for i in args: #5     10 20 30
			self.result+=i #6 result=0+10+20+30+40=100
		return self.result #7 result=100

	
>>> obj=demo()
>>> print("Case 1:",obj.add("int",10,20,30,40)) #1
Case 1: 100
>>> print("Case 2:",obj.add("str","I","like","python."))
Case 2:  Ilikepython.

>>> class overload:
	def greeting(self,name=None):
		if name is not None:
			print("Welcome "+name)
		else:
			print("Welcome to python")

			
>>> obj=overload()
>>> obj.greeting() # case1
Welcome to python
>>> obj.greeting("Modiji")
Welcome Modiji

>>> #Inheritance

>>> ##Single Level
>>> ##Multilevel
>>> ##Multiple
>>> ##Hierarchical
>>> ##Hybrid

>>> ##Single Level Inheritance
>>> class base:
	print("Hello")

Hello

>>> class child:
	print("Hii")
Hii

>>> obj=base
>>> obj=base()

>>> class base:
	def method1(self):
		print("Hello")

>>> class child(base):
	def method2(self):
		print("Hii")

>>> obj=child()
>>> obj.method1()
Hello

>>> obj.method2()
Hii

>>> def method1():
	print("Hello")

>>> def method2():
	print("Hii")

>>> method1()
Hello
>>> method2()
Hii

>>> #Multilevel Inheritance
>>> #A---> B---> C

>>> class A:
	def show1(self):
		print("Hello")

>>> class B(A):
	def show2(self):
		print("Hii")

>>> class C(B):
	def show3(self):
		print("How r u ?")

>>> obj=C()
>>> obj.show3()
How r u ?
>>> obj.show2()
Hii
>>> obj.show1()
Hello
