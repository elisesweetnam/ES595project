import requests # see intro python book p222
import time
import serial
import datetime
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
        url = 'http://192.168.0.20/movement' # '192.168.0.40/movement'
        resp = requests.get(url)
        pin_list=resp.text.split('-')
        # print(resp.text)
        email_util.handleEmail(pin_list) 
        db.write_db.handleWriting(pin_list)

    #Change resp to movement 
    # ThisReading = resp
    # Movement= ThisReading - LastReading
    # Movement_sq= sqrt(sq(Movement))
    # mov_tests_df['Movementsq - rolling avg'] = mov_tests_df['Tom sit up 1s sampling'].rolling(3000).mean()

if __name__ == "__main__":
    handleData()