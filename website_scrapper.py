import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup

import os
import errno

links = [
    'https://www.automechanika-birmingham.com/welcome/Exhibitors/exhibitor-list?&page=1&sortby=title%20asc%20%2Ctitle%20asc&searchgroup=943063BF-exhibitors',
    'https://www.automechanika-birmingham.com/welcome/Exhibitors/exhibitor-list?&page=2&sortby=title%20asc%20%2Ctitle%20asc&searchgroup=943063BF-exhibitors',
    'https://www.automechanika-birmingham.com/welcome/Exhibitors/exhibitor-list?&page=3&sortby=title%20asc%20%2Ctitle%20asc&searchgroup=943063BF-exhibitors',
    'https://www.automechanika-birmingham.com/welcome/Exhibitors/exhibitor-list?&page=4&sortby=title%20asc%20%2Ctitle%20asc&searchgroup=943063BF-exhibitors',
    'https://www.automechanika-birmingham.com/welcome/Exhibitors/exhibitor-list?&page=5&sortby=title%20asc%20%2Ctitle%20asc&searchgroup=943063BF-exhibitors',
]

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
# browser.get(
#     'https://www.automechanika-birmingham.com/welcome/Exhibitors/exhibitor-list?&page=2&sortby=title%20asc%20%2Ctitle%20asc&searchgroup=943063BF-exhibitors')
#
outfile = open('websitedata/nationaloutdoorexpo/nationaloutdoorexpo_complete.csv', 'a+', newline='')
writer = csv.writer(outfile)
writer.writerow(
    ["name", "website", "details", "actual_website"])

# with open('websitedata/automechanika/nationaloutdoorexpo.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count <= 0:
#             line_count += 1
#             continue
#             # print(f'Column names are {", ".join(row)}')
#         else:
#             try:
item_count = 0
for i in links:
    # browser.implicitly_wait(0)
    browser.get(i)
    # breakpoint()

    # items = browser.find_elements_by_class_name('m-exhibitors-list__items__item--status-standard')
    link = browser.find_element_by_class_name('m-exhibitors-list__items__item__header__title__link')

    link.click()
    time.sleep(5)

    for page in range(100):
        time.sleep(5)
        try:
            name = browser.find_element_by_class_name("m-exhibitor-entry__item__header__title").text
        except:
            name = "name"
        try:
            description = browser.find_element_by_class_name("m-exhibitor-entry__item__body__description").text
        except:
            description = "description"
        try:
            website = browser.find_element_by_class_name(
                "m-exhibitor-entry__item__body__contacts__additional__website").find_element_by_tag_name(
                'a').get_attribute('href')
        except:
            website = "website"
        try:
            address = browser.find_element_by_class_name(
                "m-exhibitor-entry__item__body__contacts__address").text.replace('\n', ' ')
        except:
            address = "address"
        item_count += 1
        print(item_count)
        print(name, description, website, address)
        writer.writerow([name, description, website, address])
        # breakpoint()
        browser.find_element_by_class_name("pagination__list__item__link--next").click()
        time.sleep(2)

        # try:
        #     address = " ".join([i for i in left_data.find_elements_by_tag_name('p')[0].text.split('\n') if
        #                         "Web:" not in i and "Email" not in i and "Tel" not in i and "Fax" not in i])
        # except:
        #     address = "address"
        #
        # try:
        #     telephone = \
        #         [i for i in left_data.find_elements_by_tag_name('p')[0].text.split('\n') if "Tel:" in i][
        #             0].strip(
        #             'Tel: ')
        # except:
        #     telephone = "telephone"
        # try:
        #     website = data.find_element_by_tag_name('a').get_attribute('href')
        # except:
        #     website = "website"
        # # try:
        # #     email = [i for i in left_data.find_elements_by_tag_name('p')[0].text.split('\n') if "Email:" in i][
        # #         0].strip('Email: ')
        # # except:
        # #     email = "email"
        # try:
        #     d = data.find_element_by_tag_name('p').text
        #     if d != 'Go to website':
        #         details = d
        #     else:
        #         details = "details"
        # except:
        #     details = "details"

        # print(details, website)
        # breakpoint()
    # except Exception:
    # print("IIIIIIIIIIIIIIIIIIIIIIIIIIIII" + row[1])
# line_count += 1
# print(f'Processed {line_count} lines.')
outfile.close()
browser.close()
