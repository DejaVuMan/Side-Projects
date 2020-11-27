import pandas as pd
import matplotlib.pyplot as plt

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
    data_top = list(data.head())
    a = data.columns.tolist()
    x_ax = data[a[0]]
    y_ax = data[a[1]]
    plt.title("Test")
    plt.plot(x_ax, y_ax, color="red", marker="o")
    plt.xlabel(data_top[0])
    plt.ylabel(data_top[1])
    plt.tight_layout()
    plt.show()


def bar():
    plt.style.use('fivethirtyeight')
    data = pd.read_csv('data.csv')
    data_top = list(data.head())
    a = data.columns.tolist()
    height = data[a[0]]
    plt.bar(['test', 'test2', 'test3', 'test4', 'test5'], height)
    plt.xlabel(data_top[0])
    plt.tight_layout()
    plt.show()
