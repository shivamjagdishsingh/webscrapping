from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv
import os
import errno

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

browser.get("https://www.springfair.com")

categories = [
            # "craft", "diy", "gadgets", "games", "gardentools",
              "greetings_and_stationary", "hair_care", "houseware",
              "jewellery_and_watches", "kitchenware", "makeup", "pet_care", "skin_and_bodycare", "toys"]

for category in categories:

    with open("springfair" + "/" + category + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count <= 0:
                line_count += 1
                continue
            else:
                try:
                    browser.get(row[1])
                    time.sleep(3)
                    html = browser.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    soup = soup.prettify()
                    print(line_count, time.time())
                    filename = "springfair" + "/" + category + "/" + str(line_count) + '.txt'

                    if not os.path.exists(os.path.dirname(filename)):
                        try:
                            os.makedirs(os.path.dirname(filename))
                        except OSError as exc:  # Guard against race condition
                            if exc.errno != errno.EEXIST:
                                raise
                    with open(filename, 'w+') as file:
                        file.write(str(soup))
                    file.close()
                except AttributeError:
                    print("issue")
                    continue

                line_count += 1
        print(f'Processed {line_count} lines.')
browser.close()
