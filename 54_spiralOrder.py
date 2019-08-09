class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        return self._helper(matrix, 0, 0, n-1, m-1)
        
    def _helper(self, matrix, left, up, right, down):
        if left == up == right == down:
            return [matrix[left][right]]
        res = []
        for j in range(left, right+1):
            res.append(matrix[up][j])
        for i in range(up+1, down+1):
            res.append(matrix[i][right])
        if down - up > 0 and right - left > 0:
            for j in range(right-1, left-1, -1):
                res.append(matrix[down][j])
            for i in range(down-1, up, -1):
                res.append(matrix[i][left])
        if right - left >= 2 and down - up >= 2:
            inner_res = self._helper(matrix, left+1, up+1, right-1, down-1)
            return res + inner_res
        return res
        
test = [
  [1,4],[2,5]
]
print(Solution().spiralOrder(test))