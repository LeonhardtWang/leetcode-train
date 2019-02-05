class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum_ = []
        temp = 0
        for i in nums:
            temp += i
            self.sum_.append(temp)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:return self.sum_[j]
        return self.sum_[j] - self.sum_[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)