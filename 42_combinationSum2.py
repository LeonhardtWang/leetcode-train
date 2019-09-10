from typing import List, int
# 方法一
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates:
            return res
        candidates.sort()
        for i, num in enumerate(candidates):
            if num > target:
                break
            if num == target and [num] not in res:
                res.append([num])
            cur_res = self.combinationSum2(candidates[i+1:], target-num)
            for r in cur_res:
                if [num] + r not in res:
                    res.append([num]+r)
        return res

# 方法二：回溯+剪枝（标准解法）
class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self._dfs(candidates, 0, len(candidates), [], res, target)
        return res

    def _dfs(self, candidates, start , length, path, res, target):
        if target == 0:
            res.append(path[:])
            return 
        for i in range(start, length):
            if candidates[i] > target:
                break
            if i > start and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            self._dfs(candidates, i+1, length, path, res, target-candidates[i])
            path.pop()
