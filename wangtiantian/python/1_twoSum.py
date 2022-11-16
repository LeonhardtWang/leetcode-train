class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2idx = {}
        for i, num in enumerate(nums):
            num2idx[num] = i

        for i, num in enumerate(nums):
            remain = target - num 
            if remain in num2idx and num2idx[remain] !=  i:
                return [i, num2idx[remain]]