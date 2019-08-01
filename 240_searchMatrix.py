# 方法一：二分法
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        for i in range(min(len(matrix), len(matrix[0]))):
            res_v = self._binary_search(matrix, i, target, True)
            res_h = self._binary_search(matrix, i, target, False)
            if res_v or res_h:
                return True
        return False
        
    def _binary_search(self, matrix, start, target, is_vertical):
        lo = start
        hi = len(matrix)-1 if is_vertical else len(matrix[0])-1
        if is_vertical:
            while lo <= hi:
                mid = (lo + hi) // 2
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        else:
            while lo <= hi:
                mid = (lo + hi) // 2
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
        return False
        
# 方法二：缩减搜索空间
class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        return self._helper(matrix, 0, 0, len(matrix[0])-1, len(matrix)-1, target)
        
    def _helper(self, matrix, left, up, right, down, target):
        if left > right or up > down:
            return False
        mid = (left + right) // 2
        lo = up
        hi = down
        while lo <= hi:
            mid_row = (lo + hi) // 2
            if matrix[mid_row][mid] < target:
                lo = mid_row + 1
            elif matrix[mid_row][mid] > target:
                hi = mid_row - 1
            else:
                return True
        
        row = (lo + hi) // 2
        res_left_down = self._helper(matrix, left, row+1, mid-1, down, target)
        res_right_up = self._helper(matrix, mid+1, up, right, row, target)
        return res_left_down or res_right_up

# 方法三
class Solution3(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        i = m - 1
        j = 0
        while i >=0 and j < n:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                return True
        return False


test = [[-5]]
print(Solution3().searchMatrix(test, -10))