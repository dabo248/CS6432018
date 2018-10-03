"""Contains a Flask application, which shows some of Twilio's functionality."""

from twilio.rest import Client
from flask import Flask

import config


header_text = '''
    <html>\n<head> <title>Twilio SMS</title> </head>\n<body>'''
footer_text = '</body>\n</html>'

account_sid = config.ACCOUNT_SID
auth_token  = config.AUTH_TOKEN
client = Client(account_sid, auth_token)

to = config.TO 
from_ = config.FROM_
body = config.BODY

def sendMessage(recipient, sender, message):
    # Send a SMS to a specific recipient.
    return client.messages.create(
        to=recipient, 
        from_=sender,
        body=message)

application = Flask(__name__)

application.add_url_rule('/', 'index', (lambda: header_text +
    "twilio_1" + footer_text))

application.add_url_rule('/sms', 'sms', (lambda: header_text +
    "Sent SMS with sid " + sendMessage(to, from_, body).sid + " to number " + 
    to + "." + footer_text))

if __name__ == "__main__":
    # application.debug = True
    application.run()
