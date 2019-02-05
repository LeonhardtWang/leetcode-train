class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n % 3 == 0 and n > 1:
            n /= 3
        return n == 1