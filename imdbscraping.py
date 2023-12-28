import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
a=np.arange(1,264)
a=map(str,a)
a=list(a)
data={'Movies':[],'Rating':[],'Year':[],'Runtime':[]}
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())
i=0
movies=soup.select("h3.ipc-title__text")
for movie in movies:
       if(movie.string!=None):
        if(movie.string.startswith(a[i],0)):
                data['Movies'].append(movie.string)
                i+=1
ratings=soup.find_all(class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")
for rating in ratings:
        data['Rating'].append(rating.get_text())
years=soup.find_all(class_="sc-14dd939d-6 kHVqMR cli-title-metadata-item")
for y in years:
    if(len(y.string)==4):
        data['Year'].append(y.string)
runtimes=soup.find_all(class_="sc-14dd939d-6 kHVqMR cli-title-metadata-item")
for run in runtimes:
    if(run.string.endswith('m')):
        data['Runtime'].append(run.string)
    elif(run.string.endswith('h')):
        data['Runtime'].append(run.string) 
       
df=pd.DataFrame(data)
df.to_csv("imdb.csv",index=False)
