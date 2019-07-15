# 方法一：递归（超时）
class Solution:
    def canJump(self, nums: list) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        res = False
        for step in range(1, nums[0]+1):
            res |= self.canJump(nums[step:])
        return res

# 方法二：加上记性搜索（仍超时）
class Solution2:
    def canJump(self, nums: list) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        res = [False] * (n - 1) + [True]
        for i in range(n-2, -1, -1):
            steps = nums[i]
            for step in range(1, steps+1):
                step_to_index = i + step
                if step_to_index >= n - 1 or res[step_to_index] == True:
                    res[i] = True
                    break
        return res[0]

# 在方法二上做出改进，使得时间复杂度为O(n)
class Solution3:
    def canJump(self, nums: list) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        res = [False] * (n - 1) + [True]
        max_left_index = n - 1
        for i in range(n-2, -1, -1):
            steps = nums[i]
            if steps + i >= max_left_index:
                res[i] = True
                max_left_index = i
        return res[0]

print(Solution3().canJump([2,3,1,1,4]))