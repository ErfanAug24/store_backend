from src.email import mail
from flask_mail import Message
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()


def send_email(subject, receiver, body, sender=os.getenv("MAIL_USERNAME")):
    msg = Message(subject, sender=sender, recipients=receiver, body=body)
    mail.send(msg)
    return {'Status': 'Sent',
            'to': receiver,
            'from': sender,
            'at': f'{datetime.utcnow}'}
