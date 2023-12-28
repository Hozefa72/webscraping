import requests
def getchsavefile(url,path):
    r=requests.get(url)
    with open(path,"w",encoding="utf-8") as f:
        f.write(r.text)
url="https://www.amazon.in/b?node=1389402031&pf_rd_r=Z917KZ7SZVGVY3JZGGTZ&pf_rd_p=0ce563a5-4418-4703-9319-a38b386a9695&pd_rd_r=8b086cd1-5366-47c0-bb8a-6f9b3600f1ee&pd_rd_w=SKreX&pd_rd_wg=7bKuN"
getchsavefile(url,"data/amazon.html")
# r=requests.get(url)
# print(r.text)