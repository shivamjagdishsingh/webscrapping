import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup

import os
import errno

# anishdr
# atxtzmj0

categories = [
    # "Collectables-suppliers-88",
    # "Cookware_and_Kitchenware-suppliers-82",
    # "DIY_Products-suppliers-46",
    # "Domestic_Appliances-suppliers-47",
    # "DVDs_CDs_and_Blu_Ray-suppliers-71",
    # "Food_and_Beverages-suppliers-95",
    # "Furniture_and_Fittings-suppliers-48",
    # "Garden_and_Patio-suppliers-50",
    # "Handicrafts_Giftware_and_Decorations-suppliers-45",
    # "Household_Textiles-suppliers-97",
    # "Lighting_and_Electrical-suppliers-49",
    # "Pet_Products-suppliers-72",
    # "Security-suppliers-73",
    # "Toiletries_and_Cleaning-suppliers-89",
    # "Fax_Telephone_and_Imaging-suppliers-23",
    # "Office_Supplies-suppliers-24",
    # "Post_and_Packing_Supplies-suppliers-25",
    # "Retail_Equipment-suppliers-77",
    # "Stationery-suppliers-91",
    #
    # "Cycling-suppliers-62",
    # "Football_Shirts_and_Shoes-suppliers-60",
    # "Sports_and_Fitness_Supplies-suppliers-59",
    # "Trainers_and_Sportswear-suppliers-61",

    # "Car_Audio_and_Sat_Nav-suppliers-32",
    # "Digital_Cameras_and_Camcorders-suppliers-33",
    # "DJ_Equipment_and_Hi_Fi-suppliers-38",
    # "Gadgets_and_Electronics-suppliers-37",
    # "MP3_MP4_and_Accessories-suppliers-34",
    # "Satellite_and_TV_Accessories-suppliers-35",
    # "TV_DVD_and_Home_Audio-suppliers-36",
    #
    # "Cordless_Phones_and_Accessories-suppliers-55",
    # "Mobile_Phones-suppliers-56",
    "Mobile_Phones_Accessories-suppliers-57",
    "VOIP_and_Skype-suppliers-58",

    "Computer_Components-suppliers-27",
    "Computer_Consumables-suppliers-31",
    "Computer_Peripherals_and_Accessories-suppliers-30",
    "PC_Laptop_and_PDA_Wholesalers-suppliers-28",
    "Software-suppliers-29",
]

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.wholesaledeals.co.uk/search-suppliers/Batteries-suppliers.html')
time.sleep(30)

for category in categories:
    outfile = open("___" + category + '.csv', 'a+', newline='')
    writer = csv.writer(outfile)
    writer.writerow(
        ["object1", "object2", "phone", "fax", "mobile", "email", "website", "description", "actual website"])

    with open(category + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count <= 630 if categories.index(category) == 0 else 0:
                line_count += 1
                pass
                # print(f'Column names are {", ".join(row)}')
            else:
                # print(row[6])
                if row[6] != "website":

                    try:
                        # browser.set_page_load_timeout(10)
                        browser.get(row[6])

                        # browser.send_keys(Keys.CONTROL + 'Escape')

                        # time.sleep(1)
                        # breakpoint()
                        writer.writerow(
                            [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], browser.current_url])
                        print(row[0] + browser.current_url)
                    except Exception:
                        writer.writerow(
                            [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[6]])
                        print(row[0] + row[6])
                        print(line_count, " escaped ", category)
                        continue
                else:
                    writer.writerow([row[0], "website"])
                    print(row[0] + " |||||||||| " + "website")
                line_count += 1
                print(line_count, category)
        print(f'Processed {line_count} lines.')
    outfile.close()
browser.close()
