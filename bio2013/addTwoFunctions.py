import math

def addTwoFunctions(function1,function2,x,y):
    a = map(function1,range(x,y))
    b = map(function2,range(x,y))
    addedValues = []
    for i in range(0,len(a)):
        addedValues.append(a[i] + b[i])
    return addedValues
        