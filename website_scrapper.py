import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup

import os
import errno

categories = [
    # 3, 5, 6,
    # 8, 9,
    # 11, 12, 13,
    14, 15, 16, 17, 19, 23, 24]

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.esources.co.uk/wholesale-suppliers/5/2/')
time.sleep(30)

for category in categories:
    outfile = open("___" + str(category) + '.csv', 'a+', newline='')
    writer = csv.writer(outfile)
    writer.writerow(
        ["name", "location", "products", "profile", "products_link", "website", "telephone", "actual_website"])

    with open(str(category) + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count <= 0:
                line_count += 1
                continue
                # print(f'Column names are {", ".join(row)}')
            else:
                # print(row[6])
                if row[6] != "website":

                    try:
                        # browser.set_page_load_timeout(10)
                        browser.implicitly_wait(0)
                        browser.get(row[5])
                        browser.implicitly_wait(0)
                        # browser.send_keys(Keys.CONTROL + 'Escape')

                        # if row[5] != browser.current_url:
                        #     browser.get(row[5])
                        writer.writerow(
                            [row[0], row[1], row[2], row[3], row[4], row[5], row[6], browser.current_url])
                        print(row[0] + browser.current_url)
                    except Exception:
                        writer.writerow(
                            [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[5]])
                        print(row[0] + row[6], " escaped ", Exception)
                        continue
                else:
                    writer.writerow([row[0], "website"])
                    print(row[0] + " |||||||||| " + "website")
                line_count += 1
                print(line_count, category)
        print(f'Processed {line_count} lines.')
    outfile.close()
browser.close()
