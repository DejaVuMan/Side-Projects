from tkinter import *
import pandas as pd
import os
import csv
puzzle = __import__('grapher')

root = Tk()
L1 = Label(root, text="Enter Data Separated by commas")
L1.grid(row=0, column=0)
E1 = Entry(root, bd=5)
E1.grid(row=0, column=2)
L2 = Label(root, text="Column Name")
L2.grid(row=2, column=0)
E2 = Entry(root, bd=5)
E2.grid(row=2, column=2)

tlist = []
colname = ["name1"]
colcounter = 0

xlabel = "Default X"
ylabel = "Default Y"


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
        df.to_csv('data.csv', mode='a', header=False, index=False, columns=colname)


def newcolumn():
    str2 = E1.get()
    global tlist
    tlist = str2.split(",")
    df = pd.read_csv('data.csv')
    df[colname] = tlist
    df.to_csv('data.csv', index=False)


def removecolumn():
    df = pd.read_csv('data.csv')
    df.drop(E2.get(), inplace=True, axis=1)


def delfile():
    if not os.path.isfile('C:/GitRepo/Side-Projects/Statistical Program/data.csv'):
        print("This file does not exist.")
    else:
        os.remove('C:/GitRepo/Side-Projects/Statistical Program/data.csv')


def popupmsg():
    print('\a')  # Will not make noise in IntelliJ, but will work if run separately
    NORM_FONT = ("Helvetica", 10)
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text="Are you sure?", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Yes", command=lambda: [popup.destroy(), delfile()])
    B1.pack(side=LEFT)
    B2 = Button(popup, text="No", command=popup.destroy)
    B2.pack(side=RIGHT)

    popup.mainloop()


def showcsv():
    gd = Tk()
    with open("data.csv", newline="") as file:
        reader = csv.reader(file)

        # r and c will tell us where to grid the labels
        r = 0
        for col in reader:
            c = 0
            for row in col:
                label = Label(gd, width=10, height=2,
                              text=row, relief=RIDGE)
                label.grid(row=r, column=c)
                c += 1
            r += 1
    gd.mainloop()


button_disp = Button(root, text="Enter", command=toarr)
button_disp.grid(row=0, column=1)

button_lab = Button(root, text="Set Name", command=setcolname)
button_lab.grid(row=2, column=1)

button_del = Button(root, text="Delete File", command=popupmsg)
button_del.grid(row=4, column=0)

button_ncol = Button(root, text="Add Column", command=newcolumn)
button_ncol.grid(row=4, column=2)

button_disp = Button(root, text="Display Graph", command=puzzle.plotter)
button_disp.grid(row=4, column=1)

root.geometry("600x300")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.mainloop()
