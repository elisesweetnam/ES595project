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
import email_util
import db.write_db

def handleData():
    '''
    This module handles data received from the sensor via http
    '''
    # reading data from arduino board 
    print("handling data")
    # may need to pip install requests
    

    # make requests every second, forever
    readings_l = []  # start with an empty data structure
    starttime = time.time()
    print('To stop this program, KILL THIS TERMINAL')
    while True:
        time.sleep(1.0 - ((time.time() - starttime) % 1.0)) # locks to system clock, sleeps every 1.0 seconds
        url = 'http://192.168.0.162/movement' # '192.168.0.40/movement'
        resp = requests.get(url)
        # print(resp.text)
        email_util.handleEmail(resp.text) 
        db.write_db.handleWriting(int(float(resp.text)))

    #Change resp to movement 
    # ThisReading = resp
    # Movement= ThisReading - LastReading
    # Movementsq= sqrt(sq(Movement))
    # mov_tests_df['Movementsq - rolling avg'] = mov_tests_df['Tom sit up 1s sampling'].rolling(3000).mean()

    # #Make Movementsq into a graph
    #     plt.rc('figure', figsize=(10, 6))
    #     plt.plot(Movementsq)

    # #Calculate corr/cov 
    #     mov_tests_df = pd.read_excel("testing results.xlsx", sheet_name='Data - movement tests')
    #     df1 = Movementsq
    #     df2 = mov_tests_df
    #     correlation = df2.corrwith(df2.df1)
    #If there is a sig diff send email alert es595email.py
                    


if __name__ == "__main__":
    handleData()