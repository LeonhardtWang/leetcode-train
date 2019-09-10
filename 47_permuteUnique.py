class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.helper(nums)
        
    def helper(self, nums):
        res = []
        if not nums:
            return res
        if len(nums) == 1:
            return [nums]
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: # 避免重复
                continue
            re_res = self.permuteUnique(nums[:i]+nums[i+1:])
            for r in re_res:
                res.append([num]+r)
        return res
                