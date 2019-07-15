class Solution:
    def permute(self, nums: list) -> list:
        res = []
        if not nums:
            return res
        for i, num in enumerate(nums):
            remain_res_lis = self.permute(nums[:i]+nums[i+1:])
            if not remain_res_lis:
                res.append([num])
            else:
                for remain_res in remain_res_lis:
                    res.append([num] + remain_res)
        return res

print(Solution().permute([1,2,3]))