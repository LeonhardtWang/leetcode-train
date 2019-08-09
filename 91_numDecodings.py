# 动态规划
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for _ in range(n)]
        dp[-1] = 1 # 注意这个
        if n == 0 or s[0] == '0':
            return 0
        dp[0] = 0 if s[0] == '0' else 1
        for i in range(1, n):
            if s[i-1] == '0' and s[i] != '0':
                dp[i] = dp[i-1]
            elif s[i-1] != '0' and s[i] == '0':
                if int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-2]
                else:
                    return 0
            elif s[i-1] != '0' and s[i] != '0':
                if int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                return 0
        return dp[-1]
                
print(Solution().numDecodings('226'))