class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 方法一：移动k位
        #k %= len(nums)
        #if k != 0:
        #    tempt = nums[-k:]
        #    for i in range(len(nums)-1, k-1, -1):
        #        nums[i] = nums[i-k]
        #    nums[:k] = tempt
        
        # 方法二：前半部分翻转，后K部分翻转，再整体翻转
        k %= len(nums)
        if k != 0:
            mid_num = len(nums) - k
            mid_num_copy = mid_num - 1
            for i in range((mid_num_copy + 1) // 2):
                temp = nums[i]
                nums[i] = nums[mid_num_copy]
                nums[mid_num_copy] = temp
                mid_num_copy -= 1
            
            mid_num_copy = mid_num
            for i in range(k // 2):
                temp = nums[-i-1]
                nums[-i-1] = nums[mid_num]
                nums[mid_num] = temp
                mid_num += 1
            
            
            for i in range(len(nums) // 2):
                temp = nums[i]
                nums[i] = nums[-i-1]
                nums[-i-1] = temp
