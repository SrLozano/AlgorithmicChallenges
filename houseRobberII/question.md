# 🏠 **House Robber II**

You are given an integer array `nums` where `nums[i]` represents the amount of money the `iᵗʰ` house has.
The houses are arranged **in a circle**, i.e. **the first house and the last house are neighbors**.

You plan to rob houses to maximize the amount of money stolen,
but you **cannot rob two adjacent houses** — the security system will alert the police if you do.

## 🧩 **Task**

Return the **maximum amount of money** you can rob **without alerting the police**.

## 💡 **Example 1**

**Input:**

```python
nums = [3, 4, 3]
```

**Output:**

```
4
```

**Explanation:**
You cannot rob `nums[0] + nums[2] = 6` because houses 0 and 2 are adjacent (circularly).
The best you can do is rob `nums[1] = 4`.

## 💡 **Example 2**

**Input:**

```python
nums = [2, 9, 8, 3, 6]
```

**Output:**

```
15
```

**Explanation:**
You cannot rob `nums[0] + nums[2] + nums[4] = 16` because houses `0` and `4` are adjacent (circle).
The maximum is `nums[1] + nums[4] = 9 + 6 = 15`.

## ⚙️ **Constraints**

```
1 <= nums.length <= 100
0 <= nums[i] <= 100
```

## ⏱️ **Recommended Time & Space Complexity**

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

where `n` is the number of houses.

## 🧠 **Hints**

### 💭 Hint 1

First, consider solving the simpler version — the **linear** “House Robber I” problem.
Can you express it using a recurrence relation?
At each house, you can either:

* Rob it and **skip the next**, or
* Skip it and **move to the next**.

### 💭 Hint 2

You can express this as:

```
max(nums[i] + dfs(i + 2), dfs(i + 1))
```

The base case returns 0 when `i` is out of bounds.
This recursive approach is O(2ⁿ) — can you avoid recomputation?

### 💭 Hint 3

Use **memoization** to store results for each index and reuse them.
How will you handle the **circular adjacency** between the first and last house?

### 💭 Hint 4

Split the problem into **two scenarios**:

1. Rob houses from **index 0 → n-2** (exclude the last)
2. Rob houses from **index 1 → n-1** (exclude the first)

Compute both and return the **maximum**.
You can also use bottom-up **dynamic programming** for better performance.