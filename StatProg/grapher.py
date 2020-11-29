import pandas as pd
import matplotlib.pyplot as plt


xlabel = "Default X Label"
ylabel = "Default Y Label"
title = "Default Title"


def gettitles(entryX, entryY, entryT, option):
    global xlabel
    if option == 1:
        xlabel = entryX.split(",")
    else:
        xlabel = entryX
    global ylabel
    ylabel = entryY
    global title
    title = entryT


def plotter():
    data = pd.read_csv('data.csv')
    a = data.columns.tolist()
    if len(a) == 1:
        bar()
    if len(a) == 2:
        line()


def line():
    plt.style.use('fivethirtyeight')
    data = pd.read_csv('data.csv')
    # data_top = list(data.head())
    a = data.columns.tolist()
    x_ax = data[a[0]]
    y_ax = data[a[1]]
    plt.title(title)
    plt.plot(x_ax, y_ax, color="red", marker="o")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()


def bar():
    plt.style.use('fivethirtyeight')
    data = pd.read_csv('data.csv')
    # data_top = list(data.head())
    a = data.columns.tolist()
    height = data[a[0]]
    plt.bar(['test', 'test2', 'test3', 'test4', 'test5'], height)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.show()
