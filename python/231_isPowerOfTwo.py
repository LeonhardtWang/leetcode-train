class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 方法一：不断除2看余数
        '''
        if n == 1: return True
        if n == 0: return False
        while True:
            i = n % 2
            if i == 0: 
                n = n / 2
            else:
                return False
            if n == 1:
                return True
        '''
        
        # 方法二：按位运算
        return n & (n - 1) == 0 if n > 0 else False
    
        # 方法三
        #return False if n <= 0 else 2**31 % n == 0
            