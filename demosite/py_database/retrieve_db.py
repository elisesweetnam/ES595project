import sqlite3

# we need a connection
db_conn = sqlite3.connect('movement_db') # this line will creeate the db if it does not exist

# then we need acursor
db_curr = db_conn.cursor()

statement = '''
SELECT * FROM movement_table
'''

# execute the statement (by using the cursor)
db_curr.execute(statement)

# we now have a cursor LOADED with the retrieved data
for row in db_curr.fetchall():
    print(row)


# commit the changes
db_conn.commit()

# close the connection
db_conn.close()