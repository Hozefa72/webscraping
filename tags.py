import requests
from bs4 import BeautifulSoup
with open("sample.html","r") as f:
    html_doc=f.read()
    
soup=BeautifulSoup(html_doc,"html.parser")
# print(soup.prettify())
# print(soup.title,type(soup.title))
# print(soup.div.string)
# print(soup.find_all("div"))
# for link in soup.find_all("a"):
#     print(link.get("href"))
#     print(link.get_text())
# print(soup.find_all(id="link3"))
# print(soup.select("div.Italic"))
# print(soup.select("span#Italic"))
# print(soup.span.get("class"))
# for child in soup.find(class_="container").children:
#     print(child)
# i=0
# for parent in soup.find(class_="box").parents:
#     i+=1
#     print(parent)
#     if(i==2):
#         break
# cont=soup.find(class_="container")
# cont.name="span"
# cont['class']="myclass class2"
# cont.string="I want to become a Data Scientist"
# print(cont)
# ultag=soup.new_tag('ul')
# litag=soup.new_tag('li')
# litag.string="Hozefa"
# ultag.append(litag)

# litag=soup.new_tag('li')
# litag.string="Nazima Mera Dost hai"
# ultag.append(litag)
# soup.html.body.insert(0,ultag)
# with open("modified.html","w") as f:
#     f.write(str(soup))
# s=soup.find(class_="container")
# print(s.has_attr('contenteditable'))
def has_class_but_noid(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

def has_content(tag):
    return tag.has_attr("content")
# results=soup.find_all(has_class_but_noid)
results=soup.find_all(has_content)
for result in results:
    print(result,"\n\n")