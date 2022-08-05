class Solution:
    def removeInvalidParentheses(self, s: str) -> list:
        count_1 = 0 # '('多余的个数
        count_2 = 0 # ')' 多余的个数
        for char in s:
            if char == '(':
                count_1 += 1
            elif char == ')':
                if count_1 == 0:
                    count_2 += 1
                else:
                    count_1 -= 1
        res = []
        self._dfs(res, s, 0, count_1, count_2)
        return res
        
    def _dfs(self, res, s, start, count_1, count_2):
        if count_1 == count_2 and self._is_valid(s):
            res.append(s)
            return 
        
        for i in range(start, len(s)):
            if i != start and s[i] == s[i-1]: # 防止重复计算
                continue
            elif count_1 > 0 and s[i] == '(':
                self._dfs(res, s[:i]+s[i+1:], i, count_1-1, count_2)
            elif count_2 > 0 and s[i] == ')':
                self._dfs(res, s[:i]+s[i+1:], i, count_1, count_2-1)
        
    def _is_valid(self, s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0


print(Solution().removeInvalidParentheses("(a)())()"))