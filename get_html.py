from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os
import errno

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.wholesaledeals.co.uk/all-search/toys-suppliers.html')
time.sleep(30)

categories = [
    # "Collectables-suppliers-88",
    # "Cookware_and_Kitchenware-suppliers-82",
    # "DIY_Products-suppliers-46",
    "Domestic_Appliances-suppliers-47",
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

    # "Cordless_Phones_and_Accessories-suppliers-55",
    # "Mobile_Phones-suppliers-56",
    # "Mobile_Phones_Accessories-suppliers-57",
    # "VOIP_and_Skype-suppliers-58",

    # "Computer_Components-suppliers-27",
    # "Computer_Consumables-suppliers-31",
    # "Computer_Peripherals_and_Accessories-suppliers-30",
    # "PC_Laptop_and_PDA_Wholesalers-suppliers-28",
    # "Software-suppliers-29",

]

pages = [
    # 1, 166, 252, 145, 20, 422, 664, 241, 574, 169, 227, 117, 115, 2, 20, 103, 159, 41, 51,
    # 59, 9, 163, 61,
    # 21, 42, 82, 54, 26, 14, 75,
    # 9, 28, 66, 7,
    # 81, 25, 208, 58, 105,
]
for j in range(len(categories)):
    category = categories[j]
    page = pages[j]
    # for i in range(1, page + 1):

    for i in range(55, 56):

        browser.get('https://www.wholesaledeals.co.uk/supplier-category/' + category + '-' + str(i) + '.html')
        time.sleep(5)
        html = browser.page_source
        print(i)
        soup = BeautifulSoup(html, 'html.parser')
        soup = soup.prettify()

        filename = category + '/' + category + '-' + str(i) + '.txt'
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
