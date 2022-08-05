class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：递归，超时,记忆化搜索或者动态规划来解决
        #nums_len = len(nums)
        #if nums_len == 0:
        #    return 0
        #elif nums_len == 1:
        #    return nums[0]
        #elif nums_len == 2:
        #    return max(nums)
        #elif nums_len == 3:
        #    return max(nums[1], nums[0] + nums[2])
        #return max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))
        
        # 记忆化搜索，状态转移方程：dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        elif nums_len == 1:
            return nums[0]
        elif nums_len == 2:
            return max(nums)
        dp = [i for i in range(nums_len)]
        for i in range(nums_len):
            if i == 0:
                dp[i] = nums[0]
            elif i == 1:
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]