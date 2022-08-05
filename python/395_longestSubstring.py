class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
          return 0
        s_dic = {}
        for ch in s:
          s_dic[ch] = s_dic.get(ch, 0) + 1
        
        s_set = set()
        for key, v in s_dic.items():
            if v < k:
                s_set.add(key)
        
        res = 0
        l = r = 0
        while r <= len(s):
            if r == len(s) and l == 0:
                return len(s)
            if r == len(s) or s[r] in s_set:
                tmp = self.longestSubstring(s[l:r], k)
                res = max(res, tmp)
                r += 1
                l = r
            else:
                r += 1
        return res
        
