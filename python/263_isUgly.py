class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:return False
        while num > 1:
            for i in [2, 3, 5]:
                res = num / i
                if int(res) == res:
                    num = res
                    break
                else:
                    if i == 5:return False
        return True
                    
        