from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib

categories = [
    # 3, ]
5, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 23, 24]

for category in categories:
    outfile = open(str(category) + '.csv', 'a+', newline='')

    writer = csv.writer(outfile)
    writer.writerow(
        ["name", "location", "products", "profile", "products_link", "website", "telephone"])

    for i in range(1, 1000):

        filename = "Esources/International/Htmls/" + str(category) + '/' + str(i) + '.txt'
        # breakpoint()
        file = pathlib.Path(filename)
        if not file.exists():
            # try:
            #     os.makedirs(os.path.dirname(filename))
            # except OSError as exc:  # Guard against race condition
            print("changing category")
            break
            # if exc.errno != errno.EEXIST:
            #     raise

        # print(filename)
        with open(filename) as file:
            soup = BeautifulSoup(file, "html.parser")
        try:
            html = soup.body.find('div', id='spread-maincol')
            odd_row = html.findAll('div', class_='row odd clearfix')
            even_row = html.findAll('div', class_='row odd clearfix')
            rows = []
            rows.extend(odd_row)
            rows.extend(even_row)

            for row in rows:
                name = row.div.div.h2.a.text.strip('\n ')
                location = row.div.div.p.text.strip('\n\n[] ')
                products = row.div.find('p', class_='clearp').text.strip('\n Products: … ,')
                profile = row.div.find('p', class_='justify').em.next_sibling.strip('\n :')
                try:
                    products_link = row.div.find('p', class_='justify').span.a['href']
                except:
                    products_link = "products_link"
                try:
                    website = row.div.find('p', class_='justify').span.find('a', class_='bold')['href']
                except:
                    website = "website"
                try:
                    telephone = row.div.find('p', class_='justify').span.span.next_sibling.strip(
                        '\n (quoting eSources)')
                except:
                    telephone = "telephone"
                writer.writerow([name, location, products, profile, products_link, website, telephone])
                print(len([name, location, products, profile, products_link, website, telephone]))
        except AttributeError:
            print("issue")
            continue
        # print(i)

    outfile.close()
