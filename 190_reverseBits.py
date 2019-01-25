class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 方法一：调用内置函数
        #return int(bin(n)[2:].zfill(32)[::-1], 2)
        
        # 方法二：位运算
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res
        