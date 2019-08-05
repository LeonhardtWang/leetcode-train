# 方法一：先排序（超时）
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_copy = [num for num in nums]
        self._quick_sort(nums_copy, 0, len(nums_copy)-1)
        is_start = False
        for i in range(len(nums)):
            if not is_start and nums[i] != nums_copy[i]:
                begin = i
                is_start = True
            elif nums[i] != nums_copy[i]:
                end = i
        return end - begin + 1 if is_start else 0
            
    def _quick_sort(self, nums, l, r):
        lo = l
        hi = r
        if l >= r:
            return 
        while lo < hi:
            while lo < hi and nums[lo] <= nums[r]:
                lo += 1
            while lo < hi and nums[hi] >= nums[r]:
                hi -= 1
            nums[lo], nums[hi] = nums[hi], nums[lo]
        nums[lo], nums[r] = nums[r], nums[lo]
        self._quick_sort(nums, l, lo-1)
        self._quick_sort(nums, lo+1, r)

# 方法二：前后扫描，得到区间的开始和结束索引
class Solution2(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = -1
        end = -2
        
        min_v = float('inf')
        max_v = float('-inf')
        for i in range(len(nums)):
            pos = len(nums) - i - 1
            if nums[i] < max_v:
                end = i
            max_v = max(max_v, nums[i])
            if nums[pos] > min_v:
                start = pos
            min_v = min(min_v, nums[pos])
        return end - start + 1
        
print(Solution().findUnsortedSubarray([2, 1]))