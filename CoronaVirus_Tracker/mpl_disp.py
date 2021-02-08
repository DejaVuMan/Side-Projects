# Realtime graph of coronavirus cases in Illinois

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.dates import date2num
def plotter():
    plt.style.use('classic')

    data = pd.read_csv('data.csv')
    time = data['Time'].tail(14)  # only read most recent 14 entries
    ycurr = data['current'].tail(14)
    ydif = data['difference'].tail(14)

    plt.close()  # ensures previously created graph is close
    fig, ax = plt.subplots()
    plt.title("Coronavirus Cases in Illinois")
    # make a plot
    ax.plot(time, ycurr, color="red", marker="o")
    # set x-axis label
    ax.set_xlabel("Date (MM/DD/YY)", fontsize=12)
    # set y-axis label
    ax.set_ylabel("Total Infections", color="red", fontsize=12)
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right',
             rotation_mode="anchor", fontsize=10)
    # twin object for two different y-axis on the sample plot
    ax2 = ax.twinx()
    # make a plot with different y-axis using second axis object
    ax2.plot(time, ydif, color="blue", dashes=[6, 2], marker="o")
    ax2.set_ylabel("D2D Difference", color="blue")
    plt.ion()
    plt.tight_layout()
    plt.pause(0.001)
    plt.show()
