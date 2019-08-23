class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dic = {}
        for ch in s:
          s_dic[ch] = s_dic.get(ch, 0) + 1
        for i, ch in enumerate(s):
          if s_dic[ch] == 1:
            return i
        return -1