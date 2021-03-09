import sqlite3
from datetime import datetime #takes the date from the computer where the data is running

def handleWriting(next_pin_value):
    date_value = str(datetime.now()) #gives python from the date and time at that time 

    db_conn = sqlite3.connect('movement_db')
    db_curr = db_conn.cursor()

    statement = f'''
    INSERT INTO movement_table VALUES({next_pin_value}, '{date_value}')
    '''
    print (statement)

    db_curr.execute(statement)
    db_conn.commit()
    db_conn.close()


if __name__ == "__main__":
    handleWriting()