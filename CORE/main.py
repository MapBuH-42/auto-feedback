'''Importing the send email functionality'''
from sender import send_email

if __name__ == "__main__":
    sender_email = "auto.test.feedback.bot" #REPLACE WITH SENDER EMAIL ADDRESS
    sender_password = "zYSd.6hLQUrtS$A" #REPLACE WITH SENDER EMAIL PASSWORD - EXPORT REF FOR SECURITY

    recipients = [
        "x.termal@gmail.com"
    ]

    subject = "Customizable Email"
    body = """
    Dear {recipient},

    This is a sample email with customizable text: {custom_text}.

    Best regards,
    Your Name
    """

    for recipient in recipients:
        send_email(sender_email, sender_password, recipient, subject, body)
