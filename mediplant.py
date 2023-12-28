import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url="https://bsi.gov.in/page/en/medicinal-plant-database"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.text,"html.parser")
data={"plant_name":[]}
plants=soup.find_all(class_="MsoNormal")
k=0
for i in plants:
    data['plant_name'].append(i.text)
df=pd.DataFrame(data)
df.to_csv("medical_plant.csv",index=False)
