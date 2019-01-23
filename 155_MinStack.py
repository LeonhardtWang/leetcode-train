from collections import deque # 用deque更快
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sta = deque()
        self.minsta = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.sta.append(x)
        if not self.minsta or self.minsta[-1] > x:
            self.minsta.append(x)
        else:
            self.minsta.append(self.minsta[-1])
        
    def pop(self):
        """
        :rtype: void
        """
        self.sta.pop()
        self.minsta.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.sta[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minsta[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
test_stack = MinStack()
test_stack.push(2)
test_stack.push(0)
test_stack.push(-1)
test_stack.push(3)
print(test_stack.getMin())
test_stack.pop()