"""Module providing a function to save a cvs file of the filtered articles."""

import os

import numpy as np
import pandas as pd


def articles_to_csv(article_list: list):
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
    dataframe_on_file = pd.read_csv("GFGArticles.csv", usecols=["title", "url", "date"])

    # Create a new DataFrame with the updated data
    new_data = {
        "title": titles_column,
        "url": url_column,
        "date": str(pd.Timestamp.now().floor("min")),
    }
    df_new_data = pd.DataFrame(new_data).astype({"title": str, "url": str, "date": str})

    # Merge the existing DataFrame with the new data
    df_to_file = pd.merge(
        dataframe_on_file[["title", "url"]],
        df_new_data,
        how="outer",
        indicator="new",
    )
    df_to_file["new"] = np.where(df_to_file.new == "both", True, False)

    # Save the merged DataFrame to the CSV file
    df_to_file.to_csv("GFGArticles.csv", index=False)
    # Filter out unique entities and send an email if there are new articles
    msg_df = df_to_file.loc[
        (df_to_file["date"].notnull()) & (df_to_file["new"] == False)
    ]
    return msg_df
