class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length-1, 0, -1):
            if nums[i-1] < nums[i]:
                j = i
                while j <= length-1 and nums[i-1] < nums[j]:
                    j += 1
                j -= 1
                tmp = nums[i-1]
                nums[i-1] = nums[j]
                nums[j] = tmp
                
                self.reverse(nums, i, length-1)
                return 
        self.reverse(nums, 0, length-1)
        
    def reverse(self, nums, i , j):
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1