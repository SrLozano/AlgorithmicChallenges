class Solution:
    # time complexity: O(amount * len(coins))
    # space complexity: O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # dp[a] = minimum number of coins needed to make amount 'a'
        # Initialize all with a large default (amount+1 acts as "infinity")
        # because in the worst case, we would never need more than amount coins of value 1
        dp = [amount + 1 for _ in range(amount + 1)]

        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0

        # Build up solutions for every amount from 1 to target 'amount'
        for a in range(1, amount + 1):
            # Try every coin denomination
            for c in coins:
                # Only valid if coin value <= current amount
                if a - c >= 0:
                    # Option 1: don't use coin c (dp[a])
                    # Option 2: use coin c → 1 + dp[a - c]
                    # We take the minimum of both
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # If dp[amount] wasn't updated (still "infinity"), return -1 (not possible)
        # Otherwise, return the computed minimum
        return dp[amount] if dp[amount] != amount + 1 else -1
