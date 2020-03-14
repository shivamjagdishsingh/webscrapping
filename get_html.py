from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('https://groceries.asda.com/special-offers/top-offers?cmpid=ahc-_-ghs-_-asdacom-_-hp-_-footer-_-ghs')
time.sleep(30)
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')
soup = soup.prettify()
with open('scraped_asda.txt', 'w+') as file:
    file.write(str(soup))
browser.close()