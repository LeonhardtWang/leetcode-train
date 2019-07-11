class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        i = 0
        max_len = 1
        while i < len(s):
            str_len = 1
            j = i + 1
            while j < len(s):
                if s[j] not in s[i:j]:
                    str_len += 1
                    j += 1
                else:
                    str_len = j - i
                    break
            i += 1
            if max_len < str_len:
                max_len = str_len
                
        return max_len
            
            
if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))