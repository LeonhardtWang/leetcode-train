class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.helper(1, n+1, k)
        
    def helper(self, s, e, k):
        if k == 1:
            return [[i] for i in range(s, e)]
        res = []
        for i in range(s, e-k+2):
            tmp = self.helper(i+1, e, k-1)
            for r in tmp:
                res.append([i]+r)
        return res