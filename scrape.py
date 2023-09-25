import requests
import lxml.html
import yagmail
from typing import NamedTuple
import pandas as pd
import os.path
import numpy as np
from datetime import datetime


class Article(NamedTuple):
    title: str
    url: str


html = requests.get("https://geeksforgeeks.org/trending")
doc = lxml.html.fromstring(html.content)  # created an HtmlElement object
trending_python = doc.xpath('//*[@id="gfg-trending-main-div"]')[0]  # filter div tags that have trending id
href_list = []
titles = []
titles = trending_python.xpath(
    '//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a/p/text()'
)  # extract titles trending tab
hrefs = trending_python.xpath('//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a')
for href in hrefs:
    href_list.append(href.attrib["href"])
articles = []
for title, url in zip(titles, href_list):   # make objects of class Article
    article = Article(title=title, url=url)
    articles.append(article)

#print(articles)
article_filter = ["api", "numpy"]  # words of interest
res = [
    b for b in map(lambda x: x, articles) if any(a in b.title.lower() for a in article_filter)
]  # filter out articles by certain word triggers, can be used for debugging
col_1 = [b for b in map(lambda x: x.title, res)]
col_2 = [b for b in map(lambda x: x.url, res)]

if (os.path.isfile("./GFGArticles.csv")) is False:
    df = pd.DataFrame(columns=["title", "url", "date"])
    df = df.to_csv("GFGArticles.csv", index=False)
df1 = pd.read_csv("GFGArticles.csv",  usecols=['title', 'url', 'date'])
data = {"title": col_1, "url": col_2, "date": str(pd.Timestamp.now().floor('T'))}
df2 = pd.DataFrame(data).astype({"title": object, "url": object})


df3 = pd.merge(df1[['title', 'url']], df2, how='outer', indicator='exists')
df3['exists'] = np.where(df3.exists == 'both', True, False)
df3.to_csv("GFGArticles.csv", index=False)
msg_df = df3[df3['exists'] == False]   # filters out unique entities
if msg_df.empty is False:
    print("here\n", msg_df)
if msg_df.empty is False:
    with open(
            "config.txt", "r"
    ) as f:  # read sender email and password and reciever email from config.txt
        content = [line.strip() for line in f]
    yag = yagmail.SMTP(content[0], content[1])
    yag.send(content[2], 'GEEKSFORGEEKS, Trending in Python', msg_df.iloc[:,:3])
    print("Check Inbox!")


