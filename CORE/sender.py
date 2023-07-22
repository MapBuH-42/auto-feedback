import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        smtp_server = "YOUR_SMTP_SERVER"  # Replace with your SMTP server details
        smtp_port = 587  # Update port if needed (exc.g., 465 for SSL/TLS)

        # Create a secure connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create the message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Replace {custom_text} with the actual customizable text
        body = body.replace("{custom_text}", "This is customizable text for recipient.")

        message.attach(MIMEText(body, "plain"))

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Email sent successfully to {recipient_email}")

        # Close the connection to the SMTP server
        server.quit()

    except Exception as exc:
        print(f"Error: {exc}")
        