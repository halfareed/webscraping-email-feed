import requests
import lxml.html
import yagmail
from typing import NamedTuple, List
import pandas as pd
import os.path
import numpy as np


class Article(NamedTuple):
    title: str
    url: str


def parse_and_filter(link: str) -> list['Article']:
    html = requests.get(link)
    doc = lxml.html.fromstring(html.content)  # created an HtmlElement object
    trending_python = doc.xpath('//*[@id="gfg-trending-main-div"]')[0]  # filter div tags that have trending id
    href_articles_list = []
    titles = trending_python.xpath(
        '//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a/p/text()'
    )  # extract titles trending in python tab
    hrefs = trending_python.xpath('//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a')
    for href in hrefs:
        href_articles_list.append(href.attrib["href"])
    articles = []
    for title, url in zip(titles, href_articles_list):  # make objects of class Article
        article = Article(title=title, url=url)
        articles.append(article)
    article_filter = ["file", "django", "game"]  # words of interest
    article_result = [
        b for b in articles if any(a in b.title.lower() for a in article_filter)
    ]  # filter out articles by certain word triggers, can be used for debugging
    return article_result


def articles_to_cvs(article_list: list) -> None:
    titles_column = [b for b in map(lambda x: x.title, article_list)]
    url_column = [b for b in map(lambda x: x.url, article_list)]
    if (os.path.isfile("./GFGArticles.csv")) is False:
        df = pd.DataFrame(columns=["title", "url", "date"])  # template new database
        df = df.to_csv("GFGArticles.csv", index=False)
    dataframe_on_file = pd.read_csv("GFGArticles.csv", usecols=['title', 'url', 'date'])
    new_data = {"title": titles_column, "url": url_column, "date": str(pd.Timestamp.now().floor('T'))}
    df_new_data = pd.DataFrame(new_data).astype({"title": object, "url": object, "date": object})
    df_to_file = pd.merge(dataframe_on_file[['title', 'url']], df_new_data, how='outer', indicator='exists')
    df_to_file['exists'] = np.where(df_to_file.exists == 'both', True, False)
    df_to_file.to_csv("GFGArticles.csv", index=False)
    msg_df = df_to_file[(df_to_file.exists == False)]   # filters out unique entities

    def feed_to_email() -> None:
        with open(
                "config.txt", "r"
        ) as f:  # read sender email and password and reciever email from config.txt
            content = [line.strip() for line in f]
        yag = yagmail.SMTP(content[0], content[1])
        yag.send(content[2], 'GEEKSFORGEEKS, Trending in Python', (msg_df.iloc[:]))
        print("Check Inbox!")

    if len(msg_df.index) != 0:
        feed_to_email()
    return


articles_temp = parse_and_filter("https://geeksforgeeks.org/trending")
articles_to_cvs(articles_temp)
