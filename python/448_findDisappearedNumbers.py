# 方法一：桶排序+异或交换（抽屉原理）
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] != nums[nums[i]-1]:
                    self._swap(nums, i, nums[i]-1)
                else:
                    break
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i+1)
        return res
    
    def _swap(self, nums, i, j):
        nums[i] = nums[i] ^ nums[j]
        nums[j] = nums[i] ^ nums[j]
        nums[i] = nums[i] ^ nums[j]

# 方法二：位图
class Solution2(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        help_num = 1
        help_num <<= len(nums)
        
        for num in nums:
            help_num |= (1 << (num - 1))
        
        res = []
        for i in range(len(nums)):
            if help_num & 1 == 0:
                res.append(i+1)
            help_num >>= 1
        return res

print(Solution2().findDisappearedNumbers([3,3,2,5,4]))