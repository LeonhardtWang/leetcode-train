class Solution:
    def minPathSum(self, grid: list) -> int:
        if not grid:
            return None
        n = len(grid)
        m = len(grid[0])
        res = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1 or j == 1:
                    res[i][j] = max(res[i-1][j], res[i][j-1]) + grid[i-1][j-1]
                else:
                    res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i-1][j-1]
        return res[-1][-1]

test = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(Solution().minPathSum(test))