# 方法一：回溯法
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_sum = sum(nums)
        if num_sum % 2 == 0:
            num_sum //= 2
        else:
            return False
        return self._is_split(sorted(nums), num_sum)
        
    def _is_split(self, nums, num_sum):
        for i, num in enumerate(nums):
            if i != 0 and nums[i] == nums[i-1]: # 避免全是一个数，超时
                continue
            div = num_sum - num
            if div == 0:
                return True
            elif div > 0:
                tmp = self._is_split(nums[:i]+nums[i+1:], div)
                if tmp:
                    return tmp
            else:
                continue
        return False


# 方法二：动态规划
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_sum = sum(nums)
        if num_sum % 2 == 0:
            num_sum //= 2
        else:
            return False
        n = len(nums)
        dp = [[False for _ in range(num_sum+1)] for _ in range(n)]
        # dp[i][j] 表示 区间[0,i]是否存在子集的和为j
        for j in range(num_sum+1):
            dp[0][j] = True if nums[0] == j else False
        
        for i in range(1, n):
            for j in range(num_sum+1):
                if j > nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
                
print(Solution().canPartition([3,3,3,4,5]))