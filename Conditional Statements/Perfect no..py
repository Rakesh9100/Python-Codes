n = int(input("Enter a number to check its perfect or not : "))
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum = sum+i
if(sum == n):
    print("Perfect Number!!")
else:
    print("Number is not perfect!!")
