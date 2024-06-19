import smtplib, ssl
import os


def emailsend(message):
    host = "smtp.gmail.com"
    port = 465

    password = os.getenv("PASSWORD")
    username = os.getenv("EMAIL")

    receiver = os.getenv("EMAIL")
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

