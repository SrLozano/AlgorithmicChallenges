#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxMin' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY operations
#  2. INTEGER_ARRAY x
#

def maxMin(operations, x):
    aux = [] #auxiliar array to save the numbers from x
    result = [] #an array to save the result of each multiplication
    
    for i in range(0, len(operations)): #for each operation we select the type of operation
        if operations[i] == "push":
            aux.append(x[i])
        else:
            aux.remove(x[i])
        minimum = min(aux)
        maximum = max(aux)
        result.append(minimum*maximum)
    return result    


operations = ["push", "push", "push", "pop"]
x = [1, 2, 3, 1]
result_arr = maxMin(operations, x)
print("The result of the operations on the selected array is: " + str(result_arr))
