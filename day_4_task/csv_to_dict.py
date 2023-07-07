import csv
d={}
with open('employee.csv','r') as data:
    value = csv.DictReader(data)
    for i in value:
        k=i['id']
        d[k]=i

find=input("enter key:")
print(d[find])