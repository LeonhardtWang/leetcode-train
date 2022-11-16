# 暴力法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        res = 0
        for i in range(len(s)):
            if res >= len(s) - i:
                return res

            char_set = set()
            for j in range(i, len(s)):
                if s[j] not in char_set:
                    char_set.add(s[j])
                else:
                    res = max(res, len(char_set))
                    break
            res = max(res, len(char_set))
        return res 
