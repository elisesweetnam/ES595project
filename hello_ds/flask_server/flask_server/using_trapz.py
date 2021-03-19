import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
import json

from retrieve_db import retrieve_dt

# retrieved = retrieve_dt(start_dt = "2021-03-17 14:42:45",end_dt = "2021-03-17 14:42:55")#calls string from retrieve_dt
# sample = json.loads(retrieved[0])#calling on the 0th memebr of the string

retrieved = retrieve_dt(start_dt = "2021-03-17 14:42:45",end_dt = "2021-03-17 14:42:55")
retrieved_l = json.loads(retrieved[0])
# print(retrieved_l)
sample_l = []#create empty list
for i in range(0, len(retrieved_l)):
    sample_l.append(retrieved_l[i][1])
print(sample_l)

print(np.trapz(sample_l))