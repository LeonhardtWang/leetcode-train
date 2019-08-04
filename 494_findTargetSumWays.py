# 方法一：递归（超时）
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums and S == 0:
            return 1
        if not nums:
            return 0
        div_res = self.findTargetSumWays(nums[:-1], S+nums[-1])
        add_res = self.findTargetSumWays(nums[:-1], S-nums[-1])
        return div_res + add_res

# 方法二：递归 + 备忘录
class Solution2(object):
    def __init__(self):
        self.res_dic = {} # 储存中间结果

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums and S == 0:
            return 1
        if not nums:
            return 0
        index = len(nums) - 1
        if (index, S+nums[-1]) in self.res_dic:
            div_res = self.res_dic[(index, S+nums[-1])]
        else:
            div_res = self.findTargetSumWays(nums[:-1], S+nums[-1])
            self.res_dic[(index, S+nums[-1])] = div_res
        if (index, S-nums[-1]) in self.res_dic:
            add_res = self.res_dic[(index, S-nums[-1])]
        else:
            add_res = self.findTargetSumWays(nums[:-1], S-nums[-1])
            self.res_dic[(index, S-nums[-1])] = add_res
        return div_res + add_res

print(Solution2().findTargetSumWays([1,1,1,1,1], 3))