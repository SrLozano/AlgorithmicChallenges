#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumSwaps' function below.
#
# The function is expected to return an integer.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#


def minimumSwaps(arr):
    '''
    We iterate over the array, if the element is not in its correct position
    we swap it with the element that is in its correct position. We repeat this
    process until the element is in its correct position. We count the number of
    swaps and return it.
    '''

    swaps = 0
    index = 0
    
    while index < len(arr):
        if arr[index] != index + 1:
            # Swap element with its correct position
            aux = arr[index]
            arr[index] = arr[aux - 1] 
            arr[aux - 1] = aux  
            swaps += 1
        else:
            index += 1
            
    return swaps


if __name__ == "__main__":
    
    arr = [7, 1, 3, 2, 4, 5, 6]
    min_swaps = minimumSwaps(arr)

    print("The minimum number of swaps is: " + str(min_swaps))