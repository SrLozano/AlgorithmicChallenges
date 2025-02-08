# 3Sum # 🎯🔥✅

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` where `nums[i] + nums[j] + nums[k] == 0`, and the indices `i`, `j` and `k` are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

## Example 1:

**Input:** `nums = [-1,0,1,2,-1,-4]`  
**Output:** `[[-1,-1,2],[-1,0,1]]`  

**Explanation:**  
- `nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0`.  
- `nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0`.  
- `nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0`.  

The distinct triplets are `[-1,0,1]` and `[-1,-1,2]`.

## Example 2:

**Input:** `nums = [0,1,1]`  
**Output:** `[]`  

**Explanation:** The only possible triplet does not sum up to 0.

## Example 3:

**Input:** `nums = [0,0,0]`  
**Output:** `[[0,0,0]]`  

**Explanation:** The only possible triplet sums up to 0.


## Constraints ⚖️:

- `3 <= nums.length <= 1000`  
- `-10^5 <= nums[i] <= 10^5`  


## Recommended Time & Space Complexity ⏳

You should aim for a solution with **O(n²)** time and **O(1)** space, where `n` is the size of the input array.


## Hint 1 💡

A brute force solution would be to check for every triplet in the array. This would be an **O(n³)** solution. Can you think of a better way?


## Hint 2 💡

Can you think of an algorithm after sorting the input array? What can we observe by rearranging the given equation in the problem?


## Hint 3 💡

We can iterate through `nums` with index `i` and get `nums[i] = -(nums[j] + nums[k])` after rearranging the equation, making `-nums[i] = nums[j] + nums[k]`. For each index `i`, we should efficiently calculate the `j` and `k` pairs without duplicates. Which algorithm is suitable to find `j` and `k` pairs?

## Hint 4 💡

To efficiently find the `j` and `k` pairs, we run the two-pointer approach on the elements to the right of index `i` as the array is sorted. When we run the two-pointer algorithm, consider `j` and `k` as pointers (`j` is at left, `k` is at right) and `target = -nums[i]`. If the current sum `nums[j] + nums[k] < target`, then we need to increase the value of the current sum by incrementing the `j` pointer. Else if the current sum `nums[j] + nums[k] > target`, then we should decrease the value of the current sum by decrementing the `k` pointer. How do you deal with duplicates?

## Hint 5 💡

When the current sum `nums[j] + nums[k] == target`, add this pair to the result. We can move the `j` or `k` pointer until `j < k` and the pairs are repeated. This ensures that no duplicate pairs are added to the result.
