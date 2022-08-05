class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 方法一：调用python内置方法
        #return sorted(s) == sorted(t)
        
        # 方法二
        s_dic = {};t_dic = {}
        for i in s:
            if i in s_dic:
                s_dic[i] += 1
            else:
                s_dic[i] = 1
        for i in t:
            if i in t_dic:
                t_dic[i] += 1
            else:
                t_dic[i] = 1
        return s_dic == t_dic