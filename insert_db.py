import sqlite3
from datetime import datetime
date_value = str(datetime.now())#gives python from the date and time at that time 

db_conn = sqlite3.connect('movement_db')
db_curr = db_conn.cursor()



statement = f'''
INSERT INTO movement_table VALUES(2, 300, '{date_value}')
'''
print (statement)

db_curr.execute(statement)

db_conn.commit()

db_conn.close()


