import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
import json
import pandas as pd
import time
from datetime import datetime,timedelta

from db.retrieve_db import retrieve_dt
from email_util import handleEmail

# plt.rc('figure', figsize=(10,6))

# df1 = pd.read_excel("seizuretesting.xlsx", sheet_name = 'Seizure examples')
# df2 = pd.read_excel("seizuretesting.xlsx", sheet_name = 'Data - movement tests')
# # plt.plot(df1)
# # df1[['Seizure 1', 'Seizure 2']]

# retrieved = retrieve_dt(start_dt = "2021-03-17 14:42:45",end_dt = "2021-03-17 14:42:55")#calls string from retrieve_dt
# sample = json.loads(retrieved[0])#calling on the 0th memebr of the string
def handleTrapz(alertWillSend = True):
    start = datetime.now()-timedelta(seconds=30)
    retrieved = retrieve_dt(start_dt = start, end_dt = datetime.now())
    retrieved_l = json.loads(retrieved[0])
    # print(retrieved_l)
    sample_l = [] #create empty list
    for i in range(0, len(retrieved_l)):
        sample_l.append(retrieved_l[i][1])
    print(sample_l)

    areaUnder = np.trapz(sample_l)
    if areaUnder > 60000:#revisit 60,000
        # threshold exceeded, so we raise an alert
        if alertWillSend:
            print("alert ={}".format(areaUnder))

def main():
    while True:
        time.sleep(0.1)
        handleTrapz()

if __name__ == "__main__":
    main()