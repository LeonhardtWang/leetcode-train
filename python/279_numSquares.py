# 方法一：动态规划
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] = i
            j = 1
            while i - j ** 2 >= 0:
                dp[i] = min(dp[i], dp[i-j**2]+1)
                j += 1
        return dp[-1]

# 方法二：BFS算法寻找最短路径（图论）
class Solution2(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from collections import deque
        
        class Node:
            def __init__(self, val, step):
                self.val = val
                self.step = step
        
        visited = [False] * (n + 1)
        
        queue = deque()
        queue.append(Node(n, 0))
        while queue:
            node = queue.popleft()
            for i in range(1, node.val+1):
                num = node.val - i ** 2
                if num < 0:
                    break
                if not visited[num]:
                    queue.append(Node(num, node.step+1))
                    visited[num] = True
                if num == 0:
                    return node.step + 1