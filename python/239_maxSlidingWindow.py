# 方法一：维护一个双端队列
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        queue = deque()
        res = []
        for i, num in enumerate(nums):
            if not queue:
                queue.append(i)
            else:
                while queue and num > nums[queue[-1]]:
                    queue.pop()
                queue.append(i)
            if i >= k - 1:
                res.append(nums[queue[0]])
            if queue[0] == i - k + 1:
                queue.popleft()
        return res
                
# 方法二：动态规划
class Solution2(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        left = []
        right = []
        n = len(nums)
        for i in range(n):
            if i % k == 0:
                tmp = nums[i]
                left.append(tmp)
            else:
                tmp = max(tmp, nums[i])
                left.append(tmp)
        
        for i in range(n-1, -1, -1):
            if (i + 1) % k == 0 or i == n - 1:
                tmp = nums[i]
                right.insert(0, tmp)
            else:
                tmp = max(tmp, nums[i])
                right.insert(0, tmp)
                
        res = []
        for i in range(n - k + 1):
            res.append(max(right[i], left[i+k-1]))
        return res
                    
print(Solution().maxSlidingWindow([1,3,1,2,0,5], 3))