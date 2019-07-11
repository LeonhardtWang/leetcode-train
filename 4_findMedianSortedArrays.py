class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n: # m <= n可保证0<=j<=n
            nums1, nums2, m, n = nums2, nums1, n, m
            
        nums1 = [-2**31] + nums1 + [2**31-1]
        nums2 = [-2**31] + nums2 + [2**31-1]
        
        i_min = 0
        i_max = m
        while i_min <= i_max:
            mid = (i_min + i_max) // 2
            j = (m + n + 1) // 2 - mid
            if nums1[mid] > nums2[j+1]:
                i_max = mid - 1
            elif nums2[j] > nums1[mid+1]:
                i_min = mid + 1
            else:
                if (m + n) % 2 == 0:
                    return (max(nums1[mid], nums2[j]) + 
                            min(nums1[mid+1], nums2[j+1])) / 2.0
                else:
                    return max(nums1[mid], nums2[j])


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))