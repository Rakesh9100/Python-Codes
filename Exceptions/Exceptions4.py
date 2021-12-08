## Write a program to add random numbers in the file named as file2021.
# Perform proper exceptional handling on it.

from random import randint

import random
file = open("file2021.txt","w")
for i in range(50):
    a = random.randint(1, 100)
    file.write(str(a))
#file.write('The new text file is created using write function. ')
try:
    file = open("file2021.txt","r")
    file.write()
except TypeError:
    print("Got error in your command")
