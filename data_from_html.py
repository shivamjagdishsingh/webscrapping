from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib

# outfile = open('springfair_website.csv', 'a+', newline='')

# writer = csv.writer(outfile)
# writer.writerow(["name", "website"])

outfile = open("websitedata/ism/ism.csv", 'a+', newline='')
writer = csv.writer(outfile)
writer.writerow(["name", "website"])
for i in range(2, 92):
    filename = "websitedata/ism/" + str(i) + ".txt"
    try:
        with open(filename) as file:
            soup = BeautifulSoup(file, "html.parser")
        items = soup.body.find_all('div', class_="item")

        for item in items:
            # breakpoint()
            website = "https://www.ism-cologne.com" + item.find("a", class_="initial_noline")['href']
            name = item.find("a", class_="initial_noline").text.strip("\n ")
            print(website, name)

            writer.writerow([name, website])
        # print(category)
    except FileNotFoundError:
        print("changing category from ")

outfile.close()
