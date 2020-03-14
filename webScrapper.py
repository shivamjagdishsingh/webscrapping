from bs4 import BeautifulSoup
import csv

outfile = open('asda_webscrapped_data.csv', 'w', newline='')
writer = csv.writer(outfile)
writer.writerow(["object_name", "object_image_link", "object_link", "object_price"])

with open('scraped_asda.txt') as file:
    soup = BeautifulSoup(file, "html.parser")

html = soup.body.find('div', id='root')
section = html.main.section.main.div

divclass = section.find('div', class_='co-lazy-product-container').find('div', class_='co-product-list').ul
# print(divclass)

objects = divclass.find_all('li', class_='co-item')

# print(len(objects))
count = 0
for obj in objects:
    count += 1
    object1 = obj.div.find('div', class_="co-item__col1")
    object2 = obj.div.find('div', class_="co-item__col2")
    object3 = obj.div.find('div', class_="co-item__col3")
    object_name = object1.button.img['alt']
    object_image_link = object1.button.img['src']
    object_link = "groceries.asda.com" + object2.a['href']
    object_price = object3.strong.string
    print("name", object_name, 'image link', object_image_link, "object link", object_link, "object price",
          object_price)
    writer.writerow([object_name, object_image_link, object_link, object_price])
print(count)

outfile.close()
