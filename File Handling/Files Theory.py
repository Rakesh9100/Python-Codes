>>> #Create a file and Write the data into it
>>> file=open("FileBE.txt","w")   # w = write file operation

>>> ## Whenever we create a new file always create it in write mode or operation.
>>> file.write("This is my first file program")
29

>>> file.close()
>>> print("The file has been created successfully.")
The file has been created successfully.

>>> #How to read the data of the existing file.
>>> f=open("FileBE.txt","r")   # r = read file operation
>>> f.read()	# Read entire data at a time
'This is my first file program'

>>> f.readline()     #Read the data of single line
''

>>> f.readlines()     #Read the data of multiple lines
[]

>>> f.read(5)
''

>>> file=open("FileBE.txt","w")
>>> file.write("This is my first file handling program")
38

>>> file.close()
>>> print("The file has been created successfully.")
The file has been created successfully.

>>> f=open("FileBE.txt","r")
>>> f.read()
'This is my first file handling program'

>>> #How to add new data into the existing file.
>>> file=open("FileBE.txt","a")
>>> file.write(" This is python.")
16

>>> file.close()
>>> file=open("FileBE.txt","r")
>>> file.read()
'This is my first file handling program This is python.'

>>> #How to delete the existing file.

>>> import os
>>> os.remove("FileBE.txt")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    os.remove("FileBE.txt")
PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'FileBE.txt'

>>> import os
>>> os.remove("File.txt")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    os.remove("File.txt")
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'File.txt'
>>> if os.path.exists("File.txt"):
	os.remove("File.txt")
	print("The file has been removed sucessfully")
else:
	print("File not available")
File not available

>>> #How to create and delete a new foler
>>> import os
>>> os.mkdir("Sample Folder")   #mkdir = make directory
>>> print("New folder has been created")
New folder has been created

>>> import os
>>> os.rmdir("Sample Folder")   #rmdir = remove directory
>>> print("Existing Folder is deleted")
Existing Folder is deleted

>>> import os
>>> os.mkdir("Sample Folder")
>>> print("New folder has been created")
New folder has been created

>>> file=open("FileBE.txt","w")
>>> file.write("This is my first file program")
29

>>> file.close()
>>> print("The file has been created successfully.")
The file has been created successfully.

>>> file=open("Sample Folder/FileBE.txt","w")
>>> file.write("This is my first file program")
29

>>> file.close()
>>> print("The file has been created successfully.")
The file has been created successfully.
