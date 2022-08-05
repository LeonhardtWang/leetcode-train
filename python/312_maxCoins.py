# 方法一：递归（时间复杂度过高）
class Solution:
    def maxCoins(self, nums: list) -> int:
        res = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if i == 0 == n - 1:
                return num
            elif i == 0 and i < n - 1:
                res = max(res, num*nums[i+1]+self.maxCoins(nums[i+1:]))
            elif i > 0 and i == n - 1:
                res = max(res, num*nums[i-1]+self.maxCoins(nums[:i]))
            else:
                res = max(res, num*nums[i-1]*nums[i+1]+self.maxCoins(nums[:i]+nums[i+1:]))
        return res

# 方法二：动态规划
class Solution2:
    def maxCoins(self, nums: list) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
        for j in range(n+2):
            for i in range(j-2, -1, -1):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
        return dp[0][n+1]            

print(Solution2().maxCoins([3, 1, 5, 8]))