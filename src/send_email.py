import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

def send_email():
    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    app_password = os.getenv("GOOGLE_APP_PASSWORD")

    print("Sender:", bool(sender_email))
    print("Receiver:", bool(receiver_email))
    print("App Password:", bool(app_password))
    # Get the parent directory of the current script
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs', 'Grant_Draft.txt')

    OUTPUT_DIR = os.path.normpath(OUTPUT_DIR)
    if os.path.exists(OUTPUT_DIR):
        with open(OUTPUT_DIR, "r", encoding="utf-8") as f:
            newsletter_content = f.read()
            
        # create sender's email address
        sender_email = os.getenv("SENDER_EMAIL")

        # create receiver's email address
        receiver_email = os.getenv("RECEIVER_EMAIL").split(",")

        # create the subject for the message
        subject = "Reminder: GRANTS & FELLOWSHIPS APPLICATIONS"

        # Create Email Message
        msg = MIMEMultipart()
        msg["From"] = "Grants For RISE"
        msg["To"] = ", ".join(receiver_email)
        msg["Subject"] = subject

        # Attach the Email Body
        msg.attach(MIMEText(newsletter_content, "plain", "utf-8"))  

        # create the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        app_password = os.getenv("GOOGLE_APP_PASSWORD")
        # login to the email account
        server.login(user=sender_email, password=app_password)

        # send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        print("Email sent out success")
    else:
        print("File not found")
    return "Email sent out successfully!"

if __name__ == "__main__":
    send_email()


