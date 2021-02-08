from urllib.request import Request, urlopen
import time
import os
import csv
from datetime import datetime
puzzle = __import__(r'mpl_disp')


if os.stat('memory.txt').st_size == 0:  # if text file is empty
    temp = 0
    pass
else:
    f = open('memory.txt')
    temp = int(f.readline())  # otherwise read the line and put value into temp to compare against
    f.close()

print("Welcome to this basic Web Scraper application which checks the amount of Coronavirus cases in Illinois.")
print("Press Ctrl + C to call upon exit from program.")
print("Scanning...")

disp = puzzle
disp.plotter()  # run plotter from mpl_disp.py to display last results

class WebScraper:
    now = datetime.now()
    Time = now.strftime("%m/%d/%y")
    fieldnames = ["Time", "difference", "current"]
    current = temp
    difference = 0
    nextc = 0

    def updatecrawl(self):
        url = Request('https://covidtracking.com/data/state/illinois', headers={'User-Agent': 'Mozilla/5.0'})
        # many websites deny access if suspected bot is lurking through the website.
        # We get around this by setting a User Agent.
        # all data is collected from covidtracking.com and updated regularly.
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        start_index = html.find("<div class=\"c4015\">") + len("<div class=\"c4015\">")
        # start index represents the div class in the raw HTML file where the current case amount is taken from
        end_index = html.find("</div><div class=\"_27e01\"")
        # end index is where we stop gathering the data from
        title = html[start_index:end_index]
        self.nextc = title
        self.nextc = self.nextc.replace(",", "")  # replace comma that exists in number with nothing

    def readpage(self):
        if int(self.current) != int(self.nextc):
            print('\a')  # notify user of update via audio - replaced old version with winsound
            print("UPDATE: + " + str((int(self.nextc) - int(self.current))) + " cases.")
            self.difference = (int(self.nextc) - int(self.current))
            # ensure both are ints ^^^^^^ due to formatting of info from site it could initially not be seen as int
            self.current = int(self.nextc)
            self.addtocsv()  # add current data to csv for graphing later
        else:
            print("Current Coronavirus Cases: " + str(self.current))

    def addtocsv(self):

        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)

            info = {  # write to CSV file under these 3 headers
                "Time": self.Time,
                "difference": self.difference,
                "current": self.current
            }
            csv_writer.writerow(info)
        disp.plotter()


test = WebScraper()

def driver():
    try:
        while 1:
            test.updatecrawl()
            test.readpage()
            # TODO: Fix Threading Issues with display graph realtime
            # Mostly fixed? by using plt.ion in mpl_disp, it freezes real time interactivity with the plot.
            time.sleep(15)  # wait 15 seconds before next check - could be changed to 300s to be honest
    except KeyboardInterrupt:
        g = open('memory.txt', 'w')  # on keyboard interrupt, open memory.txt
        g.write(test.nextc)  # write current cases amount to text file so it can be read and checked against next time
        g.close()  # safely close
        input("Press enter to exit")  # wait for input to close
        # if user presses Ctrl + C, raises KeyboardInterrupt and exits console.
        # Does not work in IntelliJ


driver()
