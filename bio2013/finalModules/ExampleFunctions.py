import math
import CalculateFT as a
import ImplementFunctions as c
import pylab as x
import DisplayExamples as d
import itertools

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
    plotFourierTransform(DoFourierTransform([math.sin],[range(1,1000),range(2,1001)]))

def displayWithParameters(s,a,w,offset,t):
    x.figure(2)
    p = c.Function(a,w,offset,t)
    plotFourierTransform(DoFourierTransform([p],[range(1,s),range(2,s+1)]))
    x.figure(3)
    list = d.GenerateAllData([p],[range(1,s),range(2,s+1)])
    x.plot(plotFourierTransform(list))
    
def displayAll(s=1000, a=1,w=4.2,offset=3,t=.001):
    '''
    displays Fourier transform
    
    parameters:
    -other parameters are from the sin function constructor
    '''
    x.figure(1)
    displayNoParameters()
    x.figure(2)
    displayWithParameters(s,a,w,offset,t)

def displayMultiple():
    x.figure(1)
    displayNoParameters()
    displayWithParameters(1000,1,4.2,3,.001)
    displayWithParameters(1000,1,4.2,3,.01)
    displayWithParameters(500,1,4.2,3,.001)
    