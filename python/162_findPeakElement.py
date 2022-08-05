# 方法一：线性搜索
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return i
        return n - 1

# 方法二：递归二分查找
class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        return self._helper(nums, 0, len(nums)-1)
        
    def _helper(self, nums, lo, hi):
        if lo == hi:
            return lo
        mid = (lo + hi) // 2
        if nums[mid] > nums[mid+1]:
            return self._helper(nums, lo, mid)
        else:
            return self._helper(nums, mid+1, hi)

# 方法三：迭代二分查找
class Solution3:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid+1]:
                hi = mid
            else:
                lo = mid + 1
        return lo