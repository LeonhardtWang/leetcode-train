class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 埃拉托斯特尼筛法
        if n <= 2:
            return 0
        is_prime = [True] * n # 小于n的数中，0,1,n都为False
        is_prime[:2] = [False] * 2
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i] == True:
                is_prime[i*2:n:i] = [False] * len(is_prime[i*2:n:i])
        return sum(is_prime)

print(Solution().countPrimes(10))