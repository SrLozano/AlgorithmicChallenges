class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        results = []
        for i in range(0, len(nums)):
            copy = nums.copy()
            aux_num = copy[i]
            copy.pop(i)
            
            permutations = self.permute(copy)
            for permutation in permutations:
                results.append([aux_num] + permutation)
        
        return results
