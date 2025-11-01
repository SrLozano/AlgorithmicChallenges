# 👁️ Binary Tree Right Side View

You are given the root of a binary tree.
Return the **values of the nodes visible from the right side** of the tree, ordered from **top to bottom**.

## 💡 Example 1

**Input:**

```python
root = [1,2,3]
```

**Output:**

```python
[1,3]
```

## 💡 Example 2

**Input:**

```python
root = [1,2,3,4,5,6,7]
```

**Output:**

```python
[1,3,7]
```

## 📏 Constraints

* `0 <= number of nodes in the tree <= 100`
* `-100 <= Node.val <= 100`

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n), where n is the number of nodes in the tree

## 🧠 Hints

### 🪜 Hint 1

In the **right-side view** of a tree, we see only the **nodes visible from the right**.
Try traversing the tree **level by level** to identify which nodes are visible.

### 🧩 Hint 2

The visible nodes are the **last nodes** at each level.
Can you think of an algorithm that processes nodes **level by level**?

### ⚙️ Hint 3

Use **Breadth-First Search (BFS)**:

* Traverse the tree level by level.
* For each level, record the **last node** visited.
* Add these nodes to the result list and return it at the end.
