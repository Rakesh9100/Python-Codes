def count(n):
    if n== 0:
        print("Blastoff")
    else:
        print(n)
        count(n-1)
a=int(input("Enter your number"))
count(a)
