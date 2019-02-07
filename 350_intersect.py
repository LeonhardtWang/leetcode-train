class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 方法一：
        #from collections import Counter
        #return list((Counter(nums1) & Counter(nums2)).elements())
        
        # 方法二：
        nums1_dic = {};nums2_dic = {}
        for num in nums1:
            if num not in nums1_dic:
                nums1_dic[num] = 1
            else:
                nums1_dic[num] += 1
        for num in nums2:
            if num not in nums2_dic:
                nums2_dic[num] = 1
            else:
                nums2_dic[num] += 1
        res = []
        for k, v in nums1_dic.items():
            if k in nums2_dic:
                count = min(v, nums2_dic[k])
                res += [k] * count
        return res
            
        
        
        