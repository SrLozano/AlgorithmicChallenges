# 🔠 Longest Repeating Character Replacement

You are given a string `s` consisting of only uppercase English characters and an integer `k`.
You can choose up to `k` characters of the string and replace them with any other uppercase English character.

After performing at most `k` replacements, return the length of the longest substring which contains only one distinct character.

## 💡 Example 1

**Input:**

```python
s = "XYYX", k = 2
```

**Output:**

```python
4
```

**Explanation:**
Either replace the `'X'` characters with `'Y'`, or replace the `'Y'` characters with `'X'`.

## 💡 Example 2

**Input:**

```python
s = "AAABABB", k = 1
```

**Output:**

```python
5
```

## 📏 Constraints

* `1 <= s.length <= 1000`
* `0 <= k <= s.length`

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(m), where m is the number of unique characters in the string

## 🧠 Hints

### 🪜 Hint 1

Which characters would you replace in a string to make all its characters identical?
Think in terms of the **frequency** of characters.

### 🧩 Hint 2

It is always optimal to replace characters with the **most frequent character** in the substring.
This minimizes the number of replacements required.

### ⚙️ Hint 3

The number of replacements = `window_length - frequency_of_most_frequent_char`.
A brute-force approach would check all substrings (O(n²)), but we can do better!

### 🚀 Hint 4

Use a **sliding window** that expands and shrinks dynamically:
Shrink the window when replacements exceed `k`, and track the **maximum window size** seen.