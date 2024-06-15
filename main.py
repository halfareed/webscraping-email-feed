"""
This script is the main entry point for a web scraping application.

It fetches articles from the "https://geeksforgeeks.org/trending" URL, filters the articles,
and writes them to a CSV file. If there are new articles, it sends an email notification.

Modules used:
- article_parser: Parses and filters the articles from the provided URL.
- csv_handler: Handles the CSV file operations.
- email_notifier: Sends an email notification if there are new articles.

Functions:
- main: The main function to run the program.
"""

# Import libraries
from src.modules.article_parser import parse_and_filter
from src.modules.csv_handler import articles_to_csv
from src.modules.email_notifier import send_email_notification

# Main function
def main():
    """
    Main function to run the program.
    """
    articles_temp = parse_and_filter("https://geeksforgeeks.org/trending")
    filtered_articles_df = articles_to_csv(articles_temp)
    if len(filtered_articles_df.index):
        send_email_notification(filtered_articles_df)
    else:
        print("No new articles")


if __name__ == "__main__":
    main()
