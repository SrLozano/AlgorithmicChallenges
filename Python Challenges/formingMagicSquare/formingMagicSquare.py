#!/bin/python3

#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

'''All possible 3x3 matrixes of integers that fulfil the conditions
to be considered a magic square'''
magicSquares = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],        
]

def formingMagicSquare(s):
    '''The function checks the given matrix with all the possible magic squares
    and returns the minimun cost to get one of them'''
    
    minimal_cost = float("inf") # infinite
    
    for magic_square in magicSquares:
        aux = 0
        for i in range(0, len(s)):
            for j in range(0, len(s[i])):
                aux = aux + abs(s[i][j] - magic_square[i][j])
        if aux < minimal_cost:
            minimal_cost = aux
            
    return minimal_cost

# Matrix passed as an argument to formingMagicSquare. Result: 4
s = [[4, 8, 2],
     [4, 5, 7],
     [6, 1, 6]]

result = formingMagicSquare(s)

print("The proposed matrix is:")
print("\n" + str(s[0]) + "\n" + str(s[1]) + "\n" + str(s[2]) + "\n")
print("The minimal cost is: " + str(result))