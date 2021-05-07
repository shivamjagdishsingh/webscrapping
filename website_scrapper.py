import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup

import os
import errno

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.ism-cologne.com/exhibitors-and-products/exhibitor-index/?fw_goto=aussteller/details&&kid=0002441403')

outfile = open('websitedata/ism/ism_complete.csv', 'a+', newline='')
writer = csv.writer(outfile)
writer.writerow(
    ["name", "website", "address", "telephone", "actual_website", "email"])

with open('websitedata/ism/ism.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count <= 0:
            line_count += 1
            continue
            # print(f'Column names are {", ".join(row)}')
        else:
            try:
                # browser.implicitly_wait(0)
                browser.get(row[1])
                time.sleep(3)
                try:
                    address = browser.find_element_by_class_name('cont').text
                except:
                    address = "address"
                try:
                    telephone = browser.find_element_by_class_name('ico_phone').text
                except:
                    telephone = "telephone"
                try:
                    website = browser.find_element_by_class_name('ico_link').text
                except:
                    website = "website"
                try:
                    email = browser.find_element_by_class_name('ico_email').text
                except:
                    email = "email"


                print(telephone, website, email)

                writer.writerow(
                    [row[0], row[1], address, telephone, website, email])
            except Exception:
                print("IIIIIIIIIIIIIIIIIIIIIIIIIIIII" + row[1])
            line_count += 1
    print(f'Processed {line_count} lines.')
outfile.close()
browser.close()
