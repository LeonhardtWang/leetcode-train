class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_n = len(s)
        p_n = len(p)
        dp = [[False for _ in range(p_n+1)] for _ in range(s_n+1)]
        dp[0][0] = True
        for j in range(1, p_n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        for i in range(1, s_n+1):
            for j in range(1, p_n+1):
                if s[i-1] == p[j-1] or p [j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] =  dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]