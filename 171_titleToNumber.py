class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s) - 1
        num = 0
        for i in s:
            num += (ord(i) - 64) * 26 ** length
            length -= 1
        return num