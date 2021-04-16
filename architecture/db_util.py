import db.initilise_db as init
import db.write_db as wrt

def handleDatabase():
    '''
    This module handles the database reading and writing
    '''
    init.handleInitiliseDB()
    wrt.handleWriting()
    
if __name__ == "__main__":
    handleDatabase()