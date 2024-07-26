GeeksForGeeks Trending Articles Scraper

The GeeksForGeeks Trending Articles Scraper is a Python script designed to extract trending articles related to Python programming from the GeeksForGeeks website. It provides a convenient way to stay updated with the latest and most popular articles in the Python community.
Features


    Scrapes trending articles from the GeeksForGeeks website.
    Saves articles to a CSV file for easy access and analysis.
    Sends email notifications for new articles using yagmail.
    Customizable configuration for email settings and article filtering.
    
Project Structure

    models.py: Contains the Article class used to represent articles.
    article_parser.py: Handles parsing and filtering articles from GeeksForGeeks.
    csv_handler.py: Manages saving articles to a CSV file.
    email_notifier.py: Handles sending email notifications for new articles.

Installation

    Clone the repository:
    git clone https://github.com/halfareed/webscraping-email-feed.git

Usage

    Update the .env file with necessary credentials.
    Run the main script to scrape and save trending articles:

    python main.py

Dependencies

Install these dependencies using the provided requirements.txt file.

    cd webscraping-email-feed
    pip install -r requirements.txt

Configuration using .env

1. **Create a .env File**:
   Create a `.env` file in the root directory with the following variables:
   ```env
   SENDER_EMAIL=your-email@example.com
   SENDER_PASSWORD=your-email-password
   RECIPIENT_EMAIL=recipient-email@example.com
   FIRST_KEYWORD=
   SECOND_KEYWORD=
   THIRD_KEYWORD=

Contributing

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request on GitHub.
License

This project is licensed under the MIT License. See the LICENSE file for details.
