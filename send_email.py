import smtplib, ssl


def emailsend(message):
    host = "smtp.gmail.com"
    port = 465

    username = "dlakshya223@gmail.com"
    password = "kukmchplrxbwbdqz"

    receiver = "dlakshya223@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
