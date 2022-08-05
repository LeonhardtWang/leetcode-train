class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        return self.combinationSumCore(candidates, target)
    
    def combinationSumCore(self, candidates, target):
        res = []
        if not candidates or target < candidates[0]:
            return res
        for can in candidates:
            remain = target - can
            if remain == 0:
                res.append([can])
            elif remain < 0:
                continue
            else:
                remain_res_lis = self.combinationSumCore(candidates, remain)
                if remain_res_lis:
                    for remain_res in remain_res_lis:
                        now_res = sorted([can] + remain_res)
                        if now_res not in res:
                            res.append(now_res)
        return res

# 方法二：回溯+剪枝
class Solution2:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self._dfs(candidates, 0, len(candidates), [], res, target)
        return res
        
    def _dfs(self, candidates, start, length, path, res, target):
        if target < 0:
            return
        if target == 0:
            res.append(path[:])
            return
        for i in range(start, length):
            if candidates[i] > target:
                break
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if not path or candidates[i] >= path[-1]:
                path.append(candidates[i])
                self._dfs(candidates, start, length, path, res, target-candidates[i])
                path.pop()

print(Solution().combinationSum([2,3,6,7], 12))
