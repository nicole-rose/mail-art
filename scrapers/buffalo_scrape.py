import cloudscraper
import re
from bs4 import BeautifulSoup
import json
import csv

base_url = 'https://digital.lib.buffalo.edu/'
coll_url= "/items/browse?collection=2"

pages = []
mail_info={}

#list of pages to visit
index = 1
while index < 3:
    initial_url = f"{base_url}{coll_url}"
    url_params = {"page": index}

    scraper = cloudscraper.create_scraper()
    page = scraper.get(initial_url, params=url_params)
    soup = BeautifulSoup(page.text, "html.parser")

    results = soup.find('div', {'class': 'search-results'}, 'a')
    resa = results.find_all('a',{'class':'permalink'})
    for obj in resa:
        pages.append(obj['href'])
    index += 1
print("links done")

#getting info
for page in pages:
    
    scraper2 = cloudscraper.create_scraper()
    work_url = f"{base_url}{page}"
    page2 = scraper2.get(work_url)
    soup2 = BeautifulSoup(page2.text, 'html.parser')

    title_info = soup2.find('div', {'id': 'dublin-core-title'})
    if title_info is not None:
        title=title_info.find('div', {'class':'element-text'}).text.strip() 

    creator_info = soup2.find('div', {'id': 'dublin-core-creator'})
    if creator_info is not None:
        creator=creator_info.find('div', {'class':'element-text'}).text.strip() 

    recs =[]
    con_info = soup2.find('div', {'id': 'dublin-core-contributor'})
    cons = con_info.find_all('div', {'class':'element-text'})
    for c in cons:
        recs.append(c.text.strip())
    for rc in recs:
        z = re.match("Recipient", rc)
        if z:
            recipient = re.sub("Recipient: ",'',rc)
    
    mail_info[title] = {'Title':title,'Sender':creator,'Addressees':recipient}

#results as JSON file
with open(f'res/{"buff_mail"}.json', 'w') as write_file:        
    json.dump(mail_info, write_file, indent = 2)

#results as CSV file
field_names=['Title','Sender','Addressees']
with open('buff_mail.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()    
    writer.writerows(mail_info)

print('all done')