# may need to pip install requests
import requests # see intro python book p222
import time
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np
import serial
import sqlite3 
import datetime
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# make requests every second, forever
readings_l = []  # start with an empty data structure
starttime = time.time()
print('To stop this program, KILL THIS TERMINAL')
while True:
    time.sleep(1.0 - ((time.time() - starttime) % 1.0)) # locks to system clock, sleeps every 1.0 seconds
    url = 'http://192.168.0.40/movement' # '192.168.0.40/movement'
    resp = requests.get(url)
    print(resp.text)

#Put data in a database 

    db_conn=sqlite3.connect('movement.db')
        db_curr=db_conn.cursor()

        db_curr.execute('''
        CREATE TABLE movement_table
        (Time TEXT, 
        reading int, 
        reading_dt datetime)
        ''')

        db_curr.execute(
            '''INSERT INTO movement_table
        (Time TEXT, 
        reading, 
        reading_dt)
        VALUES (?,?,?)
        ''',
        (time, FSR, dt)
        )
        
        db_conn()
        db_curr.close()
        db_conn.close()

#Change resp to to movement 
    ThisReading = resp
    Movement= ThisReading - LastReading
    Movementsq= sqrt(sq(Movement))
    Serial.println(Movementsq)
    mov_tests_df['Movementsq - rolling avg'] = mov_tests_df['Tom sit up 1s sampling'].rolling(3000).mean()


#Make Movementsq into a graph

    plt.rc('figure', figsize=(10, 6))
    plt.plot(Movementsq)


#Calculate corr/cov 
    mov_tests_df = pd.read_excel("testing results.xlsx", sheet_name='Data - movement tests')
    df1 = Movementsq
    df2 = mov_tests_df
    correlation = df2.corrwith(df2.df1)
#If there is a sig diff send email alert es595email.py




# sending an email with hyperlink

    sender_email = "es595project@gmail.com"
    receiver_email = "es595recipient@gmail.com"
    password = input("Type your password and press enter:")

    message = MIMEMultipart("alternative")
    message["Subject"] = "ALERT"
    message["From"] = sender_email
    message["To"] = receiver_email

    # # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    The patient has triggered an alert:
    http://192.168.0.40/movement"""
    html = """\
    <html>
      <body>
        <p>Hi,<br>
           <a href="http://192.168.0.40/movement">The patient</a> 
           has triggered an alert.
        </p>
      </body>
    </html>
    """

    # # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # # Create secure connection with server and send email
        if correlation >0.5:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )




