class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        while n != 0:
            if nums1[i] <= nums2[0]:
                if i + 1 > m:
                    nums1[i:i+n] = nums2[:n]
                    m += n
                    n = 0
                    break
                i += 1
            else:
                temp = nums2.pop(0)
                nums1.insert(i, temp)
                del nums1[-1]
                m += 1
                n -= 1
                i += 1
        if m == 0:nums1 = nums2
nums1 = [1, 3, 4, 7, 9, 0, 0, 0, 0]; m = 5
nums2 = [2, 6, 8]; n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)