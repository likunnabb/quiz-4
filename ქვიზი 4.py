import requests
import csv
from bs4 import BeautifulSoup
import time

for numb in range(1, 8):

    result = requests.get(f'https://biblusi.ge/products?category=402&page={numb}')

    # print(result.text)

    soup = BeautifulSoup(result.text, 'html.parser')

    item_container = soup.find('div', class_='row')

    all_items = item_container.find_all('div', class_='mb-1_875rem col-sm-4 col-md-3 col-xl-2 col-6')

    information = []

    for item in all_items:
        price = item.find("div", class_="text-primary font-weight-700").text
        name = item.acronym.text

        information.append((price, name))
        time.sleep(15)


with open('konteineri.csv', 'w', encoding="utf-8_sig", newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in information:
        writer.writerow([row[0], row[1]])