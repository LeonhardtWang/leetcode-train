import bisect

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        
    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)
        
    def findMedian(self) -> float:
        if len(self.nums) % 2:
            return self.nums[len(self.nums)//2]
        else:
            return (self.nums[len(self.nums)//2-1]+self.nums[len(self.nums)//2]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()