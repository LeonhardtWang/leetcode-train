# 方法一：暴力法（超时）
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if n < 0:
            x = 1 / x
            n = -n
        for _ in range(n):
            res *= x
        return res

# 方法二：递归
class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return self.myPow(x, n-1) * x
        else:
            return self.myPow(x * x, n/2)

# 方法三：迭代
class Solution3(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans

print(Solution().myPow(2, 4))