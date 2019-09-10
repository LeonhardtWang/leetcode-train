class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + sum(nums[i+1:i+4]) > target:
                break
            if nums[i] + sum(nums[-1:-4:-1]) < target:
                continue
            for j in range(i+1, len(nums)-2):
                if j - i > 1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + sum(nums[j+1:j+3]) > target:
                    break
                if nums[i] + nums[j] + sum(nums[-1:-3:-1]) < target:
                    continue    
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    sum_num = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum_num < target:
                        l += 1
                    elif sum_num > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
                        while nums[r] == nums[r+1] and l < r:
                            r -= 1
        return res
                