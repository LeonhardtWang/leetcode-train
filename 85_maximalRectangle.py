# 方法一：动态规划（超时）
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m < 1:
            return 0 
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)] 
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    max_area = max(max_area, width * (i - k + 1))
        return max_area


# 方法2：借用84题的思想（栈）
class Solution2:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0
        if not matrix:
            return max_area
        dp = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            max_area = max(max_area, self.leetcode84(dp))
        return max_area
                
    def leetcode84(self, heights):
        stack = [-1]
        max_area = 0
        for i, v in enumerate(heights):
            while stack[-1] != -1 and v <= heights[stack[-1]]:
                max_area = max(max_area, heights[stack.pop()]*(i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()]*(len(heights) - stack[-1] - 1))
        return max_area
        
                    