from tkinter import *

root = Tk()

testlabel = Label(root, text="Hello World")
testlabel2 = Label(root, text="Goodbye World")

testlabel.grid(row=0, column=0)
testlabel2.grid(row=1, column=0)  # same column - one on top, one on bottom very funny

root.mainloop()
