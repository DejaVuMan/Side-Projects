from tkinter import *
import pandas as pd
import os

root = Tk()
L1 = Label(root, text="Enter Data Separated by commas")
L1.pack(side=LEFT)
E1 = Entry(root, bd=5)
E1.pack(side=RIGHT)
L2 = Label(root, text="Column Name")
L2.place(relx=0.0, rely=1.0, anchor='sw')

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
    if not os.path.isfile('C:/GitRepo/Side-Projects/Statistical Program/list.csv'):
        df.to_csv('list.csv', index=False)
    else:
        df.to_csv('list.csv', mode='a', header=False, index=False)


button_disp = Button(root, text="Show", command=toarr)
button_disp.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
