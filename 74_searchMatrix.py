class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 二分查找
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        lo = 0
        hi = m * n - 1
        return self.bin_search(matrix, m, n, target, lo, hi)
        
    def bin_search(self, matrix, m, n, target, lo, hi):
        while lo <= hi:
            mid = (lo+hi) // 2
            i, j = self.num_to_ij(mid, m, n)
            if matrix[i][j] < target:
                lo = mid + 1
            elif matrix[i][j] == target:
                return True
            else:
                hi = mid - 1
        return False
 
    def num_to_ij(self, num, m, n):
        num += 1
        mod = num % n
        if mod == 0:
            return (num//n-1, n-1)
        else:
            return (num//n, mod-1)

        