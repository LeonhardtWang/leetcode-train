class Solution:
    def subsets(self, nums: list) -> list:
        res = [[]]
        for num in nums:
            res_len = len(res)
            for i in range(res_len):
                res.append(res[i]+[num])
        return res

# 方法二：递归（回溯算法）
class Solution2:
    def subsets(self, nums: list) -> list:
        if not nums:
            return [[]]
        res = self.subsets(nums[:-1])
        res_len = len(res)
        for i in range(res_len):
            res.append(res[i]+[nums[-1]])
        return res

print(Solution2().subsets([1,2,3]))