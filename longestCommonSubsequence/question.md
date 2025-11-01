# 🧵 **Longest Common Subsequence**

Given two strings `text1` and `text2`, return the **length of the longest common subsequence** between the two strings if one exists, otherwise return `0`.

A **subsequence** is a sequence that can be derived from a string by deleting some or no elements without changing the **relative order** of the remaining characters.

For example:
👉 `"cat"` is a subsequence of `"crabt"`.
A **common subsequence** of two strings is one that exists in **both** strings.

## 🧩 **Example 1**

```
Input: text1 = "cat", text2 = "crabt"
Output: 3
Explanation: The longest common subsequence is "cat", which has a length of 3.
```

## 🧩 **Example 2**

```
Input: text1 = "abcd", text2 = "abcd"
Output: 4
```

## 🧩 **Example 3**

```
Input: text1 = "abcd", text2 = "efgh"
Output: 0
```

## 📏 **Constraints**

* `1 <= text1.length, text2.length <= 1000`
* `text1` and `text2` consist of only lowercase English letters (`a-z`).

## ⏱️ **Recommended Time & Space Complexity**

* **Time Complexity:** O(m × n)
* **Space Complexity:** O(m × n)
  where `m = len(text1)` and `n = len(text2)`.

## 💡 **Hints**

**Hint 1:**
Think recursively. Visualize both strings being traversed at the same time.
At each step, decide whether to **include** or **skip** a character based on whether they match.

**Hint 2:**
If characters match → move both pointers forward and add `1`.
If not → explore both possibilities (advance one string at a time) and take the **maximum** result.
This naive recursive solution is **O(2^(m+n))**, but we can **optimize it**!

**Hint 3:**
Use **Memoization** 🧠
Store previously computed results in a **2D array** or **hash map** to avoid recalculating subproblems.
This transforms the solution into **O(m × n)** time.