# 🧩 Unique Paths

There is an `m x n` grid where you are allowed to move **either down** or **to the right** at any point in time.

Given two integers `m` and `n`, return **the number of possible unique paths** that can be taken from the **top-left corner** of the grid (`grid[0][0]`) to the **bottom-right corner** (`grid[m - 1][n - 1]`).

You may assume the output will fit in a **32-bit integer**.

## 🧠 Example 1

**Input:**
`m = 3, n = 6`

**Output:**
`21`

## 🧠 Example 2

**Input:**
`m = 3, n = 3`

**Output:**
`6`

## ⚙️ Constraints

* `1 <= m, n <= 100`

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity:** O(m × n)
* **Space Complexity:** O(m × n)

Where `m` is the number of rows and `n` is the number of columns in the grid.

## 💡 Hints

**Hint 1**
Think recursively. At each cell, you have two choices — move **right** or **down**. What happens when you reach the bottom or rightmost edge?

**Hint 2**
Visualize the grid as a decision tree. Each path branches into two: right and down. Define the base case (e.g., when reaching the last cell).

**Hint 3**
This recursive approach leads to repeated calculations. Can you **optimize it**?

**Hint 4**
Use **Dynamic Programming** (either memoization or tabulation) to store already computed results and avoid recalculations. A 2D array or dictionary can be used for caching.