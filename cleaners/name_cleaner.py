import json
import csv
import pandas as pd
import re

###BUFFALO CLEANER####

data = pd.read_json("res/buff_mail.json")

def clean_json(text):
    regex = re.compile("\[(.*)\]")
    clean = regex.findall(f'{text}')
    return clean[0]

clean_names=data["Addressees"].apply(clean_json)
data["Addressees"]=clean_names


###SAIC CLEANER####

#splitting and cleaning names
with open("saic_mail.json", "r") as all_json:
    data = json.load(all_json)

#sender names
for a in data:
    name_parts = a['Sender'].split(', ')
    if len(name_parts) > 1:
        firstname = name_parts[1]
        lastname = name_parts[0]
        new_name = f"{firstname} {lastname}"
    else:
        new_name = name_parts[0]
   
    a['Sender'] = new_name

#addressee names
for b in data:
    name_parts = b['Addressee'].split(', ')
    if len(name_parts) > 1:
        firstname = name_parts[1]
        lastname = name_parts[0]
        new_name = f"{firstname} {lastname}"
    else:
        new_name = name_parts[0]
    b['Addressee'] = new_name
    

#creating updated data document    
field_names=['ID','Sender','Addressee']
with open('said_mail.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()    
    writer.writerows(data)
