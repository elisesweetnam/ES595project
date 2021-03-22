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
    readings_l = []  # start with an empty data structure
    starttime = time.time()
    # make requests every second, forever
    while True:
        time.sleep(1.0 - ((time.time() - starttime) % 1.0)) # locks to system clock, sleeps every 1.0 seconds
        url = 'http://192.168.0.20/movement' # '192.168.0.20/movement' reading data from arduino board 
        resp = requests.get(url)
        pin_list=resp.text.split('-')#splits the 
        # print(resp.text)
        # Change pin_list to movement_list 
        # ThisReading = resp
        # movement_list= ThisReading - LastReading
        # movement_sq= sqrt(sq(Movement))
        # mov_tests_df['Movementsq - rolling avg'] = mov_tests_df['Tom sit up 1s sampling'].rolling(3000).mean()
        email_util.handleEmail(pin_list) #sends pin_list to email_util
        db.write_db.handleWriting(pin_list) #sends pin_list to write_db

if __name__ == "__main__":
    handleData()