from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib

# outfile = open('springfair_website.csv', 'a+', newline='')

# writer = csv.writer(outfile)
# writer.writerow(["name", "website"])

categories = ["craft", "diy", "gadgets", "games", "gardentools", "greetings_and_stationary", "hair_care", "houseware",
              "jewellery_and_watches", "kitchenware", "makeup", "pet_care", "skin_and_bodycare", "toys"]

# categories = ["1", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
#               "u", "v", "w", "x", "y", "z", "other"]

for category in categories:
    outfile = open("springfair" + "/" + "csv" "/" + category + '.csv', 'a+', newline='')
    writer = csv.writer(outfile)
    writer.writerow(["name", "address", "website"])

    for i in range(1, 1000):
        filename = "springfair" + "/" + category + "/" + str(i) + '.txt'
        try:
            with open(filename) as file:
                soup = BeautifulSoup(file, "html.parser")
            sb = soup.body.find('div', class_="p-tabs__body__content is-visible")
            listhead = sb.find('div', class_="m-exhibitor-entry__item__body__contacts__address")
            if listhead is not None:
                # breakpoint()
                address = listhead.text.strip("\n Address").replace('\n               ', ' ')
            else:
                address = "address"
            listweb = sb.find('div', class_="m-exhibitor-entry__item__body__contacts__additional__website")
            if listweb is not None:
                # breakpoint()
                website = listweb.text.strip("\n Website").replace('\n               ', ' ')
            else:
                website = "website"

            listname = sb.find("div", class_="m-exhibitor-entry__item__body__contacts__logo--wrap")
            if listname.a is not None:
                # breakpoint()
                name = listname.a.img['alt']
            else:
                name = "address"
            print(website)

            writer.writerow([name, address, website])
            # print(category)
        except FileNotFoundError:
            print("changing category from ", category)
            break

    outfile.close()
