class Solution:
    # time complexity: O(n^2)
    # space complexity: O(n^2)
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        # is the substring s[i:j+1] palindromic?
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # substring s[i:j+1] is a palindrome if
                # 1. the end characters match → s[i] == s[j]
                # 2 Either 
                # a) the substring length is ≤ 3 → (j - i <= 2) (examples: "a", "aa", "aba" are trivially palindromes)
                # b) the inner substring s[i+1:j] (remember dp[i][j] indicates the substring s[i:j+1]) is also a palindrome → dp[i+1][j-1] == True
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1

        return res
