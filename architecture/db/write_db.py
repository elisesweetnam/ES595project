import sqlite3
from datetime import datetime #takes the date from the computer where the data is running

def handleWriting(next_pin_values):
    # print(next_pin_values)
    p0,p1,p2,p3,p4,sink=next_pin_values #sink is a throwaway value 
    date_value = str(datetime.now()) #gives python from the date and time at that time 

    db_conn = sqlite3.connect('movement_db')
    db_curr = db_conn.cursor()

    statement0 = f'''
    INSERT INTO movement_table0 VALUES({p0}, '{date_value}')
    '''
    statement1 = f'''
    INSERT INTO movement_table1 VALUES({p1}, '{date_value}')
    '''
    statement2 = f'''
    INSERT INTO movement_table2 VALUES({p2}, '{date_value}')
    '''
    statement3 = f'''
    INSERT INTO movement_table3 VALUES({p3}, '{date_value}')
    '''
    statement4 = f'''
    INSERT INTO movement_table4 VALUES({p4}, '{date_value}')
    '''
    # print (statement)

    db_curr.execute(statement0)
    db_curr.execute(statement1)
    db_curr.execute(statement2)
    db_curr.execute(statement3)
    db_curr.execute(statement4)

    db_conn.commit()
    db_conn.close()


if __name__ == "__main__":
    handleWriting()