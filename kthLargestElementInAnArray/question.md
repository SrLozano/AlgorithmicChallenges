# Kth Largest Element in an Array 🎯

Given an unsorted array of integers `nums` and an integer `k`, return the **kth largest element** in the array.

By **kth largest element**, we mean the kth largest element in the sorted order, not the kth distinct element.

**Follow-up:** Can you solve it without sorting? 🤔

## Example 1: 🧩

**Input:**  
`nums = [2,3,1,5,4]`, `k = 2`

**Output:**  
`4`

## Example 2: 🎯

**Input:**  
`nums = [2,3,1,1,5,5,4]`, `k = 3`

**Output:**  
`4`

## Constraints: ⛓️

- `1 <= k <= nums.length <= 10000`
- `-1000 <= nums[i] <= 1000`

## Recommended Time & Space Complexity ⏳💾

You should aim for a solution as good or better than **O(nlogk)** time and **O(k)** space, where `n` is the size of the input array, and `k` represents the rank of the largest number to be returned (i.e., the k-th largest element).

## Hint 1 💡

A naive solution would be to sort the array in descending order and return the k-th largest element. This would be an **O(nlogn)** solution. Can you think of a better way? Maybe you should think of a data structure which can maintain only the top `k` largest elements. 🧠

## Hint 2 🔍

We can use a **Min-Heap**, which stores elements and keeps the smallest element at its top. When we add an element to the Min-Heap, it takes **O(logk)** time since we are storing `k` elements in it. Retrieving the top element (the smallest in the heap) takes **O(1)** time. How can this be useful for finding the k-th largest element? 🤔

## Hint 3 🎯

The k-th largest element is the smallest element among the top `k` largest elements. This means we only need to maintain `k` elements in our Min-Heap to efficiently determine the k-th largest element. Whenever the size of the Min-Heap exceeds `k`, we remove the smallest element by popping from the heap. How do you implement this? 🛠️

## Hint 4 🌟

We initialize an empty Min-Heap. We iterate through the array and add elements to the heap. When the size of the heap exceeds `k`, we pop from the heap and continue. After the iteration, the top element of the heap is the k-th largest element. 🏁