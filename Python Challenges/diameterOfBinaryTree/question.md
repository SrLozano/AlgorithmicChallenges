# 🌐 Diameter of Binary Tree

The **diameter** of a binary tree is the **length of the longest path** between any two nodes in the tree.

> ⚠️ The path **does not necessarily have to pass through the root**, and it is measured in **edges**, not nodes.
> Each path must be **simple** — it cannot include the same node twice.

Given the `root` of a binary tree, return its **diameter**.

## 🧩 Example 1

**Input:**

```
root = [1, null, 2, 3, 4, 5]
```

**Output:**

```
3
```

**Explanation:**
The longest paths are `[1, 2, 3, 5]` or `[5, 3, 2, 4]`, each with a length of **3 edges**.

## 🧩 Example 2

**Input:**

```
root = [1, 2, 3]
```

**Output:**

```
2
```

## 📏 Constraints

* `1 <= number of nodes <= 100`
* `-100 <= Node.val <= 100`

## ⚡️ Recommended Complexity

* **Time Complexity:** `O(n)` — each node is visited once
* **Space Complexity:** `O(n)` — recursion stack in the worst case (for a skewed tree)

## 💡 Hints

1. 🌲 The **diameter** of a tree is the **maximum sum** of the left and right subtree heights for any node.

2. 🧭 The **longest path** may or may not pass through the root — it can be anywhere in the tree.

3. 🐢 A brute-force approach that computes the height for every node separately would take `O(n²)`. Can you compute the **height and diameter in a single DFS traversal**?

4. ⚙️ Using **Depth-First Search (DFS)**:

   * For each node, get:

     ```
     leftHeight, rightHeight
     diameter_at_node = leftHeight + rightHeight
     ```
   * Update a global variable to track the **maximum diameter** found so far.
   * Return `1 + max(leftHeight, rightHeight)` as the height to the parent call.