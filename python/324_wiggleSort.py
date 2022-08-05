class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        if n % 2 == 0:
            nums1 = nums[:n//2]
            nums2 = nums[n//2:]
        else:
            nums1 = nums[:n//2+1]
            nums2 = nums[n//2+1:]
        # nums1 = nums1[::-1]
        # nums2 = nums2[::-1]
        index = 0
        nums[index] = nums1.pop()
        while nums2:
            if nums2:
                nums[index+1] = nums2.pop()
            if nums1:
                nums[index+2] = nums1.pop()
            index += 2

test = [4, 5, 5, 6]
Solution().wiggleSort(test)
print(test)