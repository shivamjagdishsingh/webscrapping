from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv
import os
import errno

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

browser.get("https://www.ism-cologne.com/exhibitors-and-products/exhibitor-index/?fw_goto=aussteller/blaettern&fw_ajax=1&paginatevalues=&start=0")


for w in range(10, 1771, 20):
    browser.get("https://www.ism-cologne.com/exhibitors-and-products/exhibitor-index/?fw_goto=aussteller/blaettern&fw_ajax=1&paginatevalues=&start=" + str(w))
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.prettify()
    # print(line_count, time.time())
    # filename = "websitedata/ism/" + str(int((w+30)/20)) + '.txt'

    # if not os.path.exists(os.path.dirname(filename)):
    #     try:
    #         os.makedirs(os.path.dirname(filename))
    #     except OSError as exc:  # Guard against race condition
    #         if exc.errno != errno.EEXIST:
    #             raise
    # with open(filename, 'w+') as file:
    #     file.write(str(soup))
    # file.close()
    print((w+30)/20)
# except AttributeError:
#     print("issue")
#     continue

browser.close()
