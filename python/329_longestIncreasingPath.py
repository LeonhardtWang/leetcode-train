# 方法一：深度优先遍历（超时）
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        max_path = 0
        for i in range(m):
            for j in range(n):
                curr_path = self._dfs(matrix, i, j, m, n, visited)
                max_path = max(curr_path, max_path)
        return max_path
        
    def _dfs(self, matrix, i, j, m, n, visited):
        visited[i][j] = True
        res = 1
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and visited[x][y] == False and matrix[x][y] > matrix[i][j]:
                res = max(res, 1+self._dfs(matrix, x, y, m, n, visited))
        visited[i][j] = False
        return res
        
# 方法二：在方法一基础上改进，记忆化（可不用visited）
class Solution2(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        self.res = [[None for _ in range(n)] for _ in range(m)] # 保存中间节点，避免重复计算
        max_path = 0
        for i in range(m):
            for j in range(n):
                curr_path = self._dfs(matrix, i, j, m, n, visited)
                self.res[i][j] = curr_path
                max_path = max(curr_path, max_path)
        return max_path
        
    def _dfs(self, matrix, i, j, m, n, visited):
        visited[i][j] = True
        res = 1
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and visited[x][y] == False and matrix[x][y] > matrix[i][j]:
                if self.res[x][y] is None:
                    self.res[x][y] = self._dfs(matrix, x, y, m, n, visited)
                res = max(res, 1+self.res[x][y])
        visited[i][j] = False
        return res

# 方法三：类似动态规划
class Solution3(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        matrix_to_lis = [(i,j, matrix[i][j]) for i in range(m) for j in range(n)]
        matrix_to_lis.sort(key=lambda s:s[2], reverse=True)
        res_set = {}
        max_path = 0
        for i, j, v in matrix_to_lis:
            tmp = 1
            for x, y in {(i-1,j), (i+1,j), (i,j-1), (i,j+1)}:
                if (x, y) in res_set and res_set[(x, y)][0] > v:
                    tmp = max(tmp, res_set[(x, y)][1]+1)
            res_set[(i, j)] = (v, tmp)
            max_path = max(max_path, tmp)
        return max_path