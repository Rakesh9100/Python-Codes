n = int(input("Please Enter a number : "))
s = 0
temp = n
while temp > 0:
   dig = temp % 10
   s += dig ** 3
   temp //= 10
if n == s:
   print(n,"is an Armstrong number!!")
else:
   print(n,"is not an Armstrong number!!")
