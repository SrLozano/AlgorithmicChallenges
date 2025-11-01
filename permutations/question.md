# Permutations 🔄

Given an array `nums` of unique integers, return all the possible permutations. You may return the answer in any order.

## Example 1: 🧩

**Input:** `nums = [1,2,3]`

**Output:** `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

## Example 2: 🎯

**Input:** `nums = [7]`

**Output:** `[[7]]`

## Constraints: ⛓️

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`

## Recommended Time & Space Complexity ⏳💾

You should aim for a solution with **O(n * n!)** time and **O(n)** space, where `n` is the size of the input array.

## Hint 1 💡

A permutation is the same as the array but with the numbers arranged in a different order. The given array itself is also considered a permutation. This means we should make a decision at each step to take any element from the array that has not been chosen previously. By doing this recursively, we can generate all permutations. How do you implement it? 🤔

## Hint 2 🔍

We can use **backtracking** to explore all possible permutation paths. We initialize a temporary list to append the chosen elements and a boolean array of size `n` (the same size as the input array) to track which elements have been picked so far (`true` means the element is chosen; otherwise, `false`). At each step of recursion, we iterate through the entire array, picking elements that have not been chosen previously, and proceed further along that path. Can you think of the base condition to terminate the current recursive path? 🛑

## Hint 3 🎯

We observe that every permutation has the same size as the input array. Therefore, we can append a copy of the list of chosen elements in the current path to the result list if the size of the list equals the size of the input array, terminating the current recursive path. 🏁