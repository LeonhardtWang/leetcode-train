class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from collections import deque
        
        nums.sort()
        res = [[]]
        start = 0
        next_start = len(res)
        queue = deque([0])
        while queue:
            while start < next_start:
                cur = queue.pop()
                for i in range(cur, len(nums)):
                    if i > cur and nums[i] == nums[i-1]: # 剪枝
                        continue
                    res.append(res[start]+[nums[i]])
                    queue.appendleft(i+1)
                start += 1
            next_start = len(res)
        return res
            
        