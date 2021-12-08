filename = input("Enter the filename : ")
try:
    f = open(filename,"r")
except IOError:  # IOError -- Input Output Error
    print("The file you have entered is not available")
