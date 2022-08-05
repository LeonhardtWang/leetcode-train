class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]
        for i in range(1, len(nums)):
            res.append(nums[i-1] * res[i-1])
        tmp = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] = res[i] * tmp
            tmp *= nums[i]
        return res
                