class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 一个2和一个5能配出一个10，而2肯定比5的个数多，只需要数5的个数就行
        base, res = 5, 0
        while n >= base:
            res += n // base
            base *= 5
        return res