import cloudscraper
from bs4 import BeautifulSoup
import json
import csv


base_url="https://www.aaa.si.edu/search/collections?edan_q=Mail%20art&edan_fq[1]=object_type:%22Correspondence%22&edan_fq[2]=p.edanmdm.descriptivenonrepeating.record_id:AAADCD_item_*&stype=search-collections"

#getting titles
titles=[]
index = 0
while index < 12:
    url_params = {"page": index}

    scraper = cloudscraper.create_scraper()
    page = scraper.get(base_url, params=url_params)
    soup = BeautifulSoup(page.text, "html.parser")

    results = soup.find('ul', {'class': 'edan-rows'})
    resa = results.find_all('h3',{'class':'title'})
    for obj in resa:
        titles.append(obj.text.strip())
    index += 1

print("titles done")
print(len(titles))

#splitting titles
mail_info={}
matcher1 = "mail art to"
matcher2 = "Mail art to"

index_a=0
while index_a < len(titles):
    for x in titles:
        if matcher2 in x or matcher1 in x:
            y = x.split("mail art to", 1)
            a=(y[0].strip())
            b=(y[1].strip())
            s=(a.split(","))
            r=(b.split(","))
            sender=s[0]
            rec=r[0]
            mail_info[index_a]={'Sender':sender, "Addressees":rec}
        index_a+=1

#results as JSON
with open(f'res/{"ama_mail"}.json', 'w') as write_file:        
    json.dump(mail_info, write_file, indent = 2)

#results as CSV
field_names=['Sender','Addressees']
with open('ama_mail.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()    
    writer.writerows(mail_info)

print("mail info done")