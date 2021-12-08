class Parent1:
    def show1(self):
        print("I am from Parent 1")

class Parent2:
    def show2(self):
        print("I am from Parent 2")

class Child(Parent1, Parent2):
    def show3(self):
        print("I am from Child Class")

obj=Child()
obj.show1()
obj.show2()
obj.show3()

        
