import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "es595project@gmail.com"  # Enter your address
receiver_email = "es595recipient@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ") #input() used so i don't need to save my password within the code
message = """\
Subject: Hi there

This is a test email for ES595 project."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)