# 方法一：分治(超时)
class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        res = self.core(heights, 0, len(heights)-1)
        return res
        
    def core(self, heights, start, end):
        if start > end:
            return 0
        if start == end:
            return heights[start]
        
        min_val = 2 ** 31 - 1
        for i in range(start, end+1):
            v = heights[i]
            if v < min_val:
                min_val = v
                min_i = i
        
        mid = min_val * (end - start + 1)
        left = self.core(heights, start, min_i-1)
        right = self.core(heights, min_i+1, end)
        return max(left, mid, right)


# 方法二：用栈
class Solution2:
    def largestRectangleArea(self, heights: list) -> int:
        stack = [-1]
        res = 0
        for i, v in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= v:
                res = max(res, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        while stack[-1] != -1:
            res = max(res, heights[stack.pop()]*(len(heights)-stack[-1]-1))
        return res
            
print(Solution2().largestRectangleArea([1, 2, 3, 4, 5]))