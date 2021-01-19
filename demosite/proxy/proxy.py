# may need to pip install requests
import requests # see intro python book p222
import time

# Make ONE request
url = 'http://numbersapi.com/79/trivia' # '192.168.0.38/movement'
resp = requests.get(url)
print(resp) #<Response [200]>
print(resp.text)

# # rapidly make several requests and store them in a data structure
# readings_l = []
# for i in range (0,10): # start at 0 stop before 10
#     url = 'http://numbersapi.com/{}/trivia'.format(i) # '192.168.0.38/movement'
#     resp = requests.get(url)
#     readings_l.append(resp.text)
# # then print the data structure
# print(readings_l)

# # make requests every second, forever
# readings_l = []  # start with an empty data structure
# starttime = time.time()
# print('To stop this program, KILL THIS TERMINAL')
# while True:
#     time.sleep(1.0 - ((time.time() - starttime) % 1.0)) # locks to system clock, sleeps every 1.0 seconds
#     url = 'http://numbersapi.com/{}/trivia'.format(time.time) # '192.168.0.38/movement'
#     resp = requests.get(url)
#     print(resp.text)

