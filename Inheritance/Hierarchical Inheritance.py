class Parent:
    def show1(self):
        print("I am from Parent")

class Child2(Parent):
    def show2(self):
        print("I am from Child Class 2")

class Child(Parent):
    def show3(self):
        print("I am from Child Class 1")

obj = Child()
obj.show1()
obj.show3()

obj2 = Child2()
obj2.show2()

        
