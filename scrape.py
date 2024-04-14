# Import libraries
import requests
import lxml.html
import yagmail
from typing import NamedTuple, List
import pandas as pd
import os.path
import numpy as np


# Define Article class using NamedTuple
class Article(NamedTuple):
    title: str
    url: str

# Function to parse and filter articles
def parse_and_filter(link: str) -> list['Article']:
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
    titles = trending_python.xpath('//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a/p/text()')

    # Extract URLs of trending articles
    hrefs = trending_python.xpath('//*[@id="gfg-trending-main-div"]/div[5]/div[2]/a')
    href_articles_list = [href.attrib["href"] for href in hrefs]

    # Create Article objects for each title and URL pair
    articles = [Article(title=title, url=url) for title, url in zip(titles, href_articles_list)]

    # Define keywords of interest for filtering
    article_filter = ["file", "django", "game"]

    # Filter articles based on keywords
    article_result = [article for article in articles if any(keyword in article.title.lower() for keyword in article_filter)]
    return article_result


# Function to save articles to CSV
def articles_to_cvs(article_list: list) -> None:
    """
    Saves articles to a CSV file.

    Args:
        article_list (list[Article]): List of articles to save.
    """
    # Code for saving articles to CSV
    # Extract titles and URLs from the article list
    titles_column = [article.title for article in article_list]
    url_column = [article.url for article in article_list]

    # Check if the CSV file already exists; if not, create a new one with a template
    if not os.path.isfile("./GFGArticles.csv"):
        df = pd.DataFrame(columns=["title", "url", "date"])
        df.to_csv("GFGArticles.csv", index=False)

    # Read the existing CSV file into a DataFrame
    dataframe_on_file = pd.read_csv("GFGArticles.csv", usecols=['title', 'url', 'date'])

    # Create a new DataFrame with the updated data
    new_data = {"title": titles_column, "url": url_column, "date": str(pd.Timestamp.now().floor('T'))}
    df_new_data = pd.DataFrame(new_data).astype({"title": object, "url": object, "date": object})

    # Merge the existing DataFrame with the new data
    df_to_file = pd.merge(dataframe_on_file[['title', 'url']], df_new_data, how='outer', indicator='exists')
    df_to_file['exists'] = np.where(df_to_file.exists == 'both', True, False)

    # Save the merged DataFrame to the CSV file
    df_to_file.to_csv("GFGArticles.csv", index=False)

    # Filter out unique entities and send an email if there are new articles
    msg_df = df_to_file[df_to_file.exists == False]
    def feed_to_email() -> None:
        """
        Sends email notifications for new articles.
        """
        with open("config.txt", "r") as f:
            content = [line.strip() for line in f]

        # Send email using yagmail API
        yag = yagmail.SMTP(content[0], content[1])
        yag.send(content[2], 'GEEKSFORGEEKS, Trending in Python', msg_df.iloc[:])
        print("Check Inbox!")

    # Check if there are new articles to notify about
    if len(msg_df.index) != 0:
        feed_to_email()
    else:
        print("No new articles")


    return

# Main function
def main():
    """
    Main function to run the program.
    """
    articles_temp = parse_and_filter("https://geeksforgeeks.org/trending")
    articles_to_cvs(articles_temp)

if __name__ == "__main__":
    main()