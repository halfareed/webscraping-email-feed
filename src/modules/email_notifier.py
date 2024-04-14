import yagmail
from yagmail.error import YagInvalidEmailAddress, YagAddressError
from smtplib import SMTPAuthenticationError,SMTPException

def send_email_notification(msg_df) -> None:
    """
    Sends email notifications for new articles.
    """
    with open("src/tests/config/config.txt", "r") as f:
        content = [line.strip() for line in f]
        print(content)
    try:
        # Send email using yagmail API
        yag = yagmail.SMTP(content[1], content[2])
        yag.send(content[3], "GEEKSFORGEEKS, Trending in Python", msg_df.iloc[:])
        print("Check Inbox!")
    except SMTPAuthenticationError:
        print("Username and Password not accepted")
    except (YagAddressError, YagInvalidEmailAddress):
        print("address was given in an invalid format")
    except SMTPException:
        print("Server error")
    return


