import requests
from bs4 import BeautifulSoup
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}
url="https://www.amazon.in/s?k=iphone+14&crid=3UJXHXPUVD56H&sprefix=ip%2Caps%2C432&ref=nb_sb_ss_ts-doa-p_1_2"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.text,"html.parser")
print(soup.prettify())
spans=soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices=soup.select("span.a-price")
for span in spans:
    print(span.string)
# for price in prices:
#     print("Hi")
