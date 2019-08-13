# 方法一：暴力法（超时）
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        for i in range(n):
            start = i
            own = gas[i]
            remain = own - cost[i]
            i = 0 if i == n-1 else i + 1
            while i != start and remain >= 0:
                own = remain + gas[i]
                remain = own - cost[i]
                i = 0 if i == n-1 else i + 1
            if i  == start and remain >= 0:
                return i
        return -1

# 方法二：方法一上改进使得时间复杂度从O(n^2)到O(n)
class Solution2(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        gap = [gas[i]-cost[i] for i in range(n)]
        total = 0
        curr = 0
        start = 0
        for i in range(n):
            curr += gap[i]
            total += gap[i]
            if curr < 0:
                start = i + 1
                curr = 0
        return start if total >= 0 else -1
                
print(Solution().canCompleteCircuit([3, 3, 4], [3,4,4]))