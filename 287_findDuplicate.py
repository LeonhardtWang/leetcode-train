# 方法一：排序
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

# 方法二：集合
class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_num = set()
        for num in nums:
            if num in set_num:
                return num
            set_num.add(num)

# 方法三：鸽子洞原理
class Solution3(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = slow
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                ptr2 = slow
                break
        
        ptr1 = nums[0]
        while True:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
            
print(Solution3().findDuplicate([2,5,9,6,9,3,8,9,7,1]))