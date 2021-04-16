import requests # see intro python book p222
import time
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
        # we may not get any response from the sensor board, so catch any exceptions
        try:
            url = 'http://192.168.0.40/movement' # '192.168.0.20/movement' reading data from arduino board 
            resp = requests.get(url) 
            pin_list=resp.text.split('-') # splits the string of readings into a list of individual numbers 
            pin_list.pop() # we don't need the very last value, it is meaningless
            print(pin_list)
            pin_list_int = [int(float(x)) for x in pin_list]
            pin_list.append('0') # everything else expects that trailing 'meaningless' value
            prev_pin_list = pin_list_int # keep the previous set of pin readings
            diff_list = [ abs( pin_list_int[i] - prev_pin_list[i] ) for i in range(0,5) ] # take the absolute (ie positive) number

            print(diff_list)
            db.write_db.handleWriting(pin_list) #sends pin_list to write_db
            # iterate over the five sensors, checking
            if alert_sent and count<300: # 300 represents 30 seconds as tenths of a second 
                # we have recently sent an alert so we wait...
                count += 1
            else:
                count = 0
                # start checking for alerts again
                alert_sent = using_trapz.handleTrapz() # the function call will return True if an alert was raised and Fasle if no alert was raised
        # here we handle exceptions that may happen within the 'try' block  
        except ConnectionRefusedError: 
            print('Connection Refused Error - trying again in 10ms') # just ignore failed connections
        except ConnectionError:
            print('Connection Error - trying again in 10ms') 
        except Exception as e: # catch all other exceptions
            print('Exception happened {}'.format(e))
        finally:
            pass
if __name__ == "__main__":
    handleData()