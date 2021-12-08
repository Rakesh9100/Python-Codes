from tkinter import *

root = Tk()

lb = Listbox(root)
lb.insert(1,"Python")
lb.insert(2,"Java")
lb.insert(3,"C++")
lb.insert(4,"C")
lb.insert(5,"HTML")

lb.pack()

root.mainloop()
