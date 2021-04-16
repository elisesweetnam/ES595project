import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def handleEmail(msg, start_dt=0, end_dt=1, area_under=0): # sensible defaults
    '''
    This module handles sending emails
    '''  
    # read in the current email address to be used from a simple text file, or use a default address
    try:
        with open('emailAddress.txt','rt') as fin:
            currentEmail = fin.readline()
    except: # if we fail to read the text file, just set a default
        currentEmail = 'es595recipient@gmail.com'
    # print(currentEmail)

  # sending an email with hyperlink
    sender_email = "es595project@gmail.com"
    receiver_email = currentEmail # "es595recipient@gmail.com"
    print('sending an email to {}'.format(receiver_email))
    password = "Projectpassword2021!"

    message = MIMEMultipart("alternative")
    message["Subject"] = "ALERT"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    The patient has triggered an alert:
    http://127.0.0.1:5000/"""
    html = """\
    <html>
    <body>
        <p>Hi,<br>
        <!-- URL may need to change -->
        <a href="http://127.0.0.1:5000/alert?start_dt={}&end_dt={}&area_under={}">The patient</a> 
        has triggered an alert.
        </p>
        <section>
        {}
        </section>
    </body>
    </html>
    """.format(start_dt, end_dt, area_under, msg)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    
if __name__ == "__main__":
    handleEmail('dummy message just to exercise the code')