import smtplib, ssl
import os


def emailsend(message):
    host = "smtp.gmail.com"
    port = 465

    password = os.environ.get("PASSWORD")
    username = os.environ.get("EMAIL")
    receiver = os.environ.get("EMAIL2")
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

