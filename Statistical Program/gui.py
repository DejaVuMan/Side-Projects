from tkinter import *

root = Tk()
L1 = Label(root, text="Enter Data Separated by commas")
L1.pack(side=LEFT)
E1 = Entry(root, bd=5)
E1.pack(side=RIGHT)


def test():
    print(E1.get())


button_disp = Button(root, text="Show", command=test)
button_disp.pack()

root.mainloop()
