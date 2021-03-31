import pandas as pd
import sqlite3

# This file reads historical data from an Excel speadsheet and puts the data into the movement database
# be careful to run it on a copy of the db and run it ONCE


def main():

    # we need a connection
    db_conn = sqlite3.connect('movement_db')
    # then we need a cursor
    db_curr = db_conn.cursor()

    # read in a set of data from Excel
    # make sure we're inserting into correct table (for pin 0, 1, 2, 3 or 4)
    table_number = 0 # 0, 1, 2, 3 or 4 (tables are called movement_table0 etc)
    which_table = f'movement_table{table_number}'
    # change usecols for each set of readings
    dataframe_sz = pd.read_excel('seizuretesting.xlsx', sheet_name='Seizure examples', usecols=[f'date_time_s{table_number+1}', f'Seizure {table_number+1}'])
    # print(dataframe_sz[0:3])


    # Iterate over the data members and populate db
    for i, row in dataframe_sz.iterrows():
        if type(row[1]) == float: # avoid any non-numeric values
            if i==282:
                break
            next_pin_value = int(row[1]) # the db expect an integer value
            date_value = row[0] # .strftime('%m-%d-%Y %H:%M:%S')
            # print(f"Index {i}: {date_value}, {next_pin_value}")
        statement = f'''
        INSERT INTO {which_table} VALUES({next_pin_value}, '{date_value}' )
        '''
        # print(statement)
        # execute the statement (using the cursor)
        db_curr.execute(statement)
    
    # commit all our changes
    db_conn.commit()

    # close the connection
    db_conn.close()    

if __name__ == "__main__":
    main()