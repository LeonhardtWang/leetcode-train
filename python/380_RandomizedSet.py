class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lis = []
        self.dic = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        self.lis.append(val)
        self.dic[val] = len(self.lis) - 1
        return True
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False        
        self.dic[self.lis[-1]] = self.dic[val]
        self.lis[self.dic.pop(val)] = self.lis[-1]
        # self.lis[index], self.lis[-1] = self.lis[-1], self.lis[index]
        self.lis.pop()
        return True
        
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        if not self.lis:
            return 
        return self.lis[random.randint(0, len(self.lis)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()