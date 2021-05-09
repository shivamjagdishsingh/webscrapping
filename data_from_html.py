from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib

outfile = open('websitedata/nationaloutdoorexpo/nationaloutdoorexpo.csv', 'a+', newline='')

writer = csv.writer(outfile)
writer.writerow(["name", "website"])

filename = "websitedata/nationaloutdoorexpo/nationaloutdoorexpo.txt"
try:
    with open(filename) as file:
        soup = BeautifulSoup(file, "html.parser")
    items = soup.body.find_all('div', class_="logo type-exhibitor")

    for item in items:
        # breakpoint()
        try:
            website = item.div.a['href']
        except:
            website = "website"
        try:
            name = item.find('span', class_="title").text
        except:
            name = "name"
        # try:
        #     details = item.p.text
        # except:
        #     details = "details"
        print(website, name)
        #
        writer.writerow([name, website])
    # print(category)
except FileNotFoundError:
    print("changing category from ")

# outfile.close()
