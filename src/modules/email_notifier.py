"""Module providing a function to send email notifications of filtered articles."""


import yagmail
import os
from yagmail.error import YagInvalidEmailAddress, YagAddressError
from smtplib import SMTPAuthenticationError, SMTPException
from dotenv import load_dotenv


load_dotenv()

def send_email_notification(msg_df) -> None:
    """
    Sends email notifications for new articles.
    """
    sender = os.getenv('SENDER')
    sender_unlock = os.getenv('SENDER_UNLOCK')
    recipient = os.getenv('RECIPIENT')
    try:
        # Send email using yagmail API
        yag = yagmail.SMTP(sender, sender_unlock)
        yag.send(recipient, "GEEKSFORGEEKS, Trending in Python", msg_df.iloc[:])
        print("Check Inbox!")
    except SMTPAuthenticationError:
        print("Username and Password not accepted")
    except (YagAddressError, YagInvalidEmailAddress):
        print("address was given in an invalid format")
    except SMTPException:
        print("Server error")
    return
