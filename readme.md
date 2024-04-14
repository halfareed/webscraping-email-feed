GeeksForGeeks Trending Articles Scraper

This Python script scrapes trending articles from the GeeksForGeeks website and saves them to a CSV file. It also sends email notifications for new articles.
Introduction

The GeeksForGeeks Trending Articles Scraper is a Python script designed to extract trending articles related to Python programming from the GeeksForGeeks website. It provides a convenient way to stay updated with the latest and most popular articles in the Python community.
Features

    Scrapes trending articles from the GeeksForGeeks website.
    Saves articles to a CSV file for easy access and analysis.
    Sends email notifications for new articles using yagmail.
    Customizable configuration for email settings and article filtering.

Installation

    Clone the repository:

    shell

    git clone https://github.com/your-username/geeksforgeeks-trending-scraper.git


Requirements

    pip install -r requirements.txt

Usage

    Update the config.txt file with your email and password settings.
    Run the main script to scrape and save trending articles:

    python scrape.py

Dependencies

The following Python packages are required to run the scraper:

    requests
    lxml
    yagmail
    pandas
    numpy

  Install these dependencies using the provided requirements.txt file.

Configuration

    edit the config.txt file in the project directory with the following format:

    sender_email
    sender_password
    receiver_email

    Replace sender_email with your email address, sender_password with your email password, and receiver_email with the recipient's email address.
    Ensure that your email provider allows less secure apps or generate an app password for your email account if required.
    
    It is advised that you use an App password instead of your actual password. Reference this link for Gmail App passwords:
    https://support.google.com/mail/answer/185833?hl=en

Contributing

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request on GitHub.
License

This project is licensed under the MIT License. See the LICENSE file for details.
