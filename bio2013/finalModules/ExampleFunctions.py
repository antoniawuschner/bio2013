import math
import CalculateFT as a
import ImplementFunctions as c
import CombineData as b
import pylab as x
import DisplayExamples as d

def displayNoParameters():
    d.plotFourierTransform([math.sin],[range(1,1000),range(2,1001)])

def displayWithParameters(a,w,offset,t):
    x.figure(2)
    p = c.sinFunction(a,w,offset,t)
    d.plotFourierTransform([p],[range(1,1000),range(2,1001)])
    x.figure(3)
    a = d.GenerateAllData([p],[range(1,1000),range(2,1001)])
    x.plot(a)
    
def displayAll(a,w,offset,t):
    '''
    displays Fourier transform
    
    parameters:
    -other parameters are from the sin function constructor
    '''
    x.figure(1)
    displayNoParameters()
    displayWithParameters(a,w,offset,t)