# 方法一：深度搜索（超时）
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        return len(self._helper([A, B, C, D], 0))
        
    def _helper(self, list_lis, num_sum):
        res = []
        if len(list_lis) == 1:
            for i, num in enumerate(list_lis[0]):
                if num == num_sum:
                    res.append([i])
        else:
            for i, num in enumerate(list_lis[0]):
                tmp = self._helper(list_lis[1:], num_sum-num)
                if tmp:
                    for t in tmp:
                        res.append([i]+t)
        return res

# 方法二：哈希表记录
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import Counter
        dic = Counter([a + b for a in A for b in B])
        res = 0
        for c in C:
            for d in D:
                res += dic.get(-c-d, 0)
        return res
        