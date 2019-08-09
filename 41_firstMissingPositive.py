class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 not in nums:
            return 1
        n = len(nums)
        for i, num in enumerate(nums):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # 以数值符号作为判别，下一次当做索引时记得用绝对值还原
        for i, num in enumerate(nums): 
            if abs(num) == n:
                nums[0] = -abs(nums[0])
            else:
                nums[abs(num)] = -abs(nums[abs(num)])
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
        return n + 1

print(Solution().firstMissingPositive([1,2,0]))