# 🧩 Clone Graph

## 📘 Problem Statement

Given a node in a **connected undirected graph**, return a **deep copy** of the graph.

Each node in the graph contains an integer value and a list of its neighbors:

```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

The graph is shown in the test cases as an **adjacency list**, where each list describes the set of neighbors of a node in the graph.
For simplicity, node values are numbered from `1` to `n`, where `n` is the total number of nodes in the graph.

The input node will always be the **first node in the graph** and have value `1`.

## 💡 Example 1

```
Input: adjList = [[2],[1,3],[2]]
Output: [[2],[1,3],[2]]

Explanation:
Node 1: val = 1, neighbors = [2]
Node 2: val = 2, neighbors = [1,3]
Node 3: val = 3, neighbors = [2]
```

## 💡 Example 2

```
Input: adjList = [[]]
Output: [[]]
Explanation: The graph has one node with no neighbors.
```

## 💡 Example 3

```
Input: adjList = []
Output: []
Explanation: The graph is empty.
```
## ⚙️ Constraints

* `0 <= Number of nodes <= 100`
* `1 <= Node.val <= 100`
* No duplicate edges or self-loops

## ⏱ Recommended Time & Space Complexity

* **Time:** O(V + E)
* **Space:** O(E)
  Where `V` = number of vertices, `E` = number of edges

## 💭 Hints

### 🧠 Hint 1

We are given only a reference to **one node**.
To clone the **entire graph**, we must also clone all nodes **reachable** from it.
Think recursively — and consider using a **hash map** to store each original node with its cloned version.

### 🧭 Hint 2

We can use **Depth First Search (DFS)**:

* Maintain a map: `{original_node → cloned_node}`
* Create a clone for each node during DFS
* For each neighbor of the current node:

  * Recursively clone the neighbor (if not already cloned)
  * Add the cloned neighbor to the current clone’s neighbor list

### 🚧 Hint 3

Stop the recursion when you reach a node that has **already been cloned** (exists in the map).
Return the cloned node of the starting node after the traversal completes.