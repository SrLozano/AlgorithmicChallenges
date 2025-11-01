# 🌳 Binary Tree Level Order Traversal 

Given the `root` of a binary tree, return **the level order traversal** of its nodes’ values.
(Level order traversal means visiting all nodes at each depth level from **left to right**.)

## 📘 Example 1

**Input:**
`root = [1,2,3,4,5,6,7]`

**Output:**
`[[1],[2,3],[4,5,6,7]]`

## 📗 Example 2

**Input:**
`root = [1]`

**Output:**
`[[1]]`

## 📙 Example 3

**Input:**
`root = []`

**Output:**
`[]`

## ⚙️ Constraints

* `0 <= number of nodes <= 1000`
* `-1000 <= Node.val <= 1000`

## ⏱️ Recommended Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

> where `n` is the number of nodes in the tree.

## 💡 Hints

**Hint 1:**
🔹 The *level* of a tree refers to nodes that are at the same distance from the root.
Can you think of a way to traverse the tree *level by level* instead of *depth first*?

**Hint 2:**
🧠 Use **Breadth-First Search (BFS)**.
BFS employs a **queue** to explore nodes level by level.
At each step:

1. Iterate over the queue (current level).
2. Add left and right children to the queue.
3. Collect node values in a sublist.

**Hint 3:**
📏 Each BFS iteration corresponds to one *level* of the tree.
Pop all nodes in the queue for the current level, store their values,
and then push their children for the next round.