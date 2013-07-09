import math

def GenerateAllData(listOfFunctions,xValues):
    '''
    calls the GenerateDataForOneFunction method for a list of functions and combines data
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
    return [function1(a) for a in CombineXData(xValues)]

def CombineData(x):
    '''
    Combines data from 2 lists
    '''
    return [sum(i) for i in zip(*x)]

def CombineXData(lists):
    '''
    Takes in a list of several series of x values and combines them into one list
    Paremeters:
        -list of lists of x values
        - ex. ([[1,2,3],[2,3,4],[3,4,5]])
    '''
    result = list(itertools.chain(*lists))
    return result
