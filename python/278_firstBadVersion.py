# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 方法一：超时
        '''
        for i in range(1, n+1):
            if isBadVersion(i) == True:return i
        '''
            
        # 方法二：二分法
        start = 1
        end = n
        while end - start > 1:
            mid_n = (start + end) // 2
            if isBadVersion(mid_n) == False:
                start = mid_n
            else:
                end = mid_n
        if isBadVersion(start) == True:
            return start
        else:
            return end