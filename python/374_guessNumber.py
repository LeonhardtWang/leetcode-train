# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    pass

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二分法
        l, r = 1, n
        while l <= r:
            mid_val = (l + r) // 2
            if guess(mid_val) == -1:
                r = mid_val - 1
            elif guess(mid_val) == 1:
                l = mid_val + 1
            else:
                return mid_val
                