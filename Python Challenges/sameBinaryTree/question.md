# 🌳 Same Binary Tree

You are given the roots of two binary trees `p` and `q`.
Return **true** if the trees are equivalent, otherwise return **false**.

Two binary trees are considered **equivalent** if they share the **exact same structure** and the **nodes have the same values**.

## 💡 Example 1

**Input:**

```python
p = [1,2,3]
q = [1,2,3]
```

**Output:**

```python
true
```

## 💡 Example 2

**Input:**

```python
p = [4,7]
q = [4,null,7]
```

**Output:**

```python
false
```

## 💡 Example 3

**Input:**

```python
p = [1,2,3]
q = [1,3,2]
```

**Output:**

```python
false
```

## 📏 Constraints

* `0 <= number of nodes in both trees <= 100`
* `-100 <= Node.val <= 100`

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n), where n is the number of nodes in the tree

## 🧠 Hints

### 🪜 Hint 1

Can you think of an algorithm commonly used to **traverse** a tree? Perhaps **recursion** might help.

### 🧩 Hint 2

We can use **Depth-First Search (DFS)** to traverse both trees **simultaneously**.

### ⚙️ Hint 3

Start traversal from both roots:

* If both nodes are `null`, they match.
* If only one is `null` or their values differ → return `false`.
* Otherwise, recursively compare **left** and **right** subtrees.
  If all recursive calls return true, the trees are identical.