#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'calculateAmount' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def calculateAmount(prices): 
    result = 0
    arr_discount = [] #array of discounts that can be eligible
    #for each element in price we decide wheter it can have a discount or not
    for element_price in prices:
        if len(arr_discount) != 0: 
            discount = min(arr_discount)
        else: #Edge limit refering to a list of prices with just one element
            discount = 0    
        if (element_price - discount) >= 0: #A discount can not create a negative price     
            result = result + (element_price - discount)  
        arr_discount.append(element_price)
    return result

while(1):
    print("Welcome to our discount calculator")
    print("Please insert a list of prices, whenever you want to stop just select number -1")
    condition = True
    prices = []
    while(condition):
        number_introduced = int(input("Enter the price of the item "))
        if number_introduced == -1:
            condition = False
            if len(prices) != 0:
                result = calculateAmount(prices)
                print("The result is: " + str(result))
                print("")
            else:
                print("The list can not be empty")
        else:
            print("The price has been inserted")
            prices.append(number_introduced)