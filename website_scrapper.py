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
browser.get('https://www.nurseryfair.com/exhibitor_info.asp?keyletter=*&id=1901')

outfile = open('websitedata/nurseryfair/nurseryfair_complete.csv', 'a+', newline='')
writer = csv.writer(outfile)
writer.writerow(
    ["name", "website", "address", "telephone", "actual_website", "email", "details"])

with open('websitedata/nurseryfair/nurseryfair.csv') as csv_file:
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
                # time.sleep(1)
                left_data = browser.find_element_by_class_name('infoleft')
                right_data = browser.find_element_by_class_name('inforight')
                # breakpoint()
                try:
                    address = " ".join([i for i in left_data.find_elements_by_tag_name('p')[0].text.split('\n') if
                                        "Web:" not in i and "Email" not in i and "Tel" not in i and "Fax" not in i])
                except:
                    address = "address"

                try:
                    telephone = \
                    [i for i in left_data.find_elements_by_tag_name('p')[0].text.split('\n') if "Tel:" in i][0].strip(
                        'Tel: ')
                except:
                    telephone = "telephone"
                try:
                    website = [i for i in left_data.find_elements_by_tag_name('p')[0].text.split('\n') if "Web:" in i][
                        0].strip('Web: ')
                except:
                    website = "website"
                try:
                    email = [i for i in left_data.find_elements_by_tag_name('p')[0].text.split('\n') if "Email:" in i][
                        0].strip('Email: ')
                except:
                    email = "email"
                try:
                    details = right_data.find_elements_by_tag_name('p')[1].text.split('\n')[0]
                except:
                    details = "details"

                # print(details)
                # breakpoint()
                writer.writerow(
                    [row[0], row[1], address, telephone, website, email, details])
            except Exception:
                print("IIIIIIIIIIIIIIIIIIIIIIIIIIIII" + row[1])
            line_count += 1
    print(f'Processed {line_count} lines.')
outfile.close()
browser.close()
