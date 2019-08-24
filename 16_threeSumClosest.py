# 排序+双指针碰撞
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_dis = float('inf')
        for i in range(1, len(nums)-1):
            start = 0
            end = len(nums) - 1
            while start < i and end > i:
                sum_three = nums[start] + nums[i] + nums[end]
                curr_dis = sum_three - target
                if abs(curr_dis) < abs(min_dis):
                    res = sum_three
                    min_dis = curr_dis
                if sum_three > target:
                    end -= 1
                elif sum_three < target:
                    start += 1
                else:
                    return target
        return res
                    
            