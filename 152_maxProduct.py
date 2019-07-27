class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        # 元祖分别储存以num[i-1]结尾的子序列的最大正数和最小负数
        dp = (nums[0], 0) if nums[0] > 0 else (0, nums[0]) 
        
        res = nums[0]
        for i in range(1, len(nums)):
            max_pos = max(nums[i]*dp[int(nums[i]<=0)], nums[i])
            min_nega = min(nums[i]*dp[int(nums[i]>0)], nums[i])
            dp = (max_pos, min_nega) 
            res = max(res, max_pos)  
        return res

print(Solution().maxProduct([-2,0,-1]))