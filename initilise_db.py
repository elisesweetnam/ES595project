
import sqlite3

def handleInitiliseDB():
    '''
    this module creates the database if required 
    '''
    
    db_conn = sqlite3.connect('movement_db')
    db_curr = db_conn.cursor()

    statement = ''' 
    CREATE TABLE movement_table (
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

if __name__ == "__main__":
    handleInitiliseDB()