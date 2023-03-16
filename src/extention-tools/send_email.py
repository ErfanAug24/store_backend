from src.email import mail
from flask_mail import Message
from datetime import datetime


def send_email(subject, sender, receiver, body):
    msg = Message(subject, sender=sender, recipients=receiver, body=body)
    mail.send(msg)
    return {'Status': 'Sent',
            'to': receiver,
            'from': sender,
            'at': f'{datetime.utcnow}'}
