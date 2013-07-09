import math
import CalculateFT as a
import ImplementFunctions as c
import CombineData as b
import pylab as x

def GenerateAllData(listOfFunctions,xValues):
    '''
    calls the GenerateDataForOneFunction method for a list of funcitons and combines data
    '''
    FinalData =[]
    for i in range(0,len(listOfFunctions)):
        x = listOfFunctions[i]
        FinalData.append(GenerateDataForOneFunction(x,xValues))
    return CombineData(FinalData)
    
def GenerateDataForOneFunction(function1,xValues):
    '''
    takes in a function and a list of x values and calculates its y values
    '''
   return [function1(a) for a in b.CombineXData(xValues)]

def CombineData(x):
    '''
    Combines data from 2 lists
    '''
    return [sum(i) for i in zip(*x)]

def DoFourierTransform(listOfFunctions,xValues):
    '''
    Uses the FourierSequence method from the Calculate FT module to generate Fourier Transform data.
    
    Parameters:
    -listOfFunctions-list of functions to get data from
    -xValues- list of x values to apply data to
    '''
    return a.FourierSequence(GenerateAllData(listOfFunctions,xValues))
    
def plotFourierTransform(listOfFunctions,xValues):
    '''
    separates the Fourier Transform Data from the DoFourierTransform method into the real and imaginary components and plots both
    '''
    reals = []
    imag = []
    a = DoFourierTransform(listOfFunctions,xValues)
    for y in a:
        reals.append(y.real)
        imag.append(y.imag)
    x.plot(reals)
    x.plot(imag)