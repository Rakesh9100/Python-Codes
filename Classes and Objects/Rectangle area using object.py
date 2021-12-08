class rect():
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
l = int(input("Please Enter the length of rectangle: "))
b = int(input("Please Enter the breadth of rectangle: "))
obj = rect(l,b)
print("The Area of rectangle is:",obj.area())
