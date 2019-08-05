# 方法一：暴力法+一点优化（超时）

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_helper = [0] * len(nums)
        res = 0
        for i in range(len(nums)):
            index = 0
            for j in range(i, len(nums)):
                nums_helper[index] += nums[j]
                if nums_helper[index] == k:
                    res += 1
                index += 1
        return res

# 方法二：动态规划
class Solution2(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [0]
        for num in nums:
            dp.append(dp[-1]+num)
        
        sum_dict = {}
        res = 0
        for i in range(len(nums)+1):
            if dp[i] - k in sum_dict:
                res += sum_dict[dp[i] - k]
            if dp[i] in sum_dict:
                sum_dict[dp[i]] += 1
            else:
                sum_dict[dp[i]] = 1
        return res

print(Solution2().subarraySum([1,1,1], 2))