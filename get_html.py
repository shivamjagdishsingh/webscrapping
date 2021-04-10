from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os
import errno

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.esources.co.uk/wholesale-suppliers/1/')
time.sleep(30)

categories = [
    3, 5,
    6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 23, 24]

# break_ = False

for category in categories:
    for i in range(1, 1000):
        browser.get('https://www.esources.co.uk/international-suppliers/' + str(category) + '/' + str(i))
        # time.sleep(1)
        browser.implicitly_wait(0)
        url = browser.current_url
        old_url = 'https://www.esources.co.uk/international-suppliers/' + str(category) + '/' + str(i-1) + '/'
        # breakpoint()
        if old_url == url:
            print("changing category")
            break
        else:
            html = browser.page_source
            print(category, i)
            soup = BeautifulSoup(html, 'html.parser')
            soup = soup.prettify()

            filename = str(category) + '/' + str(i) + '.txt'
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc:  # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise

            with open(filename, 'w+') as file:
                file.write(str(soup))
            file.close()
browser.close()
