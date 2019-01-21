class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = [i.lower() for i in filter(str.isalnum, s)]
        return res == res[::-1]