# 🧗‍♂️ Climbing Stairs

You are given an integer `n` representing the number of steps to reach the top of a staircase.
You can climb either **1 or 2 steps** at a time.

Return the number of **distinct ways** to climb to the top of the staircase.

## Example 1

```
Input: n = 2
Output: 2
Explanation:
1 + 1 = 2
2 = 2
```

## Example 2

```
Input: n = 3
Output: 3
Explanation:
1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3
```

## Constraints

* 1 ≤ n ≤ 30

## 🕒 Recommended Time & Space Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

## 💡 Hints

**Hint 1:**
At each step, we have two choices: climb one step or climb two steps.
A purely recursive solution has O(2ⁿ) time complexity due to repeated subproblems.
Can you avoid recomputing results?

**Hint 2:**
This is a **Dynamic Programming** problem.
Use **Memoization** to cache results of recursive calls in an array `cache` so that each subproblem is solved once.

**Hint 3:**
Start recursion from `i = 0`, representing your current step.
If a result for the given `i` is already cached, return it directly.
Otherwise, compute recursively and store the result.
Think about the base condition to stop recursion.

**Hint 4:**
At each recursion, try climbing one or two steps:
`dfs(i) = dfs(i + 1) + dfs(i + 2)`
The base case is when `i == n`, where you’ve reached the top.
This is a **1D DP problem**, and can later be optimized for **O(1)** space.