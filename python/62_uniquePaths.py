class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 1 or n < 1:
            return 0
        res = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1 and j == 1:
                    res[i][j] = 1
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[n][m]

print(Solution().uniquePaths(7, 3))