import cloudscraper
import time
from bs4 import BeautifulSoup
import json

#list of pages to visit
pages = []

base_url = "https://digitalcollections.saic.edu"

index = 0
while index < 55:
    print(f"visiting page: {index}")
    initial_page = "/islandora/object/islandora%3Acamac"
    initial_url = f"{base_url}/{initial_page}"
    url_params = {"page": index, "items_per_page": 50}

    scraper = cloudscraper.create_scraper()
    page = scraper.get(initial_url, params=url_params, timeout=30)
    print(f"status code: {page.status_code}")
    soup = BeautifulSoup(page.text, "html.parser")

    art = soup.find_all('div', {'class': 'node__title'})
    for obj in art:
        link = obj.find('a')
        pages.append(link['href'])
    print(f"so far, collected: {len(pages)} pages")
    print('=================================')
    index += 1

print(f"final page count:{len(pages)} pages")
print("links done")

with open("saic_pages_all", "w") as pgs_json:
    json.dump(pages, pgs_json)

print("pages saved")