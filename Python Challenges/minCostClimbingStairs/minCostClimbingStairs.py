class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        
        def dfs(i):
            if i >= len(cost):
                return 0
            
            # if we already have the data computed, return it
            if cache[i] != -1:
                return cache[i]
            
            # divide into subproblems
            cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return cache[i]

        return min(dfs(0), dfs(1))