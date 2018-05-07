import csv

f = open('20131217.csv','r+')
csv_r = csv.reader(f)
for i in csv_r:
    print(i)
f.close()
