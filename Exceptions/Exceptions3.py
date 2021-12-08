## Write a program to create a list and handle various exception associated
# with it.

my_list = []
try:
    my_list.pop()
    my_list.append(1)
    my_list.extend([2,3])
    my_list.append()
    my_list.extend(5)
    my_list.pop()
except IndexError:
    print(my_list)
    print("Got some Index error")
except TypeError:
    print(my_list)
    print("Got some Type error")
except NameError:
    print(my_list)
    print("Got some Name error")
except EOFError:
    print(my_list)
    print("Got some Name error")
