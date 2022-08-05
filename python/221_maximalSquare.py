class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        m = len(matrix)
        if m < 1:
            return res
        n = len(matrix[0])
        dp = [0 for _ in range(n)]
        for i in range(m):
            prev = 0 # [i-1][j-1]的情况
            for j in range(n):
                tmp = dp[j]
                if matrix[i][j] == '1':
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
                prev = tmp
        return res ** 2
                    