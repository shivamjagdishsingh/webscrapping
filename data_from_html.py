from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib

# outfile = open('websitedata/nationaloutdoorexpo/nationaloutdoorexpo.csv', 'a+', newline='')
#
# writer = csv.writer(outfile)
# writer.writerow(["name", "website"])

filename = "websitedata/automechanika/1.txt"
try:
    with open(filename) as file:
        soup = BeautifulSoup(file, "html.parser")
    items = soup.find_all('li', class_="m-exhibitors-list__items__item--status-standard")
    breakpoint()
    for item in items:
        breakpoint()
        try:
            link = item.find('a', class_="m-exhibitors-list__items__item__header__title__link js-librarylink-entry")[
                'href']

        #     website = item.div.a['href']
        except:
            website = "website"
        try:
            name = item.find('a',
                             class_="m-exhibitors-list__items__item__header__title__link js-librarylink-entry").text
        except:
            name = "name"
        # try:
        #     details = item.p.text
        # except:
        #     details = "details"
        # print(website, name)
        #
        # writer.writerow([name, website])
    # print(category)
except FileNotFoundError:
    print("changing category from ")

# outfile.close()
