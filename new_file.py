from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib
import time
from selenium import webdriver

browser = webdriver.Firefox(executable_path="./geckodriver")

filename = "practicewebsitedata/ism/"  + '.txt'

lst=[]
try:
    with open(filename) as file:
        soup = BeautifulSoup(file, "html.parser")
        print(type(soup))
    items = soup.find_all('li', class_="article-company card card--1dp vcard")
    # breakpoint()
    count=0
    # print(items)
    item=items[0]
    link = item.find('a', class_="company-name display-spinner")['href']
    browser.get(link)
    cookies=browser.find_element_by_id("cookiescript_accept")
    
    cookies.click()
    time.sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # soup = soup.prettify()
    companyName = item.find('a', class_="company-name display-spinner")['title']
    # companyDetails = soup.find('a', class_="ep-epages-home-links__websites")['href']
    print(type(soup))
    # ep-epages-home-links__websites
    # companyWebsite = soup.find('a', class_="ep-epages-home-link-card v-card v-sheet v-sheet--outlined theme--light pa-4 ep-epages-home-website-link v-card v-card--link v-sheet theme--light")['href']
    # ep-epage-sidebar__website-button v-btn v-btn--block v-btn--has-bg theme--light v-size--default
    # print(soup)
    
    # breakpoint()
    button = browser.find_element_by_class_name("ep-epage-sidebar__phone-button.v-btn.v-btn--block.v-btn--has-bg.theme--light.v-size--default")
    button.click()

    time.sleep(1)
# ep-epage-phone-popup-number__button-text"
    # breakpoint()
    display_button=browser.find_element_by_class_name("ep-epage-phone-popup-number__button.v-btn.v-btn--block.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default")    
    display_button.click()

    time.sleep(1)


    grt_n=browser.find_element_by_class_name("ep-epage-phone-popup-number__button-text").text
    print(grt_n)
    # breakpoint()
   # breakpoint()

    # btn_onlclick_list = [a.get('onclick') for a in soup.find_all('button')]
    # print(btn_onlclick_list)
    # companyContact=soup.find_element_by_class_name("ep-epage-sidebar__phone-button v-btn v-btn--block v-btn--has-bg theme--light v-size--default")
    # driver.find_element_by_class_name
    # companyContact=soup.find('button',class_="ep-epage-sidebar__phone-button v-btn v-btn--block v-btn--has-bg theme--light v-size--default")
    # print(companyContact)
    # d=companyContact.find_element_by_class_name("ep-epage-sidebar__phone-button v-btn v-btn--block v-btn--has-bg theme--light v-size--default")

    # print(d)
    filename = "practicewebsitedata/ism/" + "2"+ '.txt'

    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, 'w+') as file:
        file.write(str(soup))
    file.close()
    # print((w+30)/20)
    print(companyName)
    # print(companyDetails)
    print(companyWebsite)
    file.close()
#     for item in items:

#     #     print(item)
#         # breakpoint()
#         try:

#             link = item.find('a', class_="company-name display-spinner")['href']
#             browser.get(link)
#             html = browser.page_source

#             soup = BeautifulSoup(html, 'html.parser')
#             soup = soup.prettify()
#             print(count)
#             # filename = "practicewebsitedata/ism/"  +'{}.txt'.format(count)
#             count=count+1
#             # companyName = item.find('a', class_="company-name display-spinner")['title']

#             # print(soup)
#             # soup1 = BeautifulSoup(soup, "html.parser")
#             # companyName = soup1.find('header', class_="ep-epages-header")['alt']
#             r=requests.get(link, headers=headers)
#             print(r)
#             # print(companyName)
#             if count==1:
#                 print("inside")
#                 break
#             else:
#                 print("Outside")
#             breakpoint()
#             print(filename)
#         #     print(os.path.exists(os.path.dirname(filename)))
#         #     if not os.path.exists(os.path.dirname(filename)):
#         #         try:
#         #             os.makedirs(filename)
#         #         except OSError as exc:  # Guard against race condition
#         #             if exc.errno != errno.EEXIST:
#         #                 raise
                

#         #         with open(filename, 'w+') as file:
#         #             file.write(str(soup))
#         #     file.close()
#         #     lst.append(link)
#         # except:
#         #     lst.append(None)
#         #     website = "website"
#         except:
#             print(None)
#     # print(lst)
except FileNotFoundError:
    print("changing category from ")
browser.close()
