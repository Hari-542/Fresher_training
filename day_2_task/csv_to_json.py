import csv
import json 

source_path=input("Enter csv file path:")
destination_path=input("Enter json file path:")

with open(source_path,'r') as file:
    f=list(csv.DictReader(file))
    with open(destination_path,'w') as f1:
        json.dump(f,f1,indent=4)
