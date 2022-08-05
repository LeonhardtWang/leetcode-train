class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        if len(s) == 1:
            return [[s]]
        i = 1
        res = []
        while i <= len(s):
            # if i > 1 and s[i:i+1] == s[i-1:i] == s[0]:# 去重
            #     i += 1
            #     continue
            if self._is_pal(s[:i]):
                next_res = self.partition(s[i:])
                if next_res:
                    for r in next_res:
                        res.append([s[:i]]+r)
                else:
                    res.append([s[:i]])
            i += 1
        return res      
        
    def _is_pal(self, s):
        if len(s) <= 1:
            return True
        if s[0] == s[-1]:
            return self._is_pal(s[1:-1])
        else:
            return False

print(Solution().partition('aaa'))