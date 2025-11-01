# 🌳 **Binary Tree Maximum Path Sum**

## 💡 Problem

Given the root of a **non-empty binary tree**, return the **maximum path sum** of any non-empty path.

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them.
A node **cannot** appear more than once in a path.
The path **does not necessarily need to include the root**.

The **path sum** is the sum of the node values in that path.

## 🧩 **Examples**

### ✅ Example 1

**Input:**
`root = [1,2,3]`

**Output:**
`6`

**Explanation:**
The path is `2 -> 1 -> 3`, with a sum of `2 + 1 + 3 = 6`.

### ✅ Example 2

**Input:**
`root = [-15,10,20,null,null,15,5,-5]`

**Output:**
`40`

**Explanation:**
The path is `15 -> 20 -> 5`, with a sum of `15 + 20 + 5 = 40`.

## ⚙️ **Constraints**

* `1 <= number of nodes <= 1000`
* `-1000 <= Node.val <= 1000`

## ⏱️ **Recommended Time & Space Complexity**

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`
  where `n` is the number of nodes in the tree.

## 💭 **Hints**

### 🧠 Hint 1

A brute-force approach would check **path sums between every pair of nodes**, resulting in **O(n²)** time.
Instead, consider what **information** you can compute **at each node** to build the maximum path sum efficiently.

### 🧩 Hint 2

At each node, you can have three possible maximum paths:

1. 🌿 **Through both subtrees:** left → node → right
2. 🌱 **Through one subtree only:** node → (left or right)
3. 🌾 **Extending to the parent:** node + one side only (used when returning up the recursion)

The parent will handle combining paths — you just need to return **the best one-branch sum** upward.

### 🧭 Hint 3

Use **Depth-First Search (DFS)** 🧱
At each node:

* Compute the **max path sum** from left and right subtrees.
* Update a **global maximum** with:
  `max(left + node + right, current_global_max)`
* Return `node + max(left, right)` to the parent (only one branch can continue upward).

### ⚡ Hint 4

When computing path sums from left and right,
use `max(0, left_sum)` and `max(0, right_sum)` to **ignore negative paths**,
since extending a negative path only reduces your total.