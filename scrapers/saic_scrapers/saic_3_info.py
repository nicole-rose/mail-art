import cloudscraper
import time
from bs4 import BeautifulSoup
import json
import csv

base_url = "https://digitalcollections.saic.edu"

mail_info=[]
fails=[]

with open("pages_skips", "r") as pgs_json:
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
    number_info = soup2.find('div',{'class': 'field field--name-field-local-identifier field--type-string field--label-above'})
    if number_info is not None:
        id_num = number_info.find('div',{'property':'dcterms:identifier'}).text.strip()
        print(f"pageID: {id_num}")
        print(f"page {index}/397")
    else:
        fails.append({'error':'ID tag','page':work_url,'action':"Skipped"})
        print(f"page {index}/397")
        print(f"FAILED page {page}")
        print('================================')
        continue

#SENDER
    creator_info = soup2.find('div', {'class': 'field field--name-field-primary-creator field--type-typed-relation field--label-above'})
    if creator_info is not None:
        cr = creator_info.find('a')
        creator=cr.text.strip()
    else:
        fails.append({'error':'No Primary Creator','page':work_url,'action':"Noted"})
        print("creators: 0")
        creator=[]


#ADDRESEE
    res=[]
    addressee_info=soup2.find('div', {'class': 'field field--name-field-linked-agent field--type-typed-relation field--label-above'})
    if addressee_info is not None:
        if "Contributor:" in addressee_info.text:
            fails.append({'error':'Contributor in Addressee','page':work_url,'action':"Skipped"})
            print(f"page {index}/397")
            print(f"FAILED page {page}")
            print('===============================')
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


with open('saic_mail2.json', 'w') as write_file:        
    json.dump(mail_info, write_file, indent = 2)

with open("pages_failed_2", "w") as failed_json:
    json.dump(fails, failed_json,indent = 2)

print(len(fails))
print('all done')