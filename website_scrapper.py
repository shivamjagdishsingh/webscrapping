import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup

import os
import errno

outfile = open('website_data.csv', 'a+', newline='')
writer = csv.writer(outfile)
writer.writerow(["object1", "website"])

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.wholesaledeals.co.uk/search-suppliers/Batteries-suppliers.html')
time.sleep(30)
with open('whole_sale_contacts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            pass
            # print(f'Column names are {", ".join(row)}')
        else:
            # print(row[6])
            if row[6] != "website":
                browser.get(row[6])
                time.sleep(15)
                writer.writerow([row[0], browser.current_url])
                print(row[0] + " |||||||||| " + browser.current_url)
            else:
                writer.writerow([row[0], "website"])
                print(row[0] + " |||||||||| " + "website")
            line_count += 1

    print(f'Processed {line_count} lines.')

browser.close()
outfile.close()
