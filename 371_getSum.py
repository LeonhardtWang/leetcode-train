class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            c = ((a & b) << 1 ) & 0xFFFFFFFF # 进位
            a = (a ^ b) & 0xFFFFFFFF # 无进位求和
            b = c
        return a if a < 0X7fffffff else ~(a ^ 0xFFFFFFFF)
