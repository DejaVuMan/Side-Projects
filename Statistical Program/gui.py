from tkinter import *
import csv
import pandas as pd

root = Tk()
L1 = Label(root, text="Enter Data Separated by commas")
L1.pack(side=LEFT)
E1 = Entry(root, bd=5)
E1.pack(side=RIGHT)
tlist = []


def toarr():
    string = E1.get()
    print("Values Entered: " + string)
    global tlist
    tlist = string.split(",")
    print(tlist)
    addtocsv()


def addtocsv():
    df = pd.DataFrame(tlist, columns=["colummn"])
    df.to_csv('list.csv', index=False)


button_disp = Button(root, text="Show", command=toarr)
button_disp.pack()

root.mainloop()
