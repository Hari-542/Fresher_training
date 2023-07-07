import requests
import pandas as pd
import json

api_url = "http://api.coincap.io/v2/assets"
response = requests.get(api_url) 
response=response.json()['data']
with open ('hello.json','w') as k:
    json.dump(response,k)
data=pd.read_json('hello.json')
data.to_csv('file.csv')