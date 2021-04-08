import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
import json
import pandas as pd
import time
from datetime import datetime,timedelta
import requests # we need this so we can make http requests to the server (e.g. to send email)


from db.retrieve_db import retrieve_dt
from email_util import handleEmail

# plt.rc('figure', figsize=(10,6))

# df1 = pd.read_excel("seizuretesting.xlsx", sheet_name = 'Seizure examples')
# df2 = pd.read_excel("seizuretesting.xlsx", sheet_name = 'Data - movement tests')
# # plt.plot(df1)
# # df1[['Seizure 1', 'Seizure 2']]

# retrieved = retrieve_dt(start_dt = "2021-03-17 14:42:45",end_dt = "2021-03-17 14:42:55")#calls string from retrieve_dt
# sample = json.loads(retrieved[0])#calling on the 0th memebr of the string

def handleTrapz():
    '''
    This function read the most recennt 30-seconds of data from the database for all five sensors
    then iterates over the sensor data to see if any of them exceeds a threshold
    This is done by using the trapz method from numpy
    If a threshold is exceeded, an alert string is constructed and sent to the email utility
    return True if an alert was raised and return False if not
    '''
    start = datetime.now()-timedelta(seconds=30)
    end   = datetime.now()
    thresholdForAlerts = 60000 # revisit 60,000
    # get reading for all five sensors for the last 30 seconds
    retrieved = retrieve_dt(start_dt = start, end_dt = end)
    alert_string = '' # an empty text string, which will hold any alerts we might need to generate
    # we need to check the data for each sensor, here numbered 0-4
    for i in range(0,5): # start at 0, stop before 5
        retrieved_l = json.loads(retrieved[i]) # reads sensor 0, 1, 2, 3, 4 in turn
        # print('retrieved_l from using_trapz {}\n'.format(retrieved_l)) # NB 'here we have data for ONE pin only
        sample_l = [] #create an empty list
        # populate the list
        for j in range(0, len(retrieved_l)):
            sample_l.append(retrieved_l[j][1]) # [j][1] is the actual pin value, [j][0] is the date-time for that reading
        # find the area under the current sensor readings
        areaUnder = np.trapz(sample_l)
        if areaUnder > thresholdForAlerts:
            # threshold exceeded, so we add an alert to the alert string
            # NB we put an html line-break at teh end of each alert
            alert_string += 'Sensor: {} areaUnder:{} between {} and {}<br/>'.format(i, areaUnder, start, end)
            currentAreaAlert = areaUnder
            # send an alert unless we recently sent one
            print(alert_string)
            # call the email utility to send and email
            # NB could send an sms text message as well but that would cost per sms
    if alert_string == '': # if it is still an empty string, we have no alerts!
        return False # we found no reason to raise an alert
    else:
        handleEmail(alert_string, start, end, currentAreaAlert) # send the alert string to the email utility

        # try to use the server to send an email (the server knows the latest email address to use)
        url = 'http://127.0.0.1:5000/send_email?message={}&start_dt={}&end_dt={}&area_under={}'.format(alert_string, start, end, currentAreaAlert)
        print(url)
        d = requests.get(url)

        alert_string = ''# set the alert string ready for the next set of alerts to be generated
        return True # yes, we DID raise an alert
        
        # NB this alert_string could be altered so it included clickable links for each graph
        # probably best to send the alert data and let the email utility work out what to do with it


# we call our alert checker every 0.1 seconds
def main():
    while True:
        time.sleep(0.1)
        handleTrapz()

if __name__ == "__main__":
    main()