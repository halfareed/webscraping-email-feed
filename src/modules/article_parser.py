# Define Article class using NamedTuple
import re
from typing import NamedTuple
import lxml.html
import requests


class Article(NamedTuple):
    title: str
    url: str


# Function to parse and filter articles
def parse_and_filter(link: str, *args: list) -> list["Article"]:
    """
    Parses and filters articles based on keywords.

    Args:
            link (str): The URL to parse and filter.

    Returns:
            list[Article]: List of filtered articles.
    """
    # Fetch HTML content from the provided link
    html = requests.get(link)

    # Create an HtmlElement object from the HTML content
    doc = lxml.html.fromstring(html.content)

    # Locate the div element with the trending ID
    trending_python = doc.xpath('//*[@id="gfg-trending-main-div"]')[0]

    # Extract titles of trending articles in the Python tab
    titles = trending_python.xpath(
        '//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a/p/text()'
    )

    # Extract URLs of trending articles
    hrefs = trending_python.xpath('//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a')
    href_articles_list = [href.attrib["href"] for href in hrefs]

    # Create Article objects for each title and URL pair
    articles = [
        Article(title=title, url=url) for title, url in zip(titles, href_articles_list)
    ]

    # Define keywords of interest for filtering
    article_filter = re.findall(r'\w+', open('src/tests/config/config.txt', 'r').readline())


    # Filter articles based on keywords
    article_result = [
        article
        for article in articles
        if any(keyword in article.title.lower() for keyword in article_filter)
    ]
    return article_result