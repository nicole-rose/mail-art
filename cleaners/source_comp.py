import csv

A=[]
B=[]
C=[]
dup_list=[]
nodes_list=[]

header=["Name","Source"]

#creating list of all names in each source
with open ("ama_mail.csv", "r") as am, open("buff_mail.csv", "r") as buf, open("saic_mail.csv", "r") as sac, open ("ALL_MAIL.csv", "r") as all:
    data_A = csv.reader(am)
    data_B = csv.reader(buf)
    data_C = csv.reader(sac)
    data_all=csv.reader(all)

    for a in data_A:
        if a[0] not in A:
            A.append(a[0])
        if a[1] not in A:
            A.append(a[1])

    for b in data_B:
        if b[0] not in B:
            B.append(b[0])
        if b[1] not in B:
            B.append(b[1])

    for c in data_C:
        if c[0] not in C:
            C.append(c[0])
        if c[1] not in C:
            C.append(c[1])

#creating list of names that appear in multiple sources
    with open('duplicates.csv', 'w') as file:
        dups = csv.writer(file)
        dups.writerow(header)

        for ax in A:
            for bx in B:
                if ax == bx:
                    dups.writerow([ax,"AB"])
                    dup_list.append(ax)

        for az in A:
                for cx in C:
                    if az == cx:
                        dups.writerow([az,"AC"])
                        dup_list.append(az)

        for bz in B:
                for cz in C:
                    if cz == bz:
                        dups.writerow([cz,"BC"])
                        dup_list.append(cz)

#creating list of unique names
    with open("_nodes.csv","w") as file2:
        nodes=csv.writer(file2)

        for aa in A:
            if aa not in dup_list:
                nodes.writerow([aa,"A"])
        for bb in B:
            if bb not in dup_list:
                nodes.writerow([bb,"B"])
        for cc in C:
            if cc not in dup_list:
                nodes.writerow([cc,"C"])