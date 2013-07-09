import math
import CalculateFT as a
import ImplementFunctions as c
import pylab as x
import DisplayExamples as d

def DoFourierTransform(listOfFunctions,xValues):
    '''
    Uses the FourierSequence method from the Calculate FT module to generate Fourier Transform data.
    
    Parameters:
    -listOfFunctions-list of functions to get data from
    -xValues- list of x values to apply data to
    '''
    return a.FourierSequence(d.GenerateAllData(listOfFunctions,xValues))
    
def plotFourierTransform(FourierData):
    '''
    separates the Fourier Transform Data from the DoFourierTransform method into the real and imaginary components and plots both
    '''
    reals = []
    imag = []
    for y in FourierData:
        reals.append(y.real)
        imag.append(y.imag)
    x.plot(reals)
    x.plot(imag)
    
def displayNoParameters():
    plotFourierTransform(d.DoFourierTransform([math.sin],[range(1,1000),range(2,1001)]))

def displayWithParameters(a,w,offset,t):
    x.figure(2)
    p = c.sinFunction(a,w,offset,t)
    d.plotFourierTransform([p],[range(1,1000),range(2,1001)])
    x.figure(3)
    list = d.GenerateAllData([p],[range(1,1000),range(2,1001)])
    x.plot(list)
    
def displayAll(a,w,offset,t):
    '''
    displays Fourier transform
    
    parameters:
    -other parameters are from the sin function constructor
    '''
    x.figure(1)
    displayNoParameters()
    x.figure(2)
    displayWithParameters(a,w,offset,t)