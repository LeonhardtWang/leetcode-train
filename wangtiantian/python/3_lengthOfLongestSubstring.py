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


# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            curr_s = s[left:right+1]
            max_len = max(max_len, len(curr_s))
            while left < right + 1 and right + 1 < len(s) and s[right+1] in curr_s:
                left += 1
                curr_s = s[left:right+1]
            right += 1
        return max_len
