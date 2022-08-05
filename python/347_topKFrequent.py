class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        import heapq
        
        hash_num = Counter(nums)
        res = heapq.nlargest(k, hash_num.keys(), key=hash_num.get)
        return res