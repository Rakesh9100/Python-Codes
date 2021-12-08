## Write a program to create a folder named as Python and add file handling
# program into it. Further read the newly added program and then delete the
# program as well as the folder.

import os
os.mkdir("python7")
print("folder is created")

file = open("m.txt","w")
file.write("this is my program")
file.close()
print("file created")
f=open("m.txt","r")
f.read()
f.close()
os.rmdir("python7")
print("folder deleted")
os.remove("m.txt")
print("file deleted")
