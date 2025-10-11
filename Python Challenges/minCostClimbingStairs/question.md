# 🪜 **Min Cost Climbing Stairs**

You are given an array of integers `cost` where `cost[i]` is the cost of taking a step from the *i-th* floor of a staircase.
After paying the cost, you can climb either to the **(i + 1)**-th floor or the **(i + 2)**-th floor.

You may choose to start at **index 0** or **index 1**.

Return the **minimum cost** to reach the top of the staircase — that is, just past the last index in `cost`.

## 🧩 **Example 1**

```
Input: cost = [1,2,3]
Output: 2
Explanation:
We can start at index = 1 and pay cost[1] = 2,
then take two steps to reach the top.
Total cost = 2.
```

## 🧩 **Example 2**

```
Input: cost = [1,2,1,2,1,1,1]
Output: 4
Explanation:
Start at index = 0.
Pay cost[0] = 1 → jump to index = 2
Pay cost[2] = 1 → jump to index = 4
Pay cost[4] = 1 → jump to index = 6
Pay cost[6] = 1 → reach the top
Total cost = 4.
```

## 📏 **Constraints**

* 2 ≤ cost.length ≤ 100
* 0 ≤ cost[i] ≤ 100

## ⏱️ **Recommended Time & Space Complexity**

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

## 💡 **Hints**

**Hint 1:**
At each step, you can go either **one** or **two** steps ahead.
If you draw a decision tree exploring all possibilities, the naive recursion would have **O(2ⁿ)** time complexity.
Can you optimize the repeated subproblems?

**Hint 2:**
Define the recurrence relation as:
`dfs(i) = cost[i] + min(dfs(i + 1), dfs(i + 2))`
Use **Memoization** to store already computed results and avoid recomputation.

**Hint 3:**
Start recursion from positions **0** and **1**.
Before computing `dfs(i)`, check if it’s already cached.
If so, return it; otherwise, compute, store, and return it.
Think carefully about the base case.

**Hint 4:**
The base condition is:
`return 0` if `i >= n` (you’ve reached or passed the top).
This is a **1D Dynamic Programming** problem that can be further optimized with a **Bottom-Up** tabulation approach using only **O(1)** space.