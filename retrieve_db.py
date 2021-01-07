import sqlite3
from datetime import datetime
date_value = str(datetime.now())#gives python from the date and time at that time 

db_conn = sqlite3.connect('movement_db')
db_curr = db_conn.cursor()



statement = '''
SELECT * FROM movement_table
'''
print (statement)

db_curr.execute(statement)

for row in db_curr.fetchall():
    print(row)

db_conn.commit()

db_conn.close()