# 💧 Container With Most Water

You are given an integer array `height` where `height[i]` represents the height of the *i-th* bar.

You may choose any two bars to form a container.
Your goal is to return the **maximum amount of water** a container can store.

## 🧩 Example 1

**Input:**

```
height = [1,7,2,5,4,7,3,6]
```

**Output:**

```
36
```

## 🧩 Example 2

**Input:**

```
height = [2,2,2]
```

**Output:**

```
4
```

## 📏 Constraints

* `2 <= height.length <= 1000`
* `0 <= height[i] <= 1000`

## ⚡️ Recommended Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`
  Where `n` is the size of the input array.

## 💡 Hints

1. 🐢 A brute-force solution would check all pairs of bars and calculate the water for each pair — that’s an **O(n²)** approach. Can you do better?
2. 🧭 Problems that deal with pairs often benefit from the **two-pointer** technique.
3. 📏 Use the formula:

   ```
   water = (j - i) * min(height[i], height[j])
   ```

   Move the pointer with the **smaller height**, since the limiting factor is the shorter bar.
4. 💡 Keep updating the maximum area as you move both pointers toward each other.