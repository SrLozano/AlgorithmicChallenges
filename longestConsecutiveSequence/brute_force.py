from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest_subsequence = 0
        
        for num in nums:
            current_num = num
            current_streak = 1

            # Check if the next number exists in the array
            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_subsequence = max(longest_subsequence, current_streak)
        
        return longest_subsequence
