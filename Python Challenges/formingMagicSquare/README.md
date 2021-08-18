# formingMagicSquare
A magic square is an nxn matrix of distinct positive integers from 1 to n^2 where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.

The problem gives you a 3x3 matrix of integers in the inclusive range [1, 9]. You can convert any digit a to any other digit b in the range [1, 9] at cost of |a - b|. Given s, convert it into a magic square at a minimal cost. 
## Solution 
Let's solve this problem by finding all possible magic squares and hard-code them into the solution.

### Finding all possible magic squares
First, let's demonstrate that **all 3x3 magic squares have a 5 in the centre**.

Let's call the centre value 'C'. Let's call the sum of all other values 'X'. A 3x3 magic square contains all numbers from 1 to 9. So **the sum of the values of a 3x3 magic square is 45** (= 1 + 2 + ... + 8 + 9).

Therefore,

C + X= 45

In addition, the sum of the numbers on each row, column, and diagonal has to be 15 (the magical number). Now, consider the sum of the middle row, the middle column, and the two diagonals. They add to 60 (= 4 * 15). And this sum is equivalent to adding all the numbers in the square once and four times the central number.

Therefore,

4 * C + X= 60 

From equations 1 and 2, we infer C = 5. Hence, all 3x3 magic squares have a 5 in the centre.

After that, we want to demonstrate that **corner values are always even numbers**.

Since we necessarily have a 5 in the centre, it follows that each row, column, and diagonal that comprises this five will have two other numbers that add to 10. Hence we can establish candidate pairs:

(1, 9)
(2, 8)
(3, 7)
(4, 6)

Notice that two of these pairs have odd numbers and two have even numbers.

Imagine we place one of the odd pairs on a diagonal. We would then have an odd number in one of the top corners. Consider the first row (starting from the top). Since it already has an odd number in a corner, and the row has to sum to 15, the two other numbers both need to be odd, or both even. But we don't have enough odd pairs (we only have one left). And neither do we have enough even pairs, because if we place two of these vertically, then we have none left for the column containing the odd corner number. Hence, we reach a contradiction. This implies that our original hypothesis was incorrect. Namely, the corner numbers can't be odd, and therefore, should be even.

Since we have two even pairs, there are 4 ways to place the first pair in the corners (for example, the (2, 8) pair can be placed with the 2 in the top-left, top-right, bottom-left, bottom-right). And for each of those 4 positions, there are two ways to place the second pair. Hence, 8 in total.

Once the corner pairs have been placed, there is only one way to place the remaining numbers.

Therefore, we have demonstrated that there are 8 different 3x3 magic squares. And we know how to generate them. This 8 different magic squares are: 

    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],   