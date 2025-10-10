# 🎓 Course Schedule

You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that **you must take course `b` before course `a`**.

* Example: `[0, 1]` means you must take course **1 ➡️ 0**.
* There are a total of `numCourses` courses, labeled from `0` to `numCourses - 1`.

Return **`true` ✅** if it’s possible to finish all courses,
or **`false` ❌** if it’s impossible (due to circular dependencies).

## 🧩 Example 1

**Input:**

```python
numCourses = 2
prerequisites = [[0, 1]]
```

**Output:**

```python
true
```

**Explanation:**
Take course **1** first (no prerequisites), then take **0**.

## 🔁 Example 2

**Input:**

```python
numCourses = 2
prerequisites = [[0, 1], [1, 0]]
```

**Output:**

```python
false
```

**Explanation:**
To take course **1**, you need **0** first — but to take **0**, you need **1**.
That’s a **cycle 🔄**, so it’s impossible to complete all courses.

## 📏 Constraints

* `1 <= numCourses <= 1000`
* `0 <= prerequisites.length <= 1000`
* `prerequisites[i].length == 2`
* `0 <= a[i], b[i] < numCourses`
* All prerequisite pairs are **unique**

## ⚙️ Recommended Complexity

* **Time:** `O(V + E)`
* **Space:** `O(V + E)`
  where
  `V` = number of courses (nodes),
  `E` = number of prerequisites (edges)

## 💡 Hints

### 🧠 Hint 1

Model the problem as a **directed graph**:

* Courses → **nodes**
* Prerequisites → **directed edges**

If there’s a **cycle**, some courses depend on each other — making it **impossible** to finish.

### 🔍 Hint 2

Use **Depth-First Search (DFS)** to detect cycles:

* Keep a `path` set for nodes in the current DFS call
* If you revisit a node in `path`, you’ve found a **cycle 🔄**

### 🧭 Hint 3

During DFS:

1. If the current node is already in `path`, return `False`
2. Recursively visit all neighbors
3. If any neighbor detects a cycle, stop early
4. When finished safely, remove the node from `path` to backtrack

Optionally, you can **clear the adjacency list** of fully processed nodes to skip them next time for efficiency.