class Solution:
    def numOfWays(self, n):
        return self.helper(n, 25)
    def helper(self, n, denom):
        next_denom = 0
        if denom == 25:
            next_denom = 10
        elif denom == 10:
            next_denom = 5
        elif denom == 5:
            next_denom = 1
        elif denom == 1:
            return 1
        ways = 0
        for i in range(n/denom+1):
            ways += self.helper(n-i*denom, next_denom)
        return ways

sol = Solution()
for i in range(1,26):
    print i, sol.numOfWays(i)
