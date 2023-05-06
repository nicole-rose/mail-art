import cloudscraper
from bs4 import BeautifulSoup
import json
import csv

base_url = "https://digitalcollections.saic.edu"

#getting info

mail_info=[]
fails=[]

with open("saic_pages_all", "r") as pgs_json:
    res_pages = json.load(pgs_json)

index=0
for page in res_pages:
    index+=1    
    scraper2 = cloudscraper.create_scraper()
    work_url = f"{base_url}{page}"
    print(page)
    page2 = scraper2.get(work_url)
    print(f"status code: {page2.status_code}")
    soup2 = BeautifulSoup(page2.text, 'html.parser')

#ID NUMBER
    number_info = soup2.find('span',{'class': 'views-field views-field-field-local-identifier'})
    if number_info is not None:
        id_num = number_info.find('span',{'class':'field-content'}).text.strip()
        print(f"pageID: {id_num}")
        print(f"page {index}/2682")
    else:
        fails.append({'error':'ID tag','page':work_url,'action':"Skipped"})
        print(f"page {index}/2682")
        print(f"FAILED page {page}")
        print('================X================')
        continue

#SENDER
    creator_info = soup2.find('div', {'class': 'views-field views-field-field-primary-creator'})
    if creator_info is not None:
        cr = creator_info.find('a')
        creator=cr.text.strip()
    else:
        fails.append({'error':'No Primary Creator','page':work_url,'action':"Noted"})
        print("creators: 0")
        creator=[]


#ADDRESEE
    res=[]
    addressee_info=soup2.find('span', {'class': 'views-field views-field-field-linked-agent'})
    if addressee_info is not None:
        if "Contributor:" in addressee_info.text:
            fails.append({'error':'Contributor in Addressee','page':work_url,'action':"Skipped"})
            print(f"page {index}/2682")
            print(f"FAILED page {page}")
            print('===============X=================')
            continue
        else:
            addressees = addressee_info.find_all('a')
            print(f"addressees: {len(addressees)}")
            a_index=0
            for a in addressees:
                a_index+=1
                res.append(a.text.strip())
                mail_info.append({'ID':id_num,'Sender':creator,'Addressee':a.text.strip()})
                print(f"{a_index}/{len(addressees)}")
    else:
        fails.append({'error':'No Addressees','page':work_url,'action':"Noted"})
        print("addressees: 0")
        mail_info.append({'ID':id_num,'Sender':creator,'Addressee':[]})
    print("all appended")
    print('=================================')

#results as JSON
with open('saic_mail.json', 'w') as write_file:        
    json.dump(mail_info, write_file, indent = 2)

#failed pages
with open("fails", "w") as failed_json:
    json.dump(fails, failed_json,indent = 2)

#results as CSV
field_names=['ID','Sender','Addressees']
with open('saic_mail.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()    
    writer.writerows(mail_info)

print(len(fails))
print('all done')