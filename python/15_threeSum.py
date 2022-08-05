class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        length = len(nums)
        if length < 3 or nums[0] > 0 or nums[-1] < 0:
            return res
        repeat_num = None # 为了防止前面有重复的值造成结果重复, 比如 -1, -1, -1, 0, 1
        for l in range(length-2):
            m = l + 1
            r = length - 1
            if nums[l] == repeat_num:
                continue
            if nums[l] == nums[m]:
                repeat_num = nums[l]

            mid_record = None # 为了防止中间有重复的值造成重复，比如-1, 0, 0, 0, 0, 1
            while m < r:
                if nums[l] > 0 or nums[r] < 0:
                    break
                sum_ = nums[l] + nums[m] + nums[r]
                if sum_ == 0:
                    if nums[m] == mid_record:
                        m += 1
                        continue
                    res.append([nums[l], nums[m], nums[r]])
                    mid_record = nums[m]
                if sum_ <= 0:
                    m += 1
                else:
                    r -= 1
        return res
            

if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,0, 0, 0, -4, -1, -1, 2, 2, 2]))