class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.inverse(matrix)
        self.reverse(matrix)     
    
    def inverse(self, matrix):
        """求转置矩阵"""
        n = len(matrix)
        for i in range(n):
            j = i + 1
            while j <= n-1:
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
                j += 1
        
    def reverse(self, matrix):
        """矩阵每行进行逆转"""
        n = len(matrix)
        for i in range(n):
            l = 0
            r = n - 1
            while l < r:
                tmp = matrix[i][l]
                matrix[i][l] = matrix[i][r]
                matrix[i][r] = tmp
                l += 1
                r -= 1

nums = [
  [1,2],
  [3,4]
]
Solution().rotate(nums)
print(nums)