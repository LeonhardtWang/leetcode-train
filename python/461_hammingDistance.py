class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_y = x ^ y
        res = 0
        while x_y:
            res += (x_y & 1)
            x_y >>= 1
        return res