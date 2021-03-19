from retrieve_db import retrieve_dt

def main():
    # some sample date-time values
    start_dt = '2021-03-04 17:00:00'
    end_dt = '2021-03-04 17:00:30'

    # get the date-time values

    # use the provided date-time values to retrieve values from tth db
    j = retrieve_dt(start_dt, end_dt)

    # send the retrieved values back to the web page
    return j

if __name__ == "__main__":
    main()