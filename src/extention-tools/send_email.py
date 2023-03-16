import requests
import smtplib
import ssl
import os
from dotenv import load_dotenv

port = 465
context = ssl.create_default_context()
load_dotenv()


def send_email(port, password, context, receiver_email, message):
    with smtplib.SMTP_SSL("smtp.gamil.com",
                          port=port,
                          context=context) as server:
        server.login(os.getenv("EMAIL"), password)
        server.sendmail(os.getenv("EMAIL"), receiver_email, message)
