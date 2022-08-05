class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_nums = 0
        for num in nums:
            sum_nums += num
        if max(nums) != len(nums):return len(nums)
        else:
            sum_complete = max(nums) * (len(nums) + 1) / 2
        return int(sum_complete - sum_nums)