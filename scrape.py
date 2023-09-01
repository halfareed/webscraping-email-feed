import requests
import lxml.html
import yagmail
from typing import NamedTuple
import pandas as pd
import os.path

from datetime import datetime


class Article(NamedTuple):
    title: str
    url: str


html = requests.get("https://geeksforgeeks.org/trending")
doc = lxml.html.fromstring(html.content)  # created an HtmlElement object
trending_python = doc.xpath('//*[@id="gfg-trending-main-div"]')[
    0
]  # filter div tags that have trending id
href_list = []
titles = []
titles = trending_python.xpath(
    '//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a/p/text()'
)  # extract titles trending tab
hrefs = trending_python.xpath('//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a')
for href in hrefs:
    href_list.append(href.attrib["href"])
articles = []
for title, url in zip(titles, href_list):
    article = Article(title=title, url=url)
    articles.append(article)
article_filter = ["SQLAlchemy", "binary"]  # words of interest
res = [
    b for b in map(lambda x: x, articles) if any(a in b.title for a in article_filter)
]  # filter out articles by certain word triggers

with open(
    "config.txt", "r"
) as f:  # read sender email and password and reciever email from config.txt
    content = [line.strip() for line in f]

if (os.path.isfile("./GFGArticles.csv")) is False:
    df = pd.DataFrame(columns=["title", "url"])
    df = df.to_csv("GFGArticles.csv", index=False)
col_1 = [b for b in map(lambda x: x.title, res)]
col_2 = [b for b in map(lambda x: x.url, res)]
df = pd.read_csv("GFGArticles.csv")
data = {"title": col_1, "url": col_2, "date": pd.Timestamp.now()}
df = pd.DataFrame(data)
df['date'] = df['date'].dt.floor('T')
df.to_csv("GFGArticles.csv", mode="a", header=False, index=False)
print(df)
# df.to_csv('GFGArticles.csv', mode='a', header=False)


# yag = yagmail.SMTP(content[0], content[1])
# msg = '\n'.join(map(str, res))
# yag.send(content[2], 'Trending in Python, GEEKSFORGEEKS', msg)
