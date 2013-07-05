import math

def getYValues(function, numbers):
    yValues = []
    for i in numbers:
        yValues.append(function(i))
    return yValues
    
