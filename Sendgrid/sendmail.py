from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

# SENDGRID_API_KEY = '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'
SENDGRID_API_KEY = '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'


message = Mail(
    from_email='roshan.sagvekar.v2stech@gmail.com',
    to_emails='roshansagvekar1299@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<h1>Hello,</h1>How are you??')
try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print(response.status_code)
    # print(response.body)
    # print(response.headers)
except Exception as e:
    print(e)
