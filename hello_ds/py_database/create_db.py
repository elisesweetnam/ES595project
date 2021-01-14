import sqlite3 #sqlite3 is a library for databasing 

#connection
db_conn = sqlite3.connect('movement_db') #_db tells us its a database 

#curser
db_curr = db_conn.cursor() #curser navigates in database. points to where you are in a database 

#statement, tripple quotes lets you add new lines within a quote
statement = '''
CREATE TABLE movement_table(
    id int primary key, 
    reading int,
    reading_dt datetime
)
'''

#exicute statement (cursor)
db_curr.execute(statement)

#comit the changes 
db_conn.commit()

#close the connection
db_conn.close()