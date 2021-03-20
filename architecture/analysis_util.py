import db.initilise_db as init
import db.write_db as wrt

def handleAnalysis():
    '''
    This module handles the analysis of data
    '''
    print("handling analysis")
    init.handleInitiliseDB()
    wrt.handleWriting()
    


if __name__ == "__main__":
    handleAnalysis()