class Solution:
    # time complexity: 0(n^2)
    # space complexity: 0(n^2)
    def longestPalindrome(self, s: str) -> str:
        # as solution we want to return the palindrome, so starting index plus its size
        resIdx, resLen = 0, 0
        n = len(s)

        # dp[i][j]: True if the substring s[i:j+1] is a palindrome, else False
        dp = [[False] * n for _ in range(n)]

        # bottom-up approach, we start from the end
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # check if substring s[i:j+1] is a palindrome, being dp[i+1][j-1] the inner substring
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        return s[resIdx : resIdx + resLen]