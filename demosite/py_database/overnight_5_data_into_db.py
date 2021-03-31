import pandas as pd
import sqlite3

# This file reads overnight on 5 sensors data from an Excel speadsheet and puts the data into the movement database
# be careful to run it on a copy of the db and run it ONCE

def main():

    # we need a connection
    db_conn = sqlite3.connect('movement_db')
    # then we need a cursor
    db_curr = db_conn.cursor()

    # read in a set of data from Excel
    table_number = 0
    
    dataframe_o5 = pd.read_excel('seizuretesting.xlsx', sheet_name='Overnight on 5 sensors ', usecols=['pin_value', 'dt'])
    # print(dataframe_sz[0:8])


    # Iterate over the data members and populate db
    for i, row in dataframe_o5.iterrows():
        # if i==8: # a way to se just the first few
        #     break
        # if type(row[1]) == float: # avoid any non-numeric values
        next_pin_value = row[0]
        date_value = row[1]
        # print(f"Index {i}: {date_value}, {next_pin_value}")
        table_number = (table_number)%5 # modulo arithmetic
        which_table = f'movement_table{table_number}' # will count 0, 1, 2, 3, 4
        table_number+=1
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