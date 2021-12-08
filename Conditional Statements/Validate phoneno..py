num = input("Enter the phone number: ")
for i in num:
    if num[0]=="6" or num[0]=="7" or num[0]=="8" or num[0]=="9" and num.isdigit() and len(num)==10:
        print("Valid Phone Number")
        break
    else :
        print("Invalid Phone Number")
        break
