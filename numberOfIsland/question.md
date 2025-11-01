# 🏝️ Number of Islands

Given a 2D grid `grid` where `'1'` represents **land** and `'0'` represents **water**, count and return the **number of islands**.

An **island** is formed by connecting adjacent lands **horizontally or vertically** and is surrounded by water.
You may assume the grid is surrounded by water (i.e., all edges are water).

## 🧩 Example 1

```python
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
Output: 1
```

## 🧩 Example 2

```python
Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
Output: 4
```

## ⚙️ Constraints

* `1 <= grid.length, grid[i].length <= 100`
* `grid[i][j]` is `'0'` or `'1'`

## 🧠 Recommended Time & Space Complexity

* **Time Complexity:** `O(m * n)`
* **Space Complexity:** `O(m * n)`
  where `m` and `n` are the number of rows and columns in the grid.

## 💡 Hints

**Hint 1:**
An island is a group of `'1'`s in which every `'1'` is reachable from any other `'1'` in that group.
Can you think of an algorithm that finds the number of such groups by visiting each group only once?
Maybe there’s a **recursive** way to do it.

**Hint 2:**
You can use **Depth-First Search (DFS)** to traverse each group independently.
Iterate through each cell of the grid — when you encounter a `'1'`, perform DFS starting at that cell and recursively visit every other `'1'` that’s reachable.
Mark visited `'1'`s as `'0'` to avoid revisiting them.
The number of DFS calls corresponds to the number of islands.