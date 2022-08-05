# 方法一
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_val = float('inf')
        for i, v in enumerate(nums):
            nums[i] = (v, v>min_val)
            min_val = min(min_val, v)
            
        max_val = float('-inf')
        for i in reversed(range(len(nums))):
            if nums[i][0] < max_val and nums[i][1]:
                return True
            max_val = max(max_val, nums[i][0])
        return False

# 方法二
class Solution2(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one = float('inf')
        two = float('inf')
        for num in nums:
            if num <= one:
                one = num
            elif num <= two:
                two = num
            else:
                return True
        return False