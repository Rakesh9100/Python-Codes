## Practice Question : Write a program to create a file named as demo and insert
# the content. I love python programming into it. Also read only first 7
# characters of it.

demo = open("demo.txt", "w")
demo.write("I love Python programming.")
demo.close()
print("The write operation is successful.")

read_demo = open("demo.txt", "r")
read_demo.read(7)

