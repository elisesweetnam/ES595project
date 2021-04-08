import requests # see intro python book p222
import time
import serial
from datetime import datetime,timedelta
import email_util
import db.write_db
import using_trapz
import math # we need this for sqrt calculations

def handleData():
    '''
    This module handles data received from the sensor via http
    '''
    # set some initial values
    starttime = time.time()
    alert_sent = False
    count = 0 # counter to check 30 seconds between checking for alerts
    pin_list = [0,0,0,0,0]
    prev_pin_list = [0,0,0,0,0]
    # make requests every 0.1 second, forever
    while True:
        time.sleep(0.1 - ((time.time() - starttime) % 0.1)) # locks to system clock, sleeps every 0.1 seconds
        url = 'http://192.168.0.40/movement' # '192.168.0.20/movement' reading data from arduino board 
        resp = requests.get(url) 
        prev_pin_list = pin_list # keep the previous set of pin readings
        pin_list=resp.text.split('-') # splits the string of readings into a list of individual numbers 
        # don't use this next line when using real sensors
        # pin_list = [1000,2000,3000,4000,0,0] # we always get an extraneous value in addition to pins - probably new line character
        # calculate the root-square of each reading difference
        diff_list = [ math.sqrt( ( pin_list[i] - prev_pin_list[i] )**2 ) for i in range(0,5) ]
        print(diff_list)
    # not sure what to do with these root-square values
        # mov_tests_df['Movementsq - rolling avg'] = mov_tests_df['Tom sit up 1s sampling'].rolling(3000).mean()
        db.write_db.handleWriting(pin_list) #sends pin_list to write_db
        # iterate over the five sensors, checking
        if alert_sent and count<300: # 300 represents 30 seconds as tenths of a second 
            # we have recently sent an alert so we wait...
            count += 1
        else:
            count = 0
            # start checking for alerts again
            alert_sent = using_trapz.handleTrapz() # the function call will return True if an alert was raised and Fasle if no alert was raised
           
if __name__ == "__main__":
    handleData()