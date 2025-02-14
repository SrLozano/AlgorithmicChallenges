# 🔄 Permutation in String 🔄

## 📜 Problem Description

You are given two strings `s1` and `s2`.

Return `true` if `s2` contains a permutation of `s1`, or `false` otherwise. That means if a permutation of `s1` exists as a substring of `s2`, then return `true`.

Both strings only contain lowercase letters.

### 🌟 Example 1:

**Input:**  
`s1 = "abc"`, `s2 = "lecabee"`  

**Output:**  
`true`  

**Explanation:**  
The substring `"cab"` is a permutation of `"abc"` and is present in `"lecabee"`.  

### 🌟 Example 2:

**Input:**  
`s1 = "abc"`, `s2 = "lecaabee"`  

**Output:**  
`false`  

### 🛑 Constraints:

- `1 <= s1.length, s2.length <= 1000`

---

## ⏳💾 Recommended Time & Space Complexity

You should aim for a solution with **O(n)** time and **O(1)** space, where `n` is the maximum of the lengths of the two strings.

## 💡 Hints 💡

### 🔍 Hint 1  
A brute force solution would be to check every substring of `s2` with `s1` by sorting `s1` as well as the substring of `s2`. This would be an **O(n²)** solution. Can you think of a better way? Maybe we can use the frequency of the characters of both the strings as we did in checking anagrams.

### 🔍 Hint 2  
We return `false` if the length of `s1` is greater than the length of `s2`. To count the frequency of each character in a string, we can simply use an array of size **O(26)**, since the character set consists of `a` through `z` (26 continuous characters). Which algorithm can we use now?

### 🔍 Hint 3  
We use a **sliding window approach** on `s2` with a fixed window size equal to the length of `s1`. To track the current window, we maintain a running frequency count of characters in `s2`. This frequency count represents the characters in the current window. At each step, if the frequency count matches that of `s1`, we return `true`.
