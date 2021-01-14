import sqlite3

db_conn = sqlite3.connect('movement_db')
db_curr = db_conn.cursor()



statement = '''
SELECT * FROM movement_table
'''
print (statement)

# execute the statement (by using the cursor)
db_curr.execute(statement)

# now we have a cursor loaded with the retrieved data from the database
for row in db_curr.fetchall():
    print(row)

db_conn.commit()

db_conn.close()