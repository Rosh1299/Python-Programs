# sending emails using python

# mime-multipurpose internet mail extensions
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "Roshan Sagvekar"
message["to"] = "yogesh.surve.v2stech@gmail.com"
message["subject"] = "Testing"
message.attach(MIMEText("Hello,This is testing message."))
# for attaching image file
# message.attach(MIMEImage(Path("demo.JPG").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("roshan.sagvekar.v2stech@gmail.com", "Rosh@1299")
    smtp.send_message(message)
    print("Sent Sucessfully....")
