import sqlite3
import json # we might need to use json data format

# a function to retrieve valies from the DB given a start and end date-time
def retrieve_dt(start_dt='2021-03-04 17:00:00', end_dt='2021-03-04 17:00:30'):
    # we need a connection
    db_conn = sqlite3.connect('movement_db')
    # then we need a cursor
    db_curr = db_conn.cursor()

    # select reading, reading_dt in that order, so the chart has x and y
    statement0 = '''
    SELECT reading_dt, reading FROM movement_table0 
    where reading_dt >= '{}' 
    and reading_dt <= '{}'
    '''.format(start_dt, end_dt)
    statement1 = '''
    SELECT reading_dt, reading FROM movement_table1 
    where reading_dt >= '{}' 
    and reading_dt <= '{}'
    '''.format(start_dt, end_dt)
    statement2 = '''
    SELECT reading_dt, reading FROM movement_table2 
    where reading_dt >= '{}' 
    and reading_dt <= '{}'
    '''.format(start_dt, end_dt)
    statement3 = '''
    SELECT reading_dt, reading FROM movement_table3 
    where reading_dt >= '{}' 
    and reading_dt <= '{}'
    '''.format(start_dt, end_dt)
    statement4 = '''
    SELECT reading_dt, reading FROM movement_table4 
    where reading_dt >= '{}' 
    and reading_dt <= '{}'
    '''.format(start_dt, end_dt)

    results_list=[] #create list 

    # execute the statements (using the cursor)
    db_curr.execute(statement0)
    results_list.append(json.dumps(db_curr.fetchall())) # convert the returned data to a json string
    db_curr.execute(statement1)
    results_list.append(json.dumps(db_curr.fetchall()))
    db_curr.execute(statement2)
    results_list.append(json.dumps(db_curr.fetchall()))
    db_curr.execute(statement3)
    results_list.append(json.dumps(db_curr.fetchall()))
    db_curr.execute(statement4)
    results_list.append(json.dumps(db_curr.fetchall()))
    # print(results_list)
    # results_j = json.dumps(db_curr.fetchall()) 
    # close the connection
    db_conn.close()
    # We want to return the data for use elsewhere
    return results_list

if __name__ == "__main__":
    retrieve_dt
    # j = retrieve_dt()
    # print(j)




# import sqlite3
# def handleRetrieve(min_date, max_date):
#     # we need a connection
#     db_conn = sqlite3.connect('movement_db') # this line will create the db if it does not exist

#     # then we need a cursor
#     db_curr = db_conn.cursor()

#     statement = '''
#     SELECT * FROM movement_table 
#     where reading_dt > '{}' 
#     and reading_dt < '{}'
#     '''.format(min_date, max_date)


#     # print(statement)
#     # execute the statement (by using the cursor)
#     db_curr.execute(statement)

#     # we now have a cursor LOADED with the retrieved data
#     for row in db_curr.fetchall():
#         print(row)


#     # commit the changes
#     db_conn.commit()

#     # close the connection
#     db_conn.close()


# if __name__ == "__main__":
#     handleRetrieve('2021-03-04 17:28:00','2021-03-04 17:30:00')