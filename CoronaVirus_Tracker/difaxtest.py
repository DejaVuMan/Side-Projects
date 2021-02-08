import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data.csv')
time = data['Time']
ycurr = data['current']
ydif = data['difference']


# create figure and axis objects with subplots()
fig, ax = plt.subplots()
"""# make a plot
ax.plot(time, ycurr, color="red", marker="o")
# set x-axis label
ax.set_xlabel("Date", fontsize=14)
# set y-axis label
ax.set_ylabel("Total", color="red", fontsize=14)

# twin object for two different y-axis on the sample plot
ax2 = ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(time, ydif, color="blue", marker="o")
ax2.set_ylabel("Difference", color="blue", fontsize=14)
plt.show()
"""
line1, = ax.plot(time, ycurr, label='Current total')
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break

line2, = ax.twinx().plot(time, ydif, dashes=[6, 2], label='Difference')

ax.legend()
plt.show()
