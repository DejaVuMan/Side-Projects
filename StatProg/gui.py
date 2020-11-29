from tkinter import *
import pandas as pd
import os
import csv

import StatProg.grapher as grf

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
    if not os.path.isfile('/StatProg/data.csv'):
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
    if not os.path.isfile('/StatProg/data.csv'):
        print("This file does not exist.")
    else:
        os.remove('/StatProg/data.csv')


def popupmsg():
    print('\a')  # Will not make noise in IntelliJ, but will work if run separately
    NORM_FONT = ("Helvetica", 10)
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text="Are you sure?", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Yes", command=lambda: [popup.destroy(), delfile()], bg='red')
    B1.pack(side=LEFT)
    B2 = Button(popup, text="No", command=popup.destroy, bg='green')
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
            gd.wm_title("Data Values")
    gd.geometry("200x300")
    gd.grid_columnconfigure(0, weight=1)
    gd.grid_columnconfigure(1, weight=1)
    gd.mainloop()


def showgraph():
    config = Tk()
    config.wm_title("Graph Label Configuration")
    labelx = Label(config, text="X Label")
    labely = Label(config, text="Y Label")
    labelt = Label(config, text="Title")
    xent = Entry(config, bd=5)
    yent = Entry(config, bd=5)
    tent = Entry(config, bd=5)
    setter = Button(config, text="Set Values",
                    command=lambda: [grf.gettitles(xent.get(), yent.get(), tent.get(), 0)], bg='blue')
    actdisp = Button(config, text="Show Graph",
                     command=grf.plotter)
    # TODO: Radio button for setting bar graph ind column names
    labelx.grid(row=0, column=0)
    labely.grid(row=1, column=0)
    labelt.grid(row=2, column=0)

    xent.grid(row=0, column=1)
    yent.grid(row=1, column=1)
    tent.grid(row=2, column=1)

    setter.grid(row=3, column=1)
    actdisp.grid(row=3, column=2)

    config.grid_rowconfigure(0, weight=1)
    config.grid_rowconfigure(1, weight=1)
    config.grid_rowconfigure(2, weight=1)


button_disp = Button(root, text="Enter", command=toarr)
button_disp.grid(row=0, column=1)

button_lab = Button(root, text="Set Name", command=setcolname)
button_lab.grid(row=1, column=1)

button_del = Button(root, text="Delete File", command=popupmsg)
button_del.grid(row=2, column=0)

button_ncol = Button(root, text="Add Column", command=newcolumn)
button_ncol.grid(row=2, column=2)

button_disp = Button(root, text="Display Graph", command=showgraph)
button_disp.grid(row=2, column=1)

button_csv = Button(root, text="Show Values", command=showcsv)
button_csv.grid(row=2, column=3)

root.geometry("500x150")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.wm_title("Graph Creator")
root.mainloop()
