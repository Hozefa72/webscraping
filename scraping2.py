import requests 
from bs4 import BeautifulSoup
import pandas as pd
data={'Product':[],'Price':[]}
url="https://www.amazon.in/s?k=laptop&crid=1HVPZP26VB6ON&sprefix=laptop%2Caps%2C350&ref=nb_sb_noss_1"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())
products=soup.select("span.a-size-medium.a-color-base.a-text-normal")
for product in products:
    data['Product'].append(product.string)

prices=soup.select("span.a-price-whole")
for price in prices:
    data['Price'].append(price.get_text())
    if(len(data['Price'])==len(data['Product'])):
        break
print(data)
# df=pd.DataFrame.from_dict(data)
# df.to_csv("laptopprice.csv",index=False)