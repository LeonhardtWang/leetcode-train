class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        index_lis = []
        s = list(s)
        for k, v in enumerate(s):
            if v in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                index_lis.append(k)
        for i in range(len(index_lis) // 2):
            s[index_lis[i]], s[index_lis[-i-1]] = s[index_lis[-i-1]], s[index_lis[i]]
        res = ''
        for _ in s:
            res += _
        return res
        