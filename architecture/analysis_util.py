import using_fft
import using_trapz

def handleAnalysis():
    '''
    This module handles the analysis of data
    '''
    print("handling analysis")
    using_fft.handleFFT()
    using_trapz.handleTrapz()
    


if __name__ == "__main__":
    handleAnalysis()