# 💰 Coin Change

You are given an integer array `coins` representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer `amount` representing a target sum of money.

Return the **fewest number of coins** needed to make up the exact amount.
If it’s **impossible** to make up that amount, return **-1**.

You may assume you have an **unlimited supply** of each coin.

## 💡 Example 1

**Input:**

```python
coins = [1, 5, 10]
amount = 12
```

**Output:**

```python
3
```

**Explanation:**
12 = 10 + 1 + 1.
We use **3 coins** in total.

## 💡 Example 2

**Input:**

```python
coins = [2]
amount = 3
```

**Output:**

```python
-1
```

**Explanation:**
It’s impossible to make up amount 3 with only coins of 2.

## 💡 Example 3

**Input:**

```python
coins = [1]
amount = 0
```

**Output:**

```python
0
```

**Explanation:**
Choosing **0 coins** is a valid way to make up 0.

## 📏 Constraints

* `1 <= coins.length <= 10`
* `1 <= coins[i] <= 2^31 - 1`
* `0 <= amount <= 10000`

## ⏱️ Recommended Time & Space Complexity

* **Time Complexity:** O(n × t)
* **Space Complexity:** O(t)
  Where **n** = number of coin types, and **t** = total target amount.
  
## 🧠 Hints

### 🪜 Hint 1

Think recursively.
Start from the total `amount`. At each step:

* Try subtracting each coin value (only if it’s ≤ the remaining amount).
* Recursively compute how many coins are needed for the smaller subproblem.

This can be expressed as a recurrence relation, but you’ll need a **base condition** (e.g. when the amount reaches 0).

### 🧩 Hint 2

If `amount == 0`, return 0.
If no coins fit, return ∞ (or -1).

Recurrence relation:

```
f(amount) = min(1 + f(amount - coin[i])) for all valid coins
```

However, this naive recursion is **O(n^t)** — far too slow.

### ⚙️ Hint 3

Use **Dynamic Programming / Memoization** to store results of subproblems.
That way, if you already computed the minimum coins for a certain amount, you **reuse** it instead of recalculating.

* Use an array `dp[amount + 1]` initialized to a large number.
* Base case: `dp[0] = 0`
* For each `coin`, update:

  ```
  dp[a] = min(dp[a], 1 + dp[a - coin])
  ```
* Final answer:
  If `dp[amount]` is still large (unreachable), return `-1`.