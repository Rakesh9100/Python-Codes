mylist = list()

print("Enter the size of the list: ", end="")
n = int(input())

print("Enter", n, "elements in the list: ")
for i in range(n):
    mylist.append(input())

print("\nEnter an element to search: ", end="")
elem = input()

for i in range(n):
    if elem == mylist[i]:
        print("\nElement found at Index:", i)
        print("\nElement found at Position:", i+1)
