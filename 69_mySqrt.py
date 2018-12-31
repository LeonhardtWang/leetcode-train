class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:return x
        lo = 0; hi = x
        while True:
            half = (lo + hi) // 2
            if lo == hi - 1:return lo
            if half ** 2 == x:
                return half
            elif half ** 2 < x:
                lo = half
            else:
                hi = half

print(Solution().mySqrt(8))