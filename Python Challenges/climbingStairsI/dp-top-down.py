class Solution:
    # time complexity: O(n), each subproblem solved once -> memoization
    def climbStairs(self, n: int) -> int:
        # (n+1) to avoid OOB
        cache = [-1] * (n + 1)
        
        def dfs(i):
            if i <= 1:
                return 1
            
            # if we already have the data computed, return it
            if cache[i] != -1:
                return cache[i]
            
            # divide into subproblems
            cache[i] = dfs(i-1) + dfs(i-2)
            return cache[i]

        return dfs(n)