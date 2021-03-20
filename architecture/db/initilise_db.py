import sqlite3

def handleInitiliseDB():
    '''
    this module creates the database if required 
    '''
    
    db_conn = sqlite3.connect('movement_db')
    db_curr = db_conn.cursor()

    statement0 = ''' 
    CREATE TABLE movement_table0 (
    reading int,
    reading_dt datetime
    )
    '''
    statement1 = ''' 
    CREATE TABLE movement_table1 (
    reading int,
    reading_dt datetime
    )
    '''
    statement2 = ''' 
    CREATE TABLE movement_table2 (
    reading int,
    reading_dt datetime
    )
    '''
    statement3 = ''' 
    CREATE TABLE movement_table3 (
    reading int,
    reading_dt datetime
    )
    '''
    statement4 = ''' 
    CREATE TABLE movement_table4 (
    reading int,
    reading_dt datetime
    )
    '''
    # execute the statement (by using the cursor)
    db_curr.execute(statement0)
    db_curr.execute(statement1)
    db_curr.execute(statement2)
    db_curr.execute(statement3)
    db_curr.execute(statement4)

    # commit the changes
    db_conn.commit()

    # close the connection
    db_conn.close()

if __name__ == "__main__":
    handleInitiliseDB()