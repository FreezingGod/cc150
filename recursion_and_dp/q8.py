class Solution:
    def numOfWays(self, n):
        if n == 0: return 0
        s = [1, 5, 10, 25]
        dp = [[0]*(n+1) for _ in range(len(s))]
        dp[0] = [1]*(n+1)
        for i in range(1,len(s)):
            for j in range(n+1):
                dp[i][j] = dp[i-1][j]
                if j - s[i] >= 0:
                    dp[i][j] += dp[i][j-s[i]]
        return dp[-1][-1]

sol = Solution()
print sol.numOfWays(1000)
print sol.numOfWays(10000)
# for i in range(1, 26):
#     print i, sol.numOfWays(i)
