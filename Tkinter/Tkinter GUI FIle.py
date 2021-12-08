>>> #How to create a GUI window using python
>>> from tkinter import *
>>> root = Tk()
>>> root.mainloop()

>>> #How to create a label using tkinter
>>> from tkinter import *
>>> root = Tk()
>>> lbl = Label(root, text = "User Name")
>>> lbl.pack(side = BOTTOM)
>>> root.mainloop()

>>> #How to create an entry box using tkinter
>>> from tkinter import *
>>> root = Tk()
>>> lbl = Label(root, text = "User Name").pack()
>>> lbl = Label(root, text = "Password").pack()
>>> ent1 = Entry(root).pack()
>>> ent2 = Entry(root).pack()
>>> root.mainloop()

>>> #How to divide your window in multiple frames
>>> from tkinter import *
>>> root = Tk()
>>> root.title("Frame Program")
''
>>> topframe = Frame(root)
>>> topframe.pack(side = TOP)
>>> bottomframe = Frame(root).pack(side = BOTTOM)
>>> redbtn = Button(topframe, text = "Red", fg = "Red", bg = "yellow").pack()
>>> greenbtn = Button(topframe, text = "Green", fg = "green", bg = "yellow").pack()
>>> redbtn = Button(topframe, text = "Blue", fg = "blue", bg = "yellow").pack()
>>> blackbtn = Button(bottomframe, text = "Black", fg = "Black", bg = "yellow").pack(side = BOTTOM)
>>> root.mainloop()

>>> #How to display a message box using tkinter
>>> from tkinter import *
>>> from tkinter import messagebox
>>> root = Tk()
>>> def msg():
	messagebox.showinfo("Hello Everyone","Welcome to python")

>>> btn = Button(root, text = "Click Me", bd = 20, bg = "red", fg = "yellow", command = msg).pack(side = TOP)
>>> root.mainloop()
