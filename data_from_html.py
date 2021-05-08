from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib

outfile = open('websitedata/outdoortradeshow/outdoortradeshow.csv', 'a+', newline='')

writer = csv.writer(outfile)
writer.writerow(["name", "website", "details"])

filename = "websitedata/outdoortradeshow/outdoortradeshow.txt"
try:
    with open(filename) as file:
        soup = BeautifulSoup(file, "html.parser")
    items = soup.body.find_all('div', class_="text-cont")

    for item in items:
        try:
            website = item.h4.a['href']
        except:
            website = "website"
        try:
            name = item.h4.a.text.strip('\t \n')
        except:
            name = item.h4.text.strip('\t \n')
        try:
            details = item.p.text
        except:
            details = "details"
        print(
            website, name,
            details)

        writer.writerow([name, website, details])
    # print(category)
except FileNotFoundError:
    print("changing category from ")

# outfile.close()
