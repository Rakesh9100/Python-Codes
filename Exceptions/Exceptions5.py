## Write a program to handle 5 exp in the dictionary

my_dict = {1:'one', 2:'two', 3:'three', 4:'four'}
try:
    del my_dict[3]
    print(my_dict[3])
    print(My_dict[1])
except NameError:
    print("There is a Name error.")
except KeyError:
    print("Given Key is not available.")
