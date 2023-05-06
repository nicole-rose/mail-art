import csv


#changing source field to indicate data source
header=["Sender","Addressee","Source"]

with open ("ALL_MAIL.csv","r") as x, open("duplicates_sort.csv","r") as y:
    all = csv.reader(x)
    dup = csv.reader(y)

    for a in all:
        for d in dup:
            if a[0] == d[0]:
                a[2]=d[1]
            if a[1] == d[0]:
                a[2]=d[1] 