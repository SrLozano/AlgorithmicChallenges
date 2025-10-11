# 💹 **Best Time to Buy and Sell Stock**

You are given an integer array `prices` where `prices[i]` is the price of **NeetCoin** on the `iᵗʰ` day.

You may choose **one day to buy** and **another future day to sell** the coin.

Return the **maximum profit** you can achieve.
If no profitable transaction is possible, return `0`.

## 💡 **Example 1**

**Input:**

```python
prices = [10, 1, 5, 6, 7, 1]
```

**Output:**

```
6
```

**Explanation:**
Buy on `prices[1] = 1` and sell on `prices[4] = 7`.
Profit = `7 - 1 = 6`.

## 💡 **Example 2**

**Input:**

```python
prices = [10, 8, 7, 5, 2]
```

**Output:**

```
0
```

**Explanation:**
No profitable transaction can be made, so the maximum profit is `0`.

## ⚙️ **Constraints**

```
1 <= prices.length <= 100
0 <= prices[i] <= 100
```

## ⏱️ **Recommended Time & Space Complexity**

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

where `n` is the number of days.

## 🧠 **Hints**

### 💭 Hint 1

A brute force solution would try **every pair** of buy/sell days → O(n²) time.
Can you think of a way to do it in a **single pass**?

### 💭 Hint 2

You should **buy low** and **sell high**.
Can you track the **lowest price seen so far** as you iterate?

### 💭 Hint 3

Iterate through the array considering each day `i` as a **selling day**.
What’s the **best (lowest)** buying price before day `i`?

### 💭 Hint 4

We’re maximizing

```
profit = sell_price - min_buy_price
```

Keep updating `min_buy_price` and track the **maximum profit** across all days.
If all profits are negative, return `0` (since you can skip trading).