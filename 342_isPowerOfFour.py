class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type num: int
        :rtype: bool
        """
        while n % 4 == 0 and n > 1:
            n  /= 4
        return n == 1