class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0] * 26
        for char in tasks:
            count[ord(char)-65] += 1
        
        count.sort()
        
        res = (count[25] - 1) * (n + 1) + 1
        index = 24
        while index >= 0 and count[index] == count[25]:
            res += 1
            index -= 1
        
        return max(res, len(tasks))