class Solution:
    def search(self, nums: list, target: int) -> int:
        length = len(nums)
        if length < 1:
            return -1
        rotate_num_index = self.find_rotate_num(nums, length)
        if nums[0] > target:
            res = self.binary_search(nums, rotate_num_index+1, length-1, target)
            return res
        elif nums[0] < target:
            res = self.binary_search(nums, 1, rotate_num_index, target)
            return res
        else:
            return 0
                
    def find_rotate_num(self, nums, length):
        l = 0 
        r = length - 1
        while l <= r:
            mid = (l + r) // 2
            if (mid <= 0 or nums[mid] > nums[0]) and (mid >= length-1 or nums[mid] < nums[mid+1]):
                l = mid + 1
            elif (mid <= 0 or nums[mid] < nums[0]) and (mid >= length-1 or nums[mid] < nums[mid+1]):
                r = mid - 1
            else:
                return mid
        return mid
            
    def binary_search(self, nums, l, r, target):
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1

print(Solution().search([3, 2, 1, 0] , 2))