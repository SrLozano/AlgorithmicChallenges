class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        longest_subsequence = 0
        
        for num in num_set:
            if num - 1 not in num_set:  # Start only if it's the beginning of a sequence
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_subsequence = max(longest_subsequence, current_streak)
        
        return longest_subsequence
