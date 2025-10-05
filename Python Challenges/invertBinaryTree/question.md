# 🌲 Invert Binary Tree

Given the `root` of a binary tree, **invert** the tree, and return *its root*.

Inverting a binary tree means swapping the left and right children of **every** node in the tree.

## 🧩 Example 1

**Input:**

```
    4
   / \
  2   7
 / \ / \
1  3 6  9
```

**Output:**

```
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

## 🧩 Example 2

**Input:**

```
root = [2,1,3]
```

**Output:**

```
[2,3,1]
```

## 🧩 Example 3

**Input:**

```
root = []
```

**Output:**

```
[]
```

## 📏 Constraints

* The number of nodes in the tree is in the range `[0, 100]`
* `-100 <= Node.val <= 100`


## ⚡️ Recommended Complexity

* **Time Complexity:** `O(n)` — each node is visited once
* **Space Complexity:** `O(h)` — where `h` is the height of the tree (for recursion stack)

## 💡 Hints

1. 🔄 Try recursively swapping the left and right children of each node.
2. 🧠 You can solve it using either **recursion** or **iteration** (with a queue or stack).
3. 🌐 For each node:

   ```
   left, right = right, left
   ```

   Then repeat the process for the subtrees.