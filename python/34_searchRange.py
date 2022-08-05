class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        return self.searchRangeCore(nums, target, 0, len(nums)-1)
        
    def searchRangeCore(self, nums, target, i, j):
        if not nums or i > j:
            return [-1, -1]
        mid = (i + j) // 2
        if nums[mid] >= target:
            left = self.searchRangeCore(nums, target, i, mid-1)
        if nums[mid] <= target:
            right = self.searchRangeCore(nums, target, mid+1, j)
            
        if nums[mid] > target:
            return left
        elif nums[mid] < target:
            return right
        else:
            if left[0] == -1:
                left_index = mid
            else:
                left_index = left[0]
            if right[-1] == -1:
                right_index = mid
            else:
                right_index = right[-1]
            return [left_index, right_index]
            
print(Solution().searchRange([5,7,7], 5))