## Write a program to check whether the given input is valid or not. Consider
# the dynamic input from the user for mobile no.

try:
    Ph_num = int(input("Enter your mobile number: "))
    if len(str(Ph_num)) == 10:
        print(f"You entred a valid mobile number.\nyour mobile number is {Ph_num}.")
except ValueError:
    print("You entred a invalid mobile number.")

