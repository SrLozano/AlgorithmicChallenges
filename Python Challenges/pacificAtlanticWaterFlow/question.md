# 🌊 Pacific Atlantic Water Flow

**Solved**

You are given a rectangular island `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

The island borders:

* 🌊 **Pacific Ocean** from the **top** and **left** sides
* 🌊 **Atlantic Ocean** from the **bottom** and **right** sides

Water can flow **up, down, left, or right** from a cell to a neighboring cell **with height equal or lower**.
Water can also flow **into the ocean** from cells adjacent to the ocean.

Return all cells **[r, c]** from which water can flow to **both** the Pacific and Atlantic oceans.
You may return the answer in any order.

## 💡 Example 1

**Input:**

```python
heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
```

**Output:**

```python
[[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
```

## 💡 Example 2

**Input:**

```python
heights = [[1],[1]]
```

**Output:**

```python
[[0,0],[0,1]]
```

## 📏 Constraints

* `1 <= heights.length, heights[r].length <= 100`
* `0 <= heights[r][c] <= 1000`

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity:** O(m × n)
* **Space Complexity:** O(m × n)
  Where **m** = number of rows and **n** = number of columns in the grid.

## 🧠 Hints

### 🪜 Hint 1

A **brute-force** solution would run BFS from each cell to check if it can reach both oceans —
this would be **O((m × n)²)**.
Can you think of a **reverse way** to traverse instead?

### 🌧️ Hint 2

Use **DFS** (or BFS) starting from the **border cells** connected to each ocean.

* For the **Pacific Ocean** (top and left borders):
  Run DFS and mark reachable cells in a set called `pacific`.

* For the **Atlantic Ocean** (bottom and right borders):
  Run DFS and mark reachable cells in a set called `atlantic`.

💡 **Reversal insight:**
When exploring, move **to cells with equal or higher height** (reverse of the water flow direction).
Finally, the cells that exist in **both** sets can flow to **both oceans**.

### 🌎 Hint 3

1. Perform DFS from each ocean’s border, filling their respective sets (`pacific`, `atlantic`).
2. In each DFS, only move to:

   * Valid (in-bounds) neighboring cells, and
   * Cells with **height ≥ current cell’s height** (since we’re reversing the flow).
3. After both DFS passes, iterate over all cells —
   any cell found in **both sets** is part of the result.