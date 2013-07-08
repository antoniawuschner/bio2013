import math
import CalculateFT as a
import ImplementFunctions as c
import CombineData as b
import pylab as x

def GenerateAllData(listOfFunctions,xValues):
    FinalData =[]
    for i in range(0,len(listOfFunctions)):
        x = listOfFunctions[i]
        FinalData.append(GenerateDataForOneFunction(x,xValues))
    return CombineData(FinalData)
    
def GenerateDataForOneFunction(function1,xValues):
   return [function1(a) for a in b.CombineData(xValues)]

def CombineData(x):
    return [sum(i) for i in zip(*x)]

def DoFourierTransform(listOfFunctions,xValues):
    return a.FourierSequence(GenerateAllData(listOfFunctions,xValues))
    
def plotFourierTransform(listOfFunctions,xValues):
    reals = []
    imag = []
    a = DoFourierTransform(listOfFunctions,xValues)
    for y in a:
        reals.append(y.real)
        imag.append(y.imag)
    x.plot(reals)
    x.plot(imag)