class Solution:
    def __init__(self):
        self.k = 0
        
    def getPermutation(self, n: int, k: int) -> str:
        self.fact_lis = [1] # 0!=1
        for i in range(1, n+1):
            self.fact_lis.append(self.fact_lis[i-1]*i)
            
        return self._dfs('', list(range(1,n+1)), k)
        
    def _dfs(self, s, lis, k):
        if k == 1:
            return s + ''.join([str(_) for _ in lis])
        else:
            # 剪枝
            mod = k % self.fact_lis[len(lis)-1]
            loop = k // self.fact_lis[len(lis)-1]
            k = mod if mod else self.fact_lis[len(lis)-1]
            # 剪枝
            
            for i, nex in enumerate(lis):
                if mod and i+1<=loop or not mod and i + 1 <= loop-1: # 剪枝
                    continue
                res = self._dfs(s+str(nex), lis[:i]+lis[i+1:], k)
                if res:
                    return res
                
        