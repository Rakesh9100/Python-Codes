## Write a program in python to create a new file and explain any python term
# in it. Also add its strength separately using append function. Finally read
# the updated data.

demo2 = open("demo2.txt", "w")
demo2.write("Dictionaries: Dictionary is a built-in Python Data Structure that is mutable.\n It is similar in spirit to List, Set, and Tuples\.n However, it is not indexed by a sequence of numbers but indexed based on keys and can be understood as associative arrays.\n On an abstract level, it consists of a key with an associated value.\n In Python, the Dictionary represents the implementation of a hash-table.")
demo2.close()
print("The write operation is successful.")

demo2 = open("demo2.txt", "a") # a = append 
demo2.write("\nIt improves the readability of your code.\n Writing out Python dictionary keys along with values adds a layer of documentation to the code.\n If the code is more streamlined, it is a lot easier to debug.\n")
demo2.close()
print("The append operation is successful.")

read_demo2 = open("demo2.txt", "r")
read_demo2.read()
