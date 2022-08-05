class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        ptr1 = 0
        ptr2 = length - 1
        curr = 0
        while curr <= ptr2:
            if curr == ptr1 and nums[curr] == 0:
                ptr1 += 1
                curr += 1
            elif nums[curr] == 0:
                self.swap(nums, curr, ptr1)
                ptr1 += 1
                curr += 1
            elif nums[curr] == 2:
                self.swap(nums, curr, ptr2)
                ptr2 -= 1
                if nums[curr] == 1:
                    curr += 1
            else:
                curr += 1

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

nums = [2, 0, 1]
Solution().sortColors(nums)
print(nums)