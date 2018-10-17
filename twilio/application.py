"""Contains a Flask application, which shows some of Twilio's functionality."""

from random import randint

from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

import config
from resources.response import MALARIA_0, MALARIA_1, COLD


header_text = '''
    <html>\n<head> <title>Twilio SMS</title> </head>\n<body>'''
footer_text = '</body>\n</html>'

account_sid = config.ACCOUNT_SID
auth_token  = config.AUTH_TOKEN
client = Client(account_sid, auth_token)

to = config.TO 
from_ = config.FROM_
body = config.BODY

# Twilio (Part 1)
def send_message(recipient, sender, message):
    """Send a SMS to a specific recipient."""
    return client.messages.create(
        to=recipient, 
        from_=sender,
        body=message)

application = Flask(__name__)

application.add_url_rule('/', 'index', (lambda: header_text +
    "twilio_1" + footer_text))

application.add_url_rule('/sms', 'sms', (lambda: header_text +
    "Sent SMS with sid " + send_message(to, from_, body).sid + " to number " + 
    to + "." + footer_text))

# Twilio (Part 2)
@application.route("/doctor", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    body = request.values.get('Body', None)

    resp = MessagingResponse()
    rand = randint(0, 1)

    if body == 'yes':
        resp.message(MALARIA_1)
    else:
        if rand == 0:
            resp.message(MALARIA_0)
        else:
            resp.message(COLD)

    return str(resp)

if __name__ == "__main__":
    # application.debug = True
    application.run()
