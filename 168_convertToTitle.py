class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            n, mod = divmod(n, 26)
            if mod == 0:
                res = 'Z' + res
                n -= 1
            else:
                res = chr(64 + mod) + res
        return res