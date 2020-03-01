#!/bin/python3

import os

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    result = "NO"
    mySet = {*()} #An empty set that it is going to be used in order not to get timeout errors
    for i in range(0, len(s1)):
        if not(s1[i] in mySet):
            mySet.update(s1[i])
            for j in range(0, len(s2)):
                if s1[i] == s2[j]:
                    result = "YES"
                    break
    return result    

print("Welcome to the SubStrings calculator.")

while(1):
    print("Enter two strings and you will get YES is the strings have common substrings.")
    s1 = input("String Nº1: ")
    s2 = input("String Nº2: ")
    result = twoStrings(s1, s2)
    print("Great, now wait while the calculator works")
    print("The result is: " + result)
    print()

