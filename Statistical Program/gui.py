from tkinter import *
import pandas as pd
import os
puzzle = __import__('grapher')

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
colcounter = 0

def toarr():
    string = E1.get()
    print("Values Entered: " + string)
    global tlist
    tlist = string.split(",")
    print(tlist)
    E1.delete(0, 'end')
    addtocsv()


def setcolname():
    global colname
    colname = [E2.get()]


def addtocsv():
    df = pd.DataFrame(tlist, columns=colname)
    if not os.path.isfile('C:/GitRepo/Side-Projects/Statistical Program/data.csv'):
        df.to_csv('data.csv', index=False)
    else:
        df.to_csv('data.csv', mode='a', header=False, index=False)


def newcolumn():
    str2 = E1.get()
    global tlist
    tlist = str2.split(",")
    df = pd.read_csv('data.csv')
    df[colname] = tlist
    df.to_csv('data.csv', index=False)


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
button_del.grid(row=2, column=0)

button_ncol = Button(root, text="Add Column", command=newcolumn)
button_ncol.grid(row=2, column=2)

button_disp = Button(root, text="Display Graph", command=puzzle.plotter)
button_disp.grid(row=2, column=1)

root.mainloop()
