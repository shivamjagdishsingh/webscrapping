def fuckme():
    print("fuck this world")




def fetch_htmlData(title,href_link):
    # browser = webdriver.Firefox(executable_path="./geckodriver")

    # filename = "practicewebsitedata/ism/"  + '.txt'

    lst=[]
    try:
        # with open(filename) as file:
        browser.get(scrapped_page['href'])
        html = browser.page_source
        soup = BeautifulSoup(href_link, "html.parser")
            # print(type(soup))
        items = soup.find_all('li', class_="article-company card card--1dp vcard")
        count=0
        temp_list=[]
        # print(len(items))
        for item in items:

            link = item.find('a', class_="company-name display-spinner")['href']
            
            browser.get(link)
            try:
                cookies=browser.find_element_by_id("cookiescript_accept")
            
                cookies.click()
                time.sleep(2)
            except:
                print("error")
            html = browser.page_source
            
            soup = BeautifulSoup(html, 'html.parser')
            companyName = item.find('a', class_="company-name display-spinner")['title']
            print(companyName)
            try:
                button = browser.find_element_by_class_name("ep-epage-sidebar__phone-button.v-btn.v-btn--block.v-btn--has-bg.theme--light.v-size--default")
                button.click()

                time.sleep(2)
            # ep-epage-phone-popup-number__button-text"
                # breakpoint()
                display_button=browser.find_element_by_class_name("ep-epage-phone-popup-number__button.v-btn.v-btn--block.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default")    
                display_button.click()

                get_no=browser.find_element_by_class_name("ep-epage-phone-popup-number__button-text").text

                time.sleep(3)
            except:
                get_no=None
            try:
                companyWebsite = soup.find('a', class_="ep-epage-sidebar__website-button v-btn v-btn--block v-btn--has-bg theme--light v-size--default")['href']
                
            except:
                companyWebsite=None
                
            # companyContact=soup.find('button',class_="ep-epage-sidebar__phone-button.v-btn.v-btn--block.v-btn--has-bg.theme--light.v-size--default::before")
            
            # # companyContact=soup.find('span',class_="v-icon notranslate mdi mdi-magnify theme--light")
            # print(companyContact)
            # d=companyContact.click()
            # print(d)
            # filename = "practicewebsitedata/ism/" + "2"+ '.txt'

            # if not os.path.exists(os.path.dirname(filename)):
            #     try:
            #         os.makedirs(os.path.dirname(filename))
            #     except OSError as exc:  # Guard against race condition
            #         if exc.errno != errno.EEXIST:
            #             raise
            # with open(filename, 'w+') as file:
            #     file.write(str(soup))
            # file.close()
            # print((w+30)/20)
            # print(companyName)
            # print(companyDetails)
            print(companyWebsite)
            print(get_no)
            temp_list.append([title,link,companyName,companyWebsite,get_no])
        file.close()
        df=pd.DataFrame(temp_list,columns=["Title","Link", "CName","CWebsite","Contact_N"])
        filename = "practicewebsitedata/ism/"  + 'df.csv'
        # if not os.path.exists(os.path.dirname(filename)):
        #     try:
        #         os.makedirs(os.path.dirname(filename))
        #     except OSError as exc:  # Guard against race condition
        #         if exc.errno != errno.EEXIST:
        #             raise
        # with open(filename, 'w+') as file:
        #     file.write(str(soup))
        # file.close()   
        df.to_csv("practicewebsitedata/ism/multiscrapped.csv")
    except FileNotFoundError:
        print("changing category from ")
    browser.close()
