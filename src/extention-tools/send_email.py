import requests
import smtplib
import ssl
import os
from dotenv import load_dotenv

port = 465
password = os.getenv("EMAIL_PASSWORD")
context = ssl.create_default_context()


def send_email(port, password, context):
    with smtplib.SMTP_SSL("smtp.gamil.com",
                          port=os.getenv("EMAIL_POST"),
                          context=context) as server:
        server.login(os.getenv("EMAIL"), os.getenv("EMAIL_PASSWORD"))
        server.sendmail()
        