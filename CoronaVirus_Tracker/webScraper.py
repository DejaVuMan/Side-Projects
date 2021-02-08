from urllib.request import Request, urlopen
import time
import os
import winsound

if os.stat('memory.txt').st_size == 0:
    temp = 0
    pass
else:
    f = open('memory.txt')
    temp = int(f.readline())
    f.close()

class WebScraper:
    current = temp
    nextc = 0

    def updatecrawl(self):
        url = Request('https://www.worldometers.info/coronavirus/usa/illinois/', headers={'User-Agent': 'Mozilla/5.0'})
        # many websites deny access if suspected bot is lurking through the website.
        # We get around this by setting a User Agent.
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        start_index = html.find("<title>") + len("<title>")
        end_index = html.find("</title>")
        title = html[start_index:end_index-14]
        self.nextc = title[22:29]
        self.nextc = self.nextc.replace(",", "")

    def readpage(self):
        if int(self.current) != int(self.nextc):
            winsound.Beep(300, 250)
            print("UPDATE: + " + str((int(self.nextc) - int(self.current))) + " cases.")
            self.current = int(self.nextc)
        else:
            print("Current Coronavirus Cases: " + str(self.current))


test = WebScraper()
try:
    while 1:
        test.updatecrawl()
        test.readpage()
        time.sleep(15)
except KeyboardInterrupt:
    g = open('memory.txt', 'w')
    g.write(test.nextc)
    g.close()
    pass
    # if user presses Ctrl + C, raises KeyboardInterrupt and exits console.
    # Does not work in IntelliJ
