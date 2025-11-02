# 🧩 Palindromic Substrings

Given a string `s`, return the **number of substrings** within `s` that are **palindromes**.

A **palindrome** is a string that reads the same forward and backward.

## 💡 Example 1

**Input:**

```python
s = "abc"
```

**Output:**

```python
3
```

**Explanation:**
The palindromic substrings are `"a"`, `"b"`, and `"c"`.

## 💡 Example 2

**Input:**

```python
s = "aaa"
```

**Output:**

```python
6
```

**Explanation:**
The palindromic substrings are `"a"`, `"a"`, `"a"`, `"aa"`, `"aa"`, and `"aaa"`.

> Note: Different substrings are counted separately even if they have the same content.

## 📏 Constraints

* `1 <= s.length <= 1000`
* `s` consists of lowercase English letters.

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity:** O(n²)
* **Space Complexity:** O(1)

## 🧠 Hints

### 🪜 Hint 1

A brute-force approach would check **every substring** to see if it’s a palindrome, giving **O(n³)** time.
Can you do better? Try thinking in terms of the **center** of each palindrome.

### 🧩 Hint 2

Iterate over each index `i` in the string and treat it as the **center** of a palindrome.
Expand outward to the left and right **as long as both characters match**.
For every valid expansion, **increment the palindrome count**.
Make sure to check both **odd-length** and **even-length** palindromes.

### ⚙️ Hint 3

Maintain a counter `res` to store the total number of palindromes found.
For **odd-length** palindromes, expand from `(i - 1, i + 1)`.
For **even-length** palindromes, expand from `(i, i + 1)`.

### 💫 Hint 4

This **center expansion** technique efficiently finds all palindromic substrings in **O(n²)** time and **O(1)** space —
a major improvement over the brute-force approach.