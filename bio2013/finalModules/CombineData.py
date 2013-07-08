import math
import itertools

def CombineXData(lists):
    result = list(itertools.chain(*lists))
    return result