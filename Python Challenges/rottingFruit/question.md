# 🧩 Rotting Fruit

You are given a 2D matrix `grid`.
Each cell can have one of three possible values:

* `0` → Empty cell
* `1` → Fresh fruit
* `2` → Rotten fruit

Every minute, if a **fresh fruit** is horizontally or vertically adjacent to a **rotten fruit**, then the fresh fruit also becomes rotten.

Return the **minimum number of minutes** that must elapse until there are **zero fresh fruits remaining**.
If this state is **impossible**, return `-1`.

## 💡 Example 1

**Input:**

```python
grid = [
  [1,1,0],
  [0,1,1],
  [0,1,2]
]
```

**Output:**

```python
4
```

## 💡 Example 2

**Input:**

```python
grid = [
  [1,0,1],
  [0,2,0],
  [1,0,1]
]
```

**Output:**

```python
-1
```

## 📏 Constraints

* `1 <= grid.length, grid[i].length <= 10`

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity:** O(m × n)
* **Space Complexity:** O(m × n)

## 🧠 Hints

### 🪜 Hint 1

The **DFS** algorithm is **not suitable** for this problem because it explores nodes deeply rather than level by level.
Here, we need to simulate minute-by-minute spread, which naturally fits **level-order traversal**.
Can you think of an algorithm designed for that?

### 🧩 Hint 2

Use **Breadth-First Search (BFS)**.
At each minute, rot all fresh fruits adjacent to currently rotten ones.
Store rotten fruits in a **queue** and process them level by level.
The minute a fruit becomes rotten corresponds to its BFS level.

### ⚙️ Hint 3

1. Traverse the grid and **enqueue** all rotten fruits.
2. Perform **BFS**:

   * For each rotten fruit, check its four neighbors.
   * If a neighbor is a fresh fruit, mark it rotten and add it to the queue.
3. Continue until the queue is empty.
4. Finally, traverse the grid again:

   * If any fresh fruit remains, return `-1`.
   * Otherwise, return the last BFS level (the total minutes elapsed).