import math
import itertools

def CombineXData(lists):
    '''
    Takes in a list of several series of x values and combines them into one list
    Paremeters:
        -list of lists of x values
        - ex. ([[1,2,3],[2,3,4],[3,4,5]])
    '''
    result = list(itertools.chain(*lists))
    return result