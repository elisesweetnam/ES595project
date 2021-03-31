# import our modules
# this modile handles other modules by importing 
import data_util
import db_util
import server

def main():
# documentations doc string (more than just a comment)
#    done at the top of a function
    '''
    This module handles all the other modules 
    '''
    data_util.handleData()
    server.handleServer()

if __name__ == "__main__":
    main()