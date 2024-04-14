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
