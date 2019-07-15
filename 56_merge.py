class Solution:
    def merge(self, intervals: list) -> list:
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals.sort(key=lambda s:s[0])
        res = []
        tmp = intervals[0]
        i = 1
        while i <= n - 1:
            curr = intervals[i]
            if curr[0] <= tmp[1] <= curr[1]:
                tmp = [tmp[0], curr[1]]
            if tmp[1] < curr[0]:
                res.append(tmp)
                tmp = curr
            if i == n - 1:
                res.append(tmp)
            i += 1
        return res
                
        
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))