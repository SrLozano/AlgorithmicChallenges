# 🏠 House Robber

## 📘 Problem Statement

You are given an integer array `nums` where `nums[i]` represents the amount of money the `i`th house has.
The houses are arranged in a straight line (each house is a neighbor of the previous and next one).

You plan to rob the houses but **cannot rob two adjacent houses**, because the security system will alert the police if two adjacent houses are both broken into.

Return the **maximum amount of money** you can rob without alerting the police.

## 💡 Example 1

**Input:**

```python
nums = [1, 1, 3, 3]
```

**Output:**

```
4
```

**Explanation:**
Rob houses `0` and `2`: `1 + 3 = 4`

## 💡 Example 2

**Input:**

```python
nums = [2, 9, 8, 3, 6]
```

**Output:**

```
16
```

**Explanation:**
Rob houses `0`, `2`, and `4`: `2 + 8 + 6 = 16`

## ⚙️ Constraints

* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 100`

## ⏱️ Recommended Time & Space Complexity

* **Time:** `O(n)`
* **Space:** `O(n)` or better (can optimize to `O(1)`)

## 🧩 Hint 1

Think recursively!
At each house, you can **either rob it or skip it**:

* If you rob the current house → you must skip the next one.
* If you skip it → move to the next house.

## 🔁 Hint 2

This leads to a recurrence relation:

```
dfs(i) = max(nums[i] + dfs(i + 2), dfs(i + 1))
```

Where:

* `i` = current house index
* `dfs` = recursive helper function

## 🚧 Hint 3

The **base condition**:
When `i` goes out of bounds (`i >= len(nums)`), return `0`.

A simple recursive version leads to **O(2ⁿ)** time because it recomputes overlapping subproblems.

## 🚀 Hint 4

Use **Memoization** to store results of recursive calls:

* Cache results for each index `i`.
* When recursion hits the same index again, return the cached result instead of recomputing.

This optimization improves the runtime to **O(n)**.

You can also use **Bottom-Up DP** to achieve the same result iteratively with constant space.