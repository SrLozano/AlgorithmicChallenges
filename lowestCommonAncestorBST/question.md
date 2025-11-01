# 🌿 Lowest Common Ancestor in a Binary Search Tree

You are given the `root` of a **Binary Search Tree (BST)** where all node values are **unique**, and two nodes `p` and `q` from the tree.

Return the **lowest common ancestor (LCA)** of the two nodes.

The **lowest common ancestor** between two nodes `p` and `q` is the lowest node in the tree such that both `p` and `q` are descendants of that node.

> ⚠️ Note: A node can be a descendant of itself.

## 🧩 Example 1

**Input:**

```
root = [5,3,8,1,4,7,9,null,2]
p = 3
q = 8
```

**Output:**

```
5
```

## 🧩 Example 2

**Input:**

```
root = [5,3,8,1,4,7,9,null,2]
p = 3
q = 4
```

**Output:**

```
3
```

**Explanation:**
The LCA of nodes `3` and `4` is `3`, since a node can be a descendant of itself.

## 📏 Constraints

* `2 <= number of nodes <= 100`
* `-100 <= Node.val <= 100`
* `p != q`
* Both `p` and `q` will exist in the BST

## ⚡️ Recommended Complexity

* **Time Complexity:** `O(h)` — where `h` is the height of the tree
* **Space Complexity:** `O(h)` — recursion stack (or `O(1)` if iterative)

## 💡 Hints

1. 🌲 In a **BST**,

   * All values in the **left subtree** are *less than* the current node’s value.
   * All values in the **right subtree** are *greater than* the current node’s value.
     Use this property to guide your search!

2. 🧭 Use **recursion** (or iteration) to traverse:

   * If both `p` and `q` are smaller than the current node, go **left**.
   * If both are larger, go **right**.
   * Otherwise, the current node is the **split point → LCA**.

3. 🌳 Remember that if the current node equals `p` or `q`, that node itself is the LCA — since a node can be its own ancestor.
