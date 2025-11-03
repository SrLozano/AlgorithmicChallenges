# 🧩 Edit Distance

You are given two strings `word1` and `word2`, each consisting of lowercase English letters.

You are allowed to perform **three operations** on `word1` an unlimited number of times:

1. Insert a character at any position
2. Delete a character at any position
3. Replace a character at any position

Return the **minimum number of operations** to make `word1` equal to `word2`.

## 💡 Example 1

**Input:**

```python
word1 = "monkeys"
word2 = "money"
```

**Output:**

```python
2
```

**Explanation:**

```
monkeys -> monkey (remove 's')
monkey -> money (remove 'k')
```

## 💡 Example 2

**Input:**

```python
word1 = "neatcdee"
word2 = "neetcode"
```

**Output:**

```python
3
```

**Explanation:**

```
neatcdee -> neetcdee (replace 'a' with 'e')
neetcdee -> neetcde (remove last 'e')
neetcde -> neetcode (insert 'o')
```

## 📏 Constraints

* `0 <= word1.length, word2.length <= 100`
* `word1` and `word2` consist of lowercase English letters.

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity:** O(m * n)
* **Space Complexity:** O(m * n)

where `m` and `n` are the lengths of `word1` and `word2`, respectively.

## 🧠 Hints

### 🪜 Hint 1

Try to think in terms of recursion and visualize it as a decision tree, as we have choices at each recursion step. Can you determine the recurrence relation and base cases?

### 🧩 Hint 2

We recursively iterate through the strings using indices `i` and `j` for `word1` and `word2`, respectively.
If the characters at the current indices match, we increment both indices without counting an operation.
Otherwise, we have three choices:

* **Insert** the character at the current index of `word1` (increment `j`)
* **Delete** the current character of `word1` (increment `i`)
* **Replace** the character at index `i` in `word1` (increment both `i` and `j`)

### ⚙️ Hint 3

If index `i` goes out of bounds, we return the number of remaining characters in `word2` (using insert operations).
If index `j` goes out of bounds, we return the number of remaining characters in `word1` (using delete operations).
At each step, we return the minimum operation path. This approach is exponential. Can you think of a way to optimize it?

### 🧩 Hint 4

We can use **memoization** to cache results and avoid redundant calculations.
A hash map or a 2D array can be used to store these results.