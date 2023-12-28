import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.flipkart.com/search?q=iphone&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_6_3_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_3_na_na_na&as-pos=6&as-type=RECENT&suggestionId=iphone&requestId=c94bd4e5-9bee-4d4b-80c9-34dfe4da70d5&as-searchtext=iph"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r=requests.get(url,headers=headers)
data={"Product":[],"price":[]}
soup=BeautifulSoup(r.text,'html.parser')
products=soup.select("div._4rR01T")
for price in products:
    print(price.string)
    data['Product'].append(price.string)
prices=soup.find_all(class_="_30jeq3 _1_WHN1")
for price in prices:
    print(price.get_text())
    data['price'].append(price.get_text())
df=pd.DataFrame(data)
df.to_csv("Iphonedetail.csv",index=False)