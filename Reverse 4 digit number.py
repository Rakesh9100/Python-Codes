a = int(input("Enter your 4 digit number: "))

rev = 0
dig = 0

for x in range(4):
    dig = a%10
    rev = rev*10+dig
    a = a//10
print(rev)
