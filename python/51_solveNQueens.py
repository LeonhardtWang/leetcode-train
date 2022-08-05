# 方法一：回溯法
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited = [[False for _ in range(n)] for _ in range(n)]
        loc = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        self._dfs(0, visited, res, loc, 0, n)
        return res
        
    def _dfs(self, i, visited, res, loc, count, n):
        if count == n:
            loc = [[loc[i][j] for i in range(n)] for j in range(n)]
            loc = [''.join(l) for l in loc]
            res.append(loc)
            return 
        for j in range(n):
            if visited[i][j] == True:
                continue
            record = self.attack(visited, i, j, n, loc)
            if not record:
                continue
            loc[i][j] = 'Q'
            self._dfs(i+1, visited, res, loc, count+1, n)
            self.de_attack(visited, record)
            loc[i][j] = '.'
                
    def attack(self, visited, i, j, n, loc):
        # 标记攻击区域
        record = []
        for jj in range(n): # 横向攻击
            if self.is_record(i, jj, visited, record, loc):
                self.de_attack(visited, record)
                return []
        for ii in range(n): # 纵向攻击
            if self.is_record(ii, j, visited, record, loc):
                self.de_attack(visited, record)
                return []
            
        # 捺方向攻击
        i_up = i - 1
        j_up = j - 1
        while i_up >= 0 and j_up >= 0:
            if self.is_record(i_up, j_up, visited, record, loc):
                self.de_attack(visited, record)
                return []
            i_up -= 1
            j_up -= 1
            
        i_dow = i + 1
        j_dow = j + 1
        while i_dow <= n - 1 and j_dow <= n - 1:
            if self.is_record(i_dow, j_dow, visited, record, loc):
                self.de_attack(visited, record)
                return []
            i_dow += 1
            j_dow += 1
            
        # 撇方向攻击
        i_na = i + 1
        j_na = j - 1
        while i_na <= n - 1 and j_na >= 0:
            if self.is_record(i_na, j_na, visited, record, loc):
                self.de_attack(visited, record)
                return []
            i_na += 1
            j_na -= 1
            
        i_na = i - 1
        j_na = j + 1
        while i_na >= 0 and j_na <= n -1:
            if self.is_record(i_na, j_na, visited, record, loc):
                self.de_attack(visited, record)
                return []
            i_na -= 1
            j_na += 1
        return record
    
    def de_attack(self, visited, record):
        # 重置攻击区域
        for i, j in record:
            visited[i][j] = False
    
    def is_record(self, i, j, visited, record, loc):
        if loc[i][j] == 'Q': # 新的皇后攻击到其他皇后
            return True
        if visited[i][j] == False:
            visited[i][j] = True
            record.append((i, j))
        return False
        
        
# 方法一上优化
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        attack = {k:set() for k in range(4)} # 0:横 1:竖 2:撇 3:捺
        res = []
        self._dfs(0, attack, [], res, n)
        final_res = []
        for r in res:
            tmp = []
            for index in r:
                tmp.append('.'*index+'Q'+'.'*(n-index-1))
            final_res.append(tmp)
        return final_res
        
    def _dfs(self, i, attack, loc, res, n):
        if len(loc) == n:
            res.append(loc[:])
        for j in range(n):
            if not (i in attack[0] or j in attack[1] or i+j in attack[2] or i-j in attack[3]):
                attack[0].add(i)
                attack[1].add(j)
                attack[2].add(i+j)
                attack[3].add(i-j)
                loc.append(j)
                self._dfs(i+1, attack, loc, res, n)
                loc.pop()
                attack[0].remove(i)
                attack[1].remove(j)
                attack[2].remove(i+j)
                attack[3].remove(i-j)
        