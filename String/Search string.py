str = input("Enter the string: ")
str1 = input("Enter the string to be searched: ")
for str1 in str:
    if str1 in str:
        print("Present in the string")
        break
    else:
        print("Not present")
        break
