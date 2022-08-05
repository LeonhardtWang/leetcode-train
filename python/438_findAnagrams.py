class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        p_dic = {}
        for char in p:
            if char in p_dic:
                p_dic[char] += 1
            else:
                p_dic[char] = 1
        
        s_dic = {}
        for i in range(len(p)):
            if s[i] in s_dic:
                s_dic[s[i]] += 1
            else:
                s_dic[s[i]] = 1
            
        res = []
        for i in range(len(s)-len(p)+1):
            if i == 0:
                if s_dic == p_dic:
                    res.append(i)
            else:
                s_dic[s[i-1]] -= 1
                if s_dic[s[i-1]] == 0:
                    del s_dic[s[i-1]]
                if s[i+len(p)-1] in s_dic:
                    s_dic[s[i+len(p)-1]] += 1
                else:
                    s_dic[s[i+len(p)-1]] = 1
                if s_dic == p_dic:
                    res.append(i)
        return res
                
print(Solution().findAnagrams("abab" , "ab"))