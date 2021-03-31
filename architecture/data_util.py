import requests # see intro python book p222
import time
import serial
from datetime import datetime,timedelta
import email_util
import db.write_db
import using_trapz


def handleData():
    '''
    This module handles data received from the sensor via http
    '''
    readings_l = []  # start with an empty data structure
    starttime = time.time()
    alertWillSend=True
    waitBetweenAlerts = timedelta(seconds=30)
    # make requests every second, forever
    while True:
        time.sleep(0.1 - ((time.time() - starttime) % 0.1)) # locks to system clock, sleeps every 0.1 seconds
        url = 'http://192.168.0.20/movement' # '192.168.0.20/movement' reading data from arduino board 
        resp = requests.get(url)
        pin_list=resp.text.split('-')#splits the 
        # Change pin_list to movement_list 

        ThisReading = resp
        movement_list= ThisReading - LastReading
        movement_sq= sqrt(sq(Movement))

        db.write_db.handleWriting(pin_list) #sends pin_list to write_db
        if alertWillSend:
            # handleEmail(areaUnder)
            # ... but we only want to raise an alert ONCE every 30 secons (or whatever time interval)
            alertWillSend = False # don't keep sending alerts
            alertSentTime = datetime.now()
        elif datetime.now() - waitBetweenAlerts > alertSentTime: # is it 30 seconds since last alert was sent?
            alertWillSend = True
        using_trapz.handleTrapz(alertWillSend)
        

if __name__ == "__main__":
    handleData()