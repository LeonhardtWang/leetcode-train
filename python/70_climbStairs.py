class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 斐波那契数列问题 fib(n) = fib(n-1) + fib(n-2)
        # return n if n <= 2 else self.climbStairs(n-1) + self.climbStairs(n-2)
        # 因为会计算大量重复值，时间消耗大
        # 解决方法：
        # 1.记忆搜索，算好的值保存起来
        # 2.动态规划：颠倒计算方向，由自顶而下递归，改为自底而上迭代(本题采用)

        g = 0; f = 1 # 设fib(-1) = 0, fib(0) = 1
        while n > 0:
            f = g + f
            g = f - g
            n -= 1
        return f
print(Solution().climbStairs(5))