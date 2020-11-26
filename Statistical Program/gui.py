from tkinter import *
import pandas as pd
import os

root = Tk()
L1 = Label(root, text="Enter Data Separated by commas")
L1.grid(row=0, column=0)
E1 = Entry(root, bd=5)
E1.grid(row=0, column=2)
L2 = Label(root, text="Column Name")
L2.grid(row=1, column=0)
E2 = Entry(root, bd=5)
E2.grid(row=1, column=2)

tlist = []
colname = ["name1"]

def toarr():
    string = E1.get()
    print("Values Entered: " + string)
    global tlist
    tlist = string.split(",")
    print(tlist)
    addtocsv()


def setcolname():
    global colname
    colname = [str(E2.get())]


def addtocsv():
    df = pd.DataFrame(tlist, columns=colname)
    if not os.path.isfile('C:/GitRepo/Side-Projects/Statistical Program/data.csv'):
        df.to_csv('data.csv', index=False)
    else:
        df.to_csv('data.csv', mode='a', header=False, index=False)


def delfile():
    if not os.path.isfile('C:/GitRepo/Side-Projects/Statistical Program/data.csv'):
        print("This file does not exist.")
    else:
        os.remove('C:/GitRepo/Side-Projects/Statistical Program/data.csv')


button_disp = Button(root, text="Enter", command=toarr)
button_disp.grid(row=0, column=1)

button_lab = Button(root, text="Set Name", command=setcolname)
button_lab.grid(row=1, column=1)

button_del = Button(root, text="Delete File", command=delfile)
button_del.grid(row=2, column=1)

root.mainloop()
