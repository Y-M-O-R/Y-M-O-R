import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/'
response = requests.get(url)
doc = BeautifulSoup(response.text, 'html.parser')

a = doc.find_all('a')
a_tag = []
title_tag = []
for i in range(len(a)):
    # print(a[i].text.strip())
    a_tag.append(a[i].text.strip())

title = doc.find_all('title')

for i in range(len(title)):
    # print(title[i].text.strip())
    title_tag.append(title[i].text.strip())
with open(r'practice_csv_dir\WebScraper.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
with open(r'practice_csv_dir\WebScraper.csv', 'a') as file:
    csv_writer = csv.DictWriter(file, fieldnames=['a', 'title'])
    csv_writer.writeheader()
    for i in a_tag :
        pass
        # csv_writer.writerow({'a': i, "title": })
