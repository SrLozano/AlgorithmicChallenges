# 🧩 Valid Sudoku

You are given a 9 x 9 Sudoku board `board`.
A Sudoku board is **valid** if the following rules are followed:

1. Each **row** must contain the digits 1–9 without duplicates.
2. Each **column** must contain the digits 1–9 without duplicates.
3. Each of the nine **3 x 3 sub-boxes** of the grid must contain the digits 1–9 without duplicates.

Return `true` if the Sudoku board is valid, otherwise return `false`.

> **Note:** The board does not need to be full or solvable to be valid.

## 💡 Example 1

**Input:**

```python
board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
]
```

**Output:**

```python
true
```

## 💡 Example 2

**Input:**

```python
board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
]
```

**Output:**

```python
false
```

**Explanation:**
There are two `1`s in the top-left 3x3 sub-box.

## 📏 Constraints

* `board.length == 9`
* `board[i].length == 9`
* `board[i][j]` is a digit `'1'`–`'9'` or `'.'`

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity:** O(n²)
* **Space Complexity:** O(n²)

## 🧠 Hints

### 🪜 Hint 1

Which data structure would you prefer to use for checking duplicates?

### 🧩 Hint 2

You can use a hash set for every row and column to check duplicates.
But how can you efficiently check for the 3x3 squares?

### ⚙️ Hint 3

We can find the index of each square by the equation `(row // 3) * 3 + (col // 3)`.
Then, use hash sets for O(1) lookups while inserting numbers into their corresponding row, column, and square hash maps.