import sqlite3
# to work with dates we need a library
from datetime import datetime
date_value = str(datetime.now()) # this gives us a Python datetime representing 'now'

# we need the same od same old connection stuff
db_conn = sqlite3.connect('movement_db')
db_curr = db_conn.cursor()

# this time , the SQL statement will INSERT new values into our db
# f is 'format' and the {} contain the thing to be injected into the string
statement = f'''
INSERT INTO movement_table VALUES(2, 300, '{date_value}' )
'''

print(statement)
# execute
db_curr.execute(statement)
# commit
db_conn.commit()
# close
db_conn.close()