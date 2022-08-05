# 方法一
class Solution:

    def __init__(self, nums: List[int]):
        self.init_nums = [num for num in nums]
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.init_nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        random.shuffle(self.nums)
        return self.nums
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# 方法二
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        res = []
        index_lis = [i for i in range(len(self.nums))]
        while index_lis:
            random_index = random.randint(0, len(index_lis)-1)  
            res.append(self.nums[index_lis.pop(random_index)])
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()