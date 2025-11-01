# 🏝️ **Max Area of Island**

You are given a matrix `grid` where `grid[i][j]` is either:

* `0` representing **water**, or
* `1` representing **land**.

An **island** is defined as a group of `1`s connected **horizontally or vertically** (not diagonally).
You may assume that all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells that belong to it.

Return the **maximum area** of any island in the grid.
If no island exists, return `0`.

## 🧩 **Example**

```
Input:
grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6

Explanation:
1's cannot be connected diagonally,
so the maximum area of the island is 6.
```

## 📏 **Constraints**

* 1 ≤ `grid.length`, `grid[i].length` ≤ 50

## ⏱️ **Recommended Time & Space Complexity**

* **Time Complexity:** O(m × n)
* **Space Complexity:** O(m × n)
  where `m` is the number of rows and `n` is the number of columns in the grid.

## 💡 **Hints**

**Hint 1:**
An island is a group of `1`s where every `1` is reachable from any other `1` in that group.
Can you find all such groups by visiting each island only once?
Perhaps a **recursive traversal** could help.

**Hint 2:**
Use **Depth First Search (DFS)** to explore each island.
When you find a `1`, recursively visit all connected `1`s (up, down, left, right) to compute its area.
How would you track which cells were already visited?

**Hint 3:**
Traverse the entire grid:

* When you find a `1`, start a DFS.
* Mark visited cells as `0` to avoid recounting them.
* Count the number of `1`s you visit (that’s the island’s **area**).
* Keep track of the **maximum area** found so far.
  After the traversal, return `maxArea`.