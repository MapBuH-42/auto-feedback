'''Importing the send email functionality'''
from sender import send_email

if __name__ == "__main__":
    sender_email = "YOUR_EMAIL@gmail.com"
    sender_password = "YOUR_PASSWORD"

    recipients = [
        "recipient1@example.com",
        "recipient2@example.com",
        "recipient3@example.com",
    ]

    subject = "Customizable Email"
    body = """
    Dear recipient,

    This is a sample email with customizable text: {custom_text}.

    Best regards,
    Your Name
    """

    for recipient in recipients:
        send_email(sender_email, sender_password, recipient, subject, body)
