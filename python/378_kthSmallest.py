# 方法一：二分查找法
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        lo = matrix[0][0]
        hi = matrix[n-1][n-1]
        while lo < hi:
            count = 0
            j = n - 1
            mid = lo + (hi - lo) // 2
            for i in range(n):
                while j >=0 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1
            if count < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

# 方法二：插排法
class Solution2(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import bisect
        k_lis = [float('inf')] * k
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                bisect.insort(k_lis, matrix[i][j], hi=k)
                k_lis.pop() # 维护长度
        return k_lis[-1]

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(Solution2().kthSmallest(matrix, 3))