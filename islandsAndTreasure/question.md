# 🧩 Islands and Treasure

You are given an `m × n` 2D grid initialized with these three possible values:

* `-1` → A **water cell** that cannot be traversed.
* `0` → A **treasure chest**.
* `INF` → A **land cell** that can be traversed.
  *(We use the integer `2^31 - 1 = 2147483647` to represent `INF`.)*

Fill each land cell with the **distance to its nearest treasure chest**.
If a land cell **cannot reach a treasure chest**, its value should remain `INF`.

You can move **up, down, left, or right**.
Modify the grid **in-place**.

## 💡 Example 1

**Input:**

```python
[
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
```

**Output:**

```python
[
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
```

## 💡 Example 2

**Input:**

```python
[
  [0,-1],
  [2147483647,2147483647]
]
```

**Output:**

```python
[
  [0,-1],
  [1,2]
]
```

## 📏 Constraints

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 100`
* `grid[i][j] ∈ {-1, 0, 2147483647}`

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity:** O(m × n)
* **Space Complexity:** O(m × n)

## 🧠 Hints

### 🪜 Hint 1

A brute-force solution would be to iterate over each land cell and run a BFS to find the nearest treasure chest.
This results in **O((m × n)²)** time — too slow.
Can you think of a better way?
💡 *Sometimes it’s not optimal to go from source → destination.*

### 🧩 Hint 2

Instead of running BFS from each cell, **run BFS from all treasure chests simultaneously**!
This is known as **Multi-Source BFS**.
Each treasure chest spreads out level by level, marking the shortest distance automatically.
You never need to revisit a cell.

### ⚙️ Hint 3

Steps:

1. Insert all treasure chest cells `(r, c)` into a queue.
2. Process the queue **level by level**.
3. For each cell, mark its distance.
4. Add adjacent land cells to the queue **only if unvisited**.

This ensures every land cell gets filled with its shortest distance to a treasure chest.