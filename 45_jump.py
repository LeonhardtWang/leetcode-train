from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        index = 0
        count = 0
        while True:
            if index + nums[index] >= len(nums) - 1:
                return count + 1 if len(nums) != 1 else count
            max_dis = float('-inf')
            for i in range(1, nums[index]+1):
                tmp = index + i + nums[index+i] 
                if tmp > max_dis:
                    best_next_i = index + i
                    max_dis = tmp
            count += 1
            index = best_next_i

print(Solution().jump([2,3,1,1,4]))