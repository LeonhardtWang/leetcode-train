class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0 
        for i in range(len(nums)):
            if nums[i] != 0 and nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
            elif nums[k] != 0:
                k += 1
    
        