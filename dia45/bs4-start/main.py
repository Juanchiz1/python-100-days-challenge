from bs4 import BeautifulSoup
import lxml

with open ("website.html") as file:
    contents=file.read()

soup=BeautifulSoup(contents,'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)

all_anchor_tags=soup.find_all(name="a")


for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get('href'))


heading=soup.find_all(name="h1",id="name")

import requests

response=requests.get(url="https://news.ycombinator.com/news")
yc_web_page=response.text
soup=BeautifulSoup(yc_web_page,'html.parser')
article_tag=soup.find(name="a",class_="storylink")
print(article_tag.getText())