n = int(input("Enter the number : "))
reverse = 0
number = n
while(n != 0):
  remainder = n % 10
  reverse = reverse * 10 + remainder
  n = int(n / 10)
if(number == reverse):
  print("It is a Palindrome")
else:
  print("It is not a Palindrome") 
