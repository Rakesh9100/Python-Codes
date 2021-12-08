class test:
    a = 0
    b = 0
    def __init__(self,c,d):
        self.a = c
        self.b = d
    def compare(self,e):
        if self.a + self.b == e:
            return "The sum of numbers in obj == given value"
        else:
            return "The sum of numbers in obj != given value"


obj1 = test(1,2)
obj2 = test(3,4)

print("Case 1:", obj1.compare(3))
print("Case 2:", obj1.compare(10))
print("Case 3:", obj2.compare(7))
print("Case 4:", obj2.compare(2))
