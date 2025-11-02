# 🧩 Longest Palindromic Substring

Given a string `s`, return the **longest substring** of `s` that is a **palindrome**.

A **palindrome** is a string that reads the same forward and backward.
If there are multiple palindromic substrings of the same length, return **any one** of them.

## 💡 Example 1

**Input:**

```python
s = "ababd"
```

**Output:**

```python
"bab"
```

**Explanation:**
Both `"aba"` and `"bab"` are valid palindromic substrings of maximum length.

## 💡 Example 2

**Input:**

```python
s = "abbc"
```

**Output:**

```python
"bb"
```

## 📏 Constraints

* `1 <= s.length <= 1000`
* `s` contains only digits and English letters.

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity:** O(n²)
* **Space Complexity:** O(1)

## 🧠 Hints

### 🪜 Hint 1

A brute-force solution would check **every substring** and see if it’s a palindrome — an **O(n³)** approach.
Can you think of a more efficient way?
💡 Try thinking in terms of the **center of a palindrome**.

### 🧩 Hint 2

Iterate over each index `i` in the string and treat it as the **center**.
From each center, expand **outward** to the left and right **while both characters match**.
This gives the length of the palindrome centered at `i`.
Remember to check both **odd-length** and **even-length** palindromes.

### ⚙️ Hint 3

Maintain two variables:

* `resLen` → length of the longest palindrome found
* `res` → starting index of that palindrome

For **odd-length** palindromes, expand from `(i - 1, i + 1)`.
For **even-length** palindromes, expand from `(i, i + 1)`.
Whenever a longer palindrome is found, update your result variables.

Finally, return the substring starting at `res` with length `resLen`.