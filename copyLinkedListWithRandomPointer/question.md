# Copy Linked List with Random Pointer 🎯📝

You are given the `head` of a linked list of length `n`. Unlike a singly linked list, each node contains an additional pointer `random`, which may point to any node in the list, or `null`. 🧐

Create a **deep copy** of the list. 🛠️

The deep copy should consist of exactly `n` new nodes, each including:

- The original value `val` of the copied node
- A `next` pointer to the new node corresponding to the `next` pointer of the original node
- A `random` pointer to the new node corresponding to the `random` pointer of the original node

**Note:** None of the pointers in the new list should point to nodes in the original list. 🚫

Return the `head` of the copied linked list. 🔄

In the examples, the linked list is represented as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where `random_index` is the index of the node (0-indexed) that the `random` pointer points to, or `null` if it does not point to any node. 📋

## Example 1:

![Local Image](images/example_1.png "Local Image")


**Input:** `head = [[3,null],[7,3],[4,0],[5,1]]`

**Output:** `[[3,null],[7,3],[4,0],[5,1]]`

## Example 2:

![Local Image](images/example_2.png "Local Image")

**Input:** `head = [[1,null],[2,2],[3,2]]`

**Output:** `[[1,null],[2,2],[3,2]]`

## ⚓️ Constraints:

- `0 <= n <= 100`
- `-100 <= Node.val <= 100`
- `random` is `null` or is pointing to some node in the linked list.

## 🕒 Recommended Time & Space Complexity

You should aim for a solution as good or better than **O(n)** time and **O(n)** space, where `n` is the length of the given list. ⏳

## 💡 Hints

### Hint 1

There is an extra `random` pointer for each node, and unlike the `next` pointer, which points to the next node, the `random` pointer can point to any random node in the list. A deep copy is meant to create completely separate nodes occupying different memory. Why can't we build a new list while iterating through the original list? 🤔

### Hint 2

Because, while iterating through the list, when we encounter a node and create a copy of it, we can't immediately assign the `random` pointer's address. This is because the `random` pointer might point to a node that has not yet been created. To solve this, we can first create copies of all the nodes in one iteration. However, we still can't directly assign the `random` pointers since we don't have the addresses of the copies of those `random` pointers. Can you think of a data structure to store this information? Maybe a hash data structure could help. 🗂️

### Hint 3

We can use a hash data structure, such as a hash map, which takes **O(1)** time to retrieve data. This can help by mapping the original nodes to their corresponding copies. This way, we can easily retrieve the copy of any node and assign the `random` pointers in a subsequent pass after creating copies of all nodes in the first pass. 🗺️
