# 🍌 Koko Eating Bananas

You are given an integer array `piles` where `piles[i]` is the number of bananas in the `ith` pile. You are also given an integer `h`, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of `k`. Each hour, you may choose a pile of bananas and eat `k` bananas from that pile. If the pile has less than `k` bananas, you may finish eating the pile but you cannot eat from another pile in the same hour.

Return the minimum integer `k` such that you can eat all the bananas within `h` hours.

## 📝 Example 1:

**Input:**  
`piles = [1,4,3,2]`, `h = 9`  

**Output:**  
`2`  

**Explanation:**  
With an eating rate of `2`, you can eat the bananas in `6` hours. With an eating rate of `1`, you would need `10` hours to eat all the bananas (which exceeds `h=9`), thus the minimum eating rate is `2`.


## 📝 Example 2:

**Input:**  
`piles = [25,10,23,4]`, `h = 4`  

**Output:**  
`25`  


## 🔒 Constraints:

- `1 <= piles.length <= 1,000`
- `piles.length <= h <= 1,000,000`
- `1 <= piles[i] <= 1,000,000,000`


## 🎯 Recommended Time & Space Complexity

You should aim for a solution with **O(nlogm)** time and **O(1)** space, where `n` is the size of the input array, and `m` is the maximum value in the array.


## 💡 Hint 1

Given `h` is always greater than or equal to the length of `piles`, can you determine the upper bound for the answer? How much time does it take Koko to eat a pile with `x` bananas?

## 💡 Hint 2

It takes `ceil(x / k)` time to finish the `x` pile when Koko eats at a rate of `k` bananas per hour. Our task is to determine the minimum possible value of `k`. However, we must also ensure that at this rate, `k`, Koko can finish eating all the piles within the given `h` hours. Can you now think of the upper bound for `k`?

## 💡 Hint 3

The upper bound for `k` is the maximum size of all the piles. Why? Because if Koko eats the largest pile in one hour, then it is straightforward that she can eat any other pile in an hour only.

## 💡 Hint 4

Consider `m` to be the largest pile and `n` to be the number of piles. A brute force solution would be to linearly check all values from `1` to `m` and find the minimum possible value at which Koko can complete the task. This approach would take **O(n * m)** time. Can you think of a more efficient method? Perhaps an efficient searching algorithm could help.

## 💡 Hint 5

Rather than linearly scanning, we can use binary search. The upper bound of `k` is `max(piles)` and since we are only dealing with positive values, the lower bound is `1`. The search space of our binary search is `1` through `max(piles)`. This allows us to find the smallest possible `k` using binary search.
