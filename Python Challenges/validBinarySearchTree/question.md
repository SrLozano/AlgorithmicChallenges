# ✅ Valid Binary Search Tree

Given the root of a binary tree, return `true` if it is a valid binary search tree, otherwise return `false`.

A **valid binary search tree** satisfies the following constraints:

- 🌲 The left subtree of every node contains only nodes with keys **less than** the node's key.
- 🌳 The right subtree of every node contains only nodes with keys **greater than** the node's key.
- 🔄 Both the left and right subtrees are also **binary search trees**.

## 📌 Example 1:

**Input:**  
`root = [2,1,3]`

**Output:**  
`true`


## 📌 Example 2:

**Input:**  
`root = [1,2,3]`

**Output:**  
`false`

**Explanation:**  
The root node's value is `1`, but its left child's value is `2`, which is greater than `1`.


## 🔢 Constraints:

- `1 <=` The number of nodes in the tree `<= 1000`
- `-1000 <=` Node.val `<= 1000`


## ⏳ Recommended Time & Space Complexity

You should aim for a solution with **O(n)** time and **O(n)** space, where `n` is the number of nodes in the given tree.


## 💡 Hints

### 🧐 Hint 1
A **brute force** solution would involve traversing the tree and, for every node, checking its entire left subtree to ensure all nodes are **less** than the current node and its entire right subtree to ensure all nodes are **greater**.  
This results in an **O(n²)** solution. Can you think of a better way? Maybe tracking values during traversal would help. 🤔

### 🚀 Hint 2
We can use **Depth First Search (DFS)** to traverse the tree. At each node, we ensure that the tree rooted at that node is a **valid Binary Search Tree (BST)**.  
One way to do this is by tracking an **interval** that defines the lower and upper limits for the node's value in that subtree.  
This interval will be updated as we move down the tree, ensuring each node adheres to the **BST property**.

### 🔄 Hint 3
We start with the interval **[-∞, ∞]** for the root node.  
- When checking the **left subtree**, we update the **maximum value limit** because all values in the left subtree must be **less than** the current node's value.  
- When checking the **right subtree**, we update the **minimum value limit** because all values in the right subtree must be **greater than** the current node's value.

