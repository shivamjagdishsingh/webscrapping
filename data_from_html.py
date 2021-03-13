from bs4 import BeautifulSoup
import csv
import os
import errno

# categories = [
#     "Baby_and_Children_Clothes-suppliers-18",
#     "Baby_Food-suppliers-20",
#     "Baby_Toys_and_Activities-suppliers-19",
#     "Maternity_and_Pregnancy-suppliers-21",
#     "Prams_and_Car_Seats-suppliers-22"
# ]
#
# pages = [167, 4, 54, 9, 3]


categories = [
    "Collectables-suppliers-88",
    "Cookware_and_Kitchenware-suppliers-82",
    "DIY_Products-suppliers-46",
    "Domestic_Appliances-suppliers-47",
    "DVDs_CDs_and_Blu_Ray-suppliers-71",
    "Food_and_Beverages-suppliers-95",
    "Furniture_and_Fittings-suppliers-48",
    "Garden_and_Patio-suppliers-50",
    "Handicrafts_Giftware_and_Decorations-suppliers-45",
    "Household_Textiles-suppliers-97",
    "Lighting_and_Electrical-suppliers-49",
    "Pet_Products-suppliers-72",
    "Security-suppliers-73",
    "Toiletries_and_Cleaning-suppliers-89",
    "Fax_Telephone_and_Imaging-suppliers-23",
    "Office_Supplies-suppliers-24",
    "Post_and_Packing_Supplies-suppliers-25",
    "Retail_Equipment-suppliers-77",
    "Stationery-suppliers-91",

    "Cycling-suppliers-62",
    "Football_Shirts_and_Shoes-suppliers-60",
    "Sports_and_Fitness_Supplies-suppliers-59",
    "Trainers_and_Sportswear-suppliers-61",

    "Car_Audio_and_Sat_Nav-suppliers-32",
    "Digital_Cameras_and_Camcorders-suppliers-33",
    "DJ_Equipment_and_Hi_Fi-suppliers-38",
    "Gadgets_and_Electronics-suppliers-37",
    "MP3_MP4_and_Accessories-suppliers-34",
    "Satellite_and_TV_Accessories-suppliers-35",
    "TV_DVD_and_Home_Audio-suppliers-36",

    "Cordless_Phones_and_Accessories-suppliers-55",
    "Mobile_Phones-suppliers-56",
    "Mobile_Phones_Accessories-suppliers-57",
    "VOIP_and_Skype-suppliers-58",

    "Computer_Components-suppliers-27",
    "Computer_Consumables-suppliers-31",
    "Computer_Peripherals_and_Accessories-suppliers-30",
    "PC_Laptop_and_PDA_Wholesalers-suppliers-28",
    "Software-suppliers-29",

]

pages = [
    # 1, 166, 252,
    145, 20, 422, 664, 241, 574, 169, 227, 117, 115, 2,
    20, 103, 159, 41, 51,
    59, 9, 163, 61,
    21, 42, 82, 54, 26, 14, 75,
    9, 28, 66, 7,
    81, 25, 208, 58, 105,
]

print(len(categories), len(pages))
for j in range(len(categories)):
    category = categories[j]
    page = pages[j]
    outfile = open(category + '.csv', 'a+', newline='')
    # outfile = open('Make_Up_and_Cosmetics' + '.csv', 'a+', newline='')
    writer = csv.writer(outfile)
    writer.writerow(["object1", "object2", "phone", "fax", "mobile", "email", "website", "description"])

    for i in range(1, page + 1):
        # filename = 'htmls/Make_Up_and_Cosmetics/Make_Up_and_Cosmetics_' + str(i) + '.txt'
        filename = category + '/' + category + '-' + str(i) + '.txt'
        # breakpoint()
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        # print(filename)
        with open(filename) as file:
            soup = BeautifulSoup(file, "html.parser")
        try:
            html = soup.body.find('div', id='outer')
        # section = html.main.section.main.div
        # breakpoint()
            divclass = html.find('div', class_='catlistblock clearfix').find('div', class_='supp-catlist dv-edit-rc')
            objects = divclass.find_all('div', class_='scat-wrap')
        # print(len(objects))
            for obj in objects:
                object1 = obj.div.find('td', class_="col1").h2.a.text
                object2 = obj.div.find('td', class_="col2").div.address.text
                object3 = obj.div.find('td', class_="col3")
                object4 = obj.div.find('td', class_="col4")
                object5 = obj.div.find('td', class_="col5")
                object6 = obj.div.find('tr', class_="supdetails").td.p.text

                # print(object1)
                # print(object2)

                phone = object3.div.find('p', class_="phone-icon")
                fax = object3.div.find('p', class_="fax-icon")
                mobile = object3.div.find('p', class_="mobile-icon")

                if phone is not None:
                    phone = phone.text
                    # print(phone.text)
                else:
                    phone = "phone"
                    # print("phone")

                if fax is not None:
                    fax = fax.text
                    # print(fax.text)
                else:
                    fax = "fax"
                    # print("fax")

                if mobile is not None:
                    mobile = mobile.text
                    # print(mobile.text)
                else:
                    mobile = "mobile"
                    # print("mobile")

                email = object4.p
                if email is not None:
                    email = email.span.a['href']
                    # print(email.span.a['href'])
                else:
                    email = "email"
                    # print("email")

                website = object5.p
                if website is not None:
                    website = website.span.a['href']
                    # print(website.span.a['href'])
                else:
                    website = "website"
                    # print("website")

                writer.writerow([object1, object2, phone, fax, mobile, email, website, object6])
        except AttributeError:
            continue
        print(i)

    outfile.close()
