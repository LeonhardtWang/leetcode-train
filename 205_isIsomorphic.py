class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_dic = {}
        for i in range(len(s)):
            if s[i] not in map_dic:
                if t[i] not in map_dic.values():
                    map_dic[s[i]] = t[i]
                else:
                    return False
            else:
                if map_dic[s[i]] != t[i]:
                    return False
                else:
                    continue
        return True   