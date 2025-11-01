# 🎓 Course Schedule II

**Status:** ✅ *Solved*

## 🧠 Problem Statement

You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must take **course `b` first** if you want to take **course `a`**.

For example, the pair `[0, 1]` means:

> To take course **0**, you must first take course **1**.

There are a total of `numCourses` courses you are required to take, labeled from `0` to `numCourses - 1`.

Return a **valid ordering** of courses you can take to finish all courses.
If there are multiple valid orders, return **any** of them.
If it’s impossible to finish all courses, return an **empty array** `[]`.

## 🧩 Example 1

**Input:**

```python
numCourses = 3
prerequisites = [[1, 0]]
```

**Output:**

```python
[0, 1, 2]
```

**Explanation:**
We must ensure that course `0` is taken before course `1`.

## 🧩 Example 2

**Input:**

```python
numCourses = 3
prerequisites = [[0,1], [1,2], [2,0]]
```

**Output:**

```python
[]
```

**Explanation:**
There is a **cycle** among the courses — it’s impossible to complete all of them.

## ⚙️ Constraints

* `1 <= numCourses <= 1000`
* `0 <= prerequisites.length <= 1000`
* All prerequisite pairs are **unique**

## ⏱️ Recommended Complexity

* **Time:** `O(V + E)`
* **Space:** `O(V + E)`
  Where:
* `V` = number of courses (nodes)
* `E` = number of prerequisites (edges)

## 💡 Hints

### 🔹 Hint 1

Think of the problem as a **directed graph** 🎯

* Courses are **nodes**
* Prerequisites are **edges** (`b → a`)
  We need to determine whether the graph has a **cycle** (which makes it impossible) and find a **valid order** if it doesn’t.

### 🔹 Hint 2

Use **DFS** to both:

* Detect cycles
* Generate a valid ordering (Topological Sort 🧭)

Alternatively, you can use **Kahn’s Algorithm (BFS)** for topological sorting, where prerequisites act as “parent nodes” for each course.

### 🔹 Hint 3

Compute the **indegree** of every course and perform **BFS**:

1. Start with courses having indegree `0` (no prerequisites).
2. Take each course, reducing the indegree of its dependent courses.
3. Add a dependent course to the queue when its indegree becomes `0`.
4. If all courses are processed, return the order; otherwise, return `[]`.