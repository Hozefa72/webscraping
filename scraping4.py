import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=5b9956f8-ff2e-42f8-8a4c-bc84ebe99dc2&as-searchtext=tv"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r=requests.get(url,headers=headers)
data={"Product":[],"Price":[]}
soup=BeautifulSoup(r.text,'html.parser')
products=soup.select("div._4rR01T")
for product in products:
    data['Product'].append(product.string)
prices=soup.find_all(class_="_30jeq3 _1_WHN1")
for price in prices:
    data['Price'].append(price.get_text())

df=pd.DataFrame(data)
df.to_csv("tvprice.csv",index=False)