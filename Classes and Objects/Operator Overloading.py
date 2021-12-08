class calculator:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        return self.x+other.x
    def __sub__(self,other):
        return self.x-other.x
    def __mul__(self,other):
        return self.x*other.x
    def __truediv__(self,other):
        return self.x/other.x
    def __mod__(self,other):
        return self.x%other.x

var1 = calculator(10)
var2 = calculator(5)

print("The sum is:",var1+var2)
print("The difference is:",var1-var2)
print("The product is:",var1*var2)
print("The quotient is:",var1/var2)
print("The reminder is:",var1%var2)
