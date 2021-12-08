a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))
c = int(input("Enter the value of c = "))
if (a == b == c):
    print("Equilateral triangle")
elif (a == b or a == c or b == c):
    print("Isosceles triangle")
else:
    print("Scalene triangle")
