## Write a program in python to create a file consisting of some data. Write a
# function to calculate the count of words available in the given file.
# Write a function to calculate the count of words available in the given file
# which is having at least 3 chars.

f = open("Counting_program.txt", "w")
f.write("Just like we humans can understand a few languages (English, Spanish, Mandarin, French, etc.), so is the case with computers. Computers understand instructions that are written in a specific syntactical form called a programming language.")
f.close()
print("File created successfully.")
print("")

c = open("Counting_program.txt", "r")
print(c.read())
c.close()

d = open("Counting_program.txt", "r")
words = d.read().split(" ")
count = len(words)

print("")
print(f"The no.of words in the file = {count}.")

d = open("Counting_program.txt", "r")
passage = d.read().split(" ")

count = 0
for words in passage:
    if len(words) >= 3:
        count += 1


print("")
print(f"The no.of words having atleast 3 characters in the file = {count}.")
