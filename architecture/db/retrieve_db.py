import sqlite3
def handleRetrieve(min_date, max_date):
    # we need a connection
    db_conn = sqlite3.connect('movement_db') # this line will create the db if it does not exist

    # then we need a cursor
    db_curr = db_conn.cursor()

    statement = '''
    SELECT * FROM movement_table 
    where reading_dt > '{}' 
    and reading_dt < '{}'
    '''.format(min_date, max_date)


    # print(statement)
    # execute the statement (by using the cursor)
    db_curr.execute(statement)

    # we now have a cursor LOADED with the retrieved data
    for row in db_curr.fetchall():
        print(row)


    # commit the changes
    db_conn.commit()

    # close the connection
    db_conn.close()


if __name__ == "__main__":
    handleRetrieve('2021-03-04 17:28:00','2021-03-04 17:30:00')
