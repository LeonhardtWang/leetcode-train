class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #方法一：
        #return int(num ** (1 / 2)) ** 2 == num
        
        #方法二：1 + 3 + …… + (2n - 1) == n ^ 2
        k = 1
        while num > 0:
            num -= k
            k += 2
        return num == 0
        
        