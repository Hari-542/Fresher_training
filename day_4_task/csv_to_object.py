import csv

class Employee():
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    def myfunc(temp):
        obj = []
        obj.append([temp.id,temp.name,temp.salary])
        for i in obj:
            print(*i)
with open('employee.csv','r') as data:
    value = csv.DictReader(data)
    for item in value:
        temp = Employee((item['id']),item['ename'],(item['salary']))
        temp.myfunc()