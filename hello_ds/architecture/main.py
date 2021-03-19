# import our modules
# this modile handles other modules by importing 
import data_util
import db_util
import email_util

def main():
# documentations doc string (more than just a comment)
#    done at the top of a function
    '''
    This module handles all the other modules 
    '''
    data_util.handleData()
    # db_util.handleDatabase()
    # email_util.handleEmail()

if __name__ == "__main__":
    main()