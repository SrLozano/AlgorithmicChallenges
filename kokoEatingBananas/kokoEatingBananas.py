import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            k = (left + right) // 2
            
            total_time = 0
            for p in piles:
                total_time += math.ceil(p/k)
            if total_time <= h:
                result = k
                right = k - 1
            else:
                left = k + 1 

        return result