# Graph Valid Tree 🌳

Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

## Example 1: ✅

**Input:**  
`n = 5`  
`edges = [[0, 1], [0, 2], [0, 3], [1, 4]]`

**Output:**  
`true`

## Example 2: ❌

**Input:**  
`n = 5`  
`edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]`

**Output:**  
`false`

## Note: 📝

- You can assume that no duplicate edges will appear in `edges`. Since all edges are undirected, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in `edges`.

## Constraints: ⛓️

- `1 <= n <= 100`
- `0 <= edges.length <= n * (n - 1) / 2`

## Recommended Time & Space Complexity ⏳💾

You should aim for a solution as good or better than **O(V + E)** time and **O(V + E)** space, where `V` is the number of vertices and `E` is the number of edges in the graph.

## Hint 1 💡

According to the definition of a tree, a tree is an undirected graph with no cycles, all the nodes are connected as one component, and any two nodes have exactly one path. Can you think of a recursive algorithm to detect a cycle in the given graph and ensure it is a tree? 🌲

## Hint 2 🔍

We can use the **Depth First Search (DFS)** algorithm to detect a cycle in the graph. Since a tree has only one component, we can start the DFS from any node, say node `0`. During the traversal, we recursively visit its neighbors (children). If we encounter any already visited node that is not the parent of the current node, we return `false` as it indicates a cycle. How would you implement this? 🤔

## Hint 3 🎯

We start DFS from node `0`, assuming `-1` as its parent. We initialize a hash set `visit` to track the visited nodes in the graph. During the DFS, we first check if the current node is already in `visit`. If it is, we return `false`, detecting a cycle. Otherwise, we mark the node as visited and perform DFS on its neighbors, skipping the parent node to avoid revisiting it. After all DFS calls, if we have visited all nodes, we return `true`, as the graph is connected. Otherwise, we return `false` because a tree must contain all nodes. 🌟
