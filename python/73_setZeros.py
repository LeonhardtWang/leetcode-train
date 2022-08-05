# 方法一：记录需要重置为0的行和列
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row = set()
        col = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0

# 方法二：用第一行和第一列去记录是否当前行或者当前列需要重置为0
class Solution2(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        sign = [False, False]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        sign[0] = True
                    if j == 0:
                        sign[1] = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if sign[0] == True:
            for j in range(n):
                matrix[0][j] = 0
        if sign[1] == True:
            for i in range(m):
                matrix[i][0] =  0
                
test = [[1,1,1],[0,1,2]]
print(Solution2().setZeroes(test))