# 🌳 **Balanced Binary Tree**

Given a binary tree, return `true` if it is **height-balanced** and `false` otherwise.

A **height-balanced binary tree** is defined as a binary tree in which the left and right subtrees of every node differ in height by **no more than 1**.

## 🧩 **Example 1**

```
Input: root = [1,2,3,null,null,4]
Output: true
```

## 🧩 **Example 2**

```
Input: root = [1,2,3,null,null,4,null,5]
Output: false

## 🧩 **Example 3**

```
Input: root = []
Output: true
```

## 📏 **Constraints**

* The number of nodes in the tree is in the range `[0, 1000]`.
* `-1000 <= Node.val <= 1000`

## ⏱️ **Recommended Time & Space Complexity**

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)
  where `n` is the number of nodes in the tree.

## 💡 **Hints**

**Hint 1:**
A brute-force solution would compute the height for every node separately — resulting in **O(n²)** time.
Can you avoid recomputing heights by combining balance-checking and height calculation in **one DFS traversal**?

**Hint 2:**
Use **Depth-First Search (DFS)** to compute heights as you go.
While calculating the left and right subtree heights:

* If `abs(leftHeight - rightHeight) > 1`, mark the tree as **unbalanced**.
* Return the height of the current node as `1 + max(leftHeight, rightHeight)`.

At the end of traversal, a global flag or return value will indicate whether the tree is balanced. 🌿