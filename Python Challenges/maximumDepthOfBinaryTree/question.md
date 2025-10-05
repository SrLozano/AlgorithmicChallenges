# 🌲 Maximum Depth of Binary Tree

Given the `root` of a binary tree, return its **maximum depth**.

The **depth** of a binary tree is defined as the number of nodes along the **longest path** from the root node down to the farthest leaf node.

## 🧩 Example 1

**Input:**

```
root = [1,2,3,null,null,4]
```

**Output:**

```
3
```

## 🧩 Example 2

**Input:**

```
root = []
```

**Output:**

```
0
```

## 📏 Constraints

* `0 <= number of nodes <= 100`
* `-100 <= Node.val <= 100`

## ⚡️ Recommended Complexity

* **Time Complexity:** `O(n)` — visit each node once
* **Space Complexity:** `O(n)` — due to recursion or the stack (worst case in a skewed tree)

## 💡 Hints

1. 🧠 Think recursively — the maximum depth at a node is **1 + the maximum depth of its subtrees**.
2. 🌿 Use **Depth-First Search (DFS)**:

   * Compute the maximum depth of the left and right children.
   * Return `1 + max(left_depth, right_depth)`.
3. ➕ The `+1` counts the current node itself in the depth.