class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sqr_sum_lis = []
        while True:
            sum_n = 0
            for i in str(n):
                sum_n += int(i) ** 2
            if sum_n == 1:
                return True
            elif (not sqr_sum_lis) or (sum_n not in sqr_sum_lis):
                sqr_sum_lis.append(sum_n)
            else:
                return False
            n = sum_n
                