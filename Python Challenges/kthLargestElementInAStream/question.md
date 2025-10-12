# 🏆 Kth Largest Element in a Stream

## 📘 Problem Statement

Design a class to find the **k-th largest integer** in a stream of values (including duplicates).
For example, the 2nd largest from `[1, 2, 3, 3]` is `3`.
The stream is **not necessarily sorted**.

Implement the following methods:

* `constructor(int k, int[] nums)` → Initializes the object with integer `k` and the stream of integers `nums`.
* `int add(int val)` → Adds integer `val` to the stream and returns the k-th largest integer in the stream.

## 💡 Example 1

**Input:**

```
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
```

**Output:**

```
[null, 3, 3, 3, 5, 6]
```

**Explanation:**

```python
KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3])
kthLargest.add(3)  # → 3
kthLargest.add(5)  # → 3
kthLargest.add(6)  # → 3
kthLargest.add(7)  # → 5
kthLargest.add(8)  # → 6
```

## 📏 Constraints

* 1 ≤ k ≤ 1000
* 0 ≤ nums.length ≤ 1000
* -1000 ≤ nums[i] ≤ 1000
* -1000 ≤ val ≤ 1000
* There will always be **at least k integers** in the stream when searching for the k-th largest.

## ⚙️ Recommended Time & Space Complexity

* **Time Complexity:** O(m log k)

  * where *m* is the number of `add()` calls
* **Space Complexity:** O(k)

  * for maintaining the k largest elements in the heap

## 🧭 Hint 1

A brute force approach would sort the entire array on each `add()` call and pick the k-th largest —
that’s **O(m × n log n)** 😬.
But do we really need to keep *all* numbers if we only care about the top *k*?

## 🪜 Hint 2

Use a **Min-Heap**!

* It keeps the **smallest element** at the top.
* Inserting a new value → O(log k)
* Getting the smallest → O(1)

Think about how this property can help us maintain just the top `k` elements.

## 💡 Hint 3

The **k-th largest element** is simply the **smallest among the top k elements**.
So:

1. Keep a Min-Heap of size `k`.
2. Each time you add a new number:

   * Push it into the heap.
   * If the heap size exceeds `k`, pop the smallest element.
3. The element at the top (`heap[0]`) is your **k-th largest**!

## 🧱 Hint 4

Algorithm summary:

1. Initialize a Min-Heap from `nums`.
2. While the heap size > `k`, pop elements until only `k` remain.
3. For each `add(val)` call:

   * Push `val` into the heap.
   * If the heap size > `k`, pop the smallest.
   * Return `heap[0]`.