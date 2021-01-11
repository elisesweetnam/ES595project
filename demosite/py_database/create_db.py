import sqlite3

# we need a connection
db_conn = sqlite3.connect('movement_db') # this line will creeate the db if it does not exist

# then we need acursor
db_curr = db_conn.cursor()

# next we dream up an SQL statement
# tripple quotes let us have several new lines within the quotes
statement = ''' 
CREATE TABLE movement_table (
    id int primary key,
    reading int,
    reading_dt datetime
)
'''

# execute the statement (by using the cursor)
db_curr.execute(statement)

# commit the changes
db_conn.commit()

# close the connection
db_conn.close()



