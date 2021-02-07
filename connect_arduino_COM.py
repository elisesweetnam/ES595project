import serial
import sqlite3 
import datetime
import time 

def add_db(time,FSR,dt):
    db_conn=sqlite3.connect('movement.db')
    db_curr=db_conn.cursor()

    db_curr.execute('''
    CREATE TABLE movement_table
    (Time TEXT, 
    reading int, 
    reading_dt datetime)
    ''')

    db_curr.execute(
        '''INSERT INTO movement_table
    (Time TEXT, 
    reading, 
    reading_dt)
    VALUES (?,?,?)
    ''',
    (time, FSR, dt)
    )
    
    db_conn()
    db_curr.close()
    db_conn.close()

def read_data():
    arduinodata=serial.Serial('COM5', 115200, timeout=0.1)
    while arduinodata.inWaiting:
        val=arduinodata.readline().decode('ascii')
        if len(val)==13:
            #print(val)
            return val


while 1:
    FSR=read_data()
    mytime=datetime.datetime.now()
    tm='{}:{}:{}'.format(mytime.hour,mytime.minute,mytime.second)
    dt='{}/{}/{}'.format(mytime.day,mytime.month,mytime.year)

    print(tm,str(FSR),str(dt))
    add_db(tm,str(FSR),str(dt))

    time.sleep(10)

