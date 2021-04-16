import sqlite3
import json # we might need to use json data format

# a function to retrieve values from the DB given a start and end date-time
def retrieve_dt(start_dt='2021-03-04 17:00:00', end_dt='2021-03-04 17:00:30'):
    # we need a connection
    db_conn = sqlite3.connect('movement_db')
    # then we need a cursor
    db_curr = db_conn.cursor()
    results_list=[] #create an empty list 
    prev_data_point = ("",0,0)
    # execute the statements (using the cursor)
    for index in range(0,5):
        statement = '''
            SELECT reading_dt, reading FROM movement_table{} 
            where reading_dt >= '{}' 
            and reading_dt <= '{}'
        '''.format(index, start_dt, end_dt)
        db_curr.execute(statement)
        values = db_curr.fetchall()
        calculated_values = []
        for data_point in values:
            data_point = (data_point[0], data_point[1], abs(data_point[1]-prev_data_point[1]))
            prev_data_point = data_point
            calculated_values.append(data_point)
        print(calculated_values) # we have a list of tuples
        results_list.append(json.dumps(calculated_values)) # convert the returned data to a json string
    
    # close the connection
    db_conn.close()
    # We want to return the data for use elsewhere
    return results_list

if __name__ == "__main__":
    retrieve_dt