import math
import CalculateFT as a
import CombineData as b
import ImplementFunctions as c

def GenerateAllData(listOfFunctions,xValues):
    FinalData =[]
    for i in range(0,len(listOfFunctions):
        x = listOfFunctions[i]
        FinalData.append(GenerateDataForOneFunction(x,b.CombineData(xValues)))
    return CombineData(FinalData)
    
def GenerateDataForOneFunction(function1,xValues):
   return [Function1(a) for a in b.CombineData(xValues)]

def CombineData(x):
    return [sum(i) for i in zip(*x)]

def DoFourierTransform():
    return a.FourierSequence(FinalData)