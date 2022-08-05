# 方法一：深度优先遍历（DFS，对应堆栈 - 递归或迭代 - 也对应树的前序遍历）
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, i, j):
            if i - 1 >= 0 and grid[i-1][j] == '1':
                grid[i-1][j] = '0'
                dfs(grid, i-1, j)
            if j - 1 >= 0 and grid[i][j-1] == '1':
                grid[i][j-1] = '0'
                dfs(grid, i, j-1)
            if i + 1 < len(grid) and grid[i+1][j] == '1':
                grid[i+1][j] = '0'
                dfs(grid, i+1, j)
            if j + 1 < len(grid[0]) and grid[i][j+1] == '1':
                grid[i][j+1] = '0'
                dfs(grid, i, j+1)

        res = 0
        m = len(grid)
        if m < 1:
            return res
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    res += 1
        return res



# 方法二：广度优先遍历（BFS， 对应队列 - 使用辅助队列 - 也对应树的层次遍历）
class Solution2(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque
        res = 0
        if not grid:
            return res
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i, j))
                    while queue:
                        row, col = queue.pop()
                        if row - 1 >= 0 and grid[row-1][col] == '1':
                            queue.appendleft((row-1, col))
                            grid[row-1][col] = '0'
                        if col - 1 >= 0 and grid[row][col-1] == '1':
                            queue.appendleft((row, col-1))
                            grid[row][col-1] = '0'
                        if row + 1 < m and grid[row+1][col] == '1':
                            queue.appendleft((row+1, col))
                            grid[row+1][col] = '0'
                        if col + 1 < n and grid[row][col+1] == '1':
                            queue.appendleft((row, col+1))
                            grid[row][col+1] = '0'
                    res += 1
        return res 

# 方法一和方法二均为洪水填充法

# 方法三：并查集
class Solution3(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        class UnionFind(object):
            def __init__(self, grid):
                self.m = len(grid)
                self.n = len(grid[0])
                self.count = 0
                self.parent = [None] * self.m * self.n
                self.rank = [None] * self.m * self.n
                for i in range(self.m):
                    for j in range(self.n):
                        if grid[i][j] == '1':
                            self.parent[i*self.n+j] = i * self.n + j
                            self.count += 1
                        self.rank[i*self.n+j] = 0
            
            def find(self, i):
                if self.parent[i] != i:
                    self.parent[i] = self.find(self.parent[i])
                return self.parent[i]
            
            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)
                if root_x != root_y:
                    if self.rank[root_x] > self.rank[root_y]:
                        self.parent[root_y] = root_x
                    elif self.rank[root_x] < self.rank[root_y]:
                        self.parent[root_x] = root_y
                    else:
                        self.parent[root_y] = root_x
                        self.rank[root_x] += 1
                    self.count -= 1
            
            def get_count(self):
                return self.count 
        
        if not grid:
            return 0 
        m = len(grid)
        n = len(grid[0])

        uf = UnionFind(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    if i - 1 >= 0 and grid[i-1][j] == '1':
                        uf.union(i*n+j, (i-1)*n+j)
                    if j - 1 >= 0 and grid[i][j-1] == '1':
                        uf.union(i*n+j, i*n+j-1)
                    if i + 1 < m and grid[i+1][j] == '1':
                        uf.union(i*n+j, (i+1)*n+j)
                    if j + 1 < n and grid[i][j+1] == '1':
                        uf.union(i*n+j, i*n+j+1)
        return uf.get_count()
                

grid = [['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '0', '0', '0', '1'],
        ['0', '1', '1', '0', '1']]

print(Solution3().numIslands(grid))

        