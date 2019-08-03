# 方法一：计算每个数字二进制中1的数目
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            res.append(self._count_1(i))
        return res
        
    def _count_1(self, num):
        res = 0
        while num:
            res += num & 1
            num >>= 1
        return res

# 方法二：动态规划
class Solution2(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num + 1)
        for i in range(1, num+1):
            p = 0
            tmp = 1
            while i - tmp >= 0:
                tmp *= 2
                p += 1
            dp[i] = dp[i-2**(p-1)] + 1
        return dp