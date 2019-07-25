class Solution:
    def numTrees(self, n: int) -> int:
        res = []
        for i in range(n+1):
            if i <= 1:
                res.append(1)
                continue
            tmp = 0
            for m in range(1, i+1):
                tmp += res[m-1] * res[i-m]
            res.append(tmp)
        return res[-1]