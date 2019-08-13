# 方法一：回溯法（超时，s类似'aaaa...')
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return ['']
        res = []
        for word in wordDict:
            n = len(word)
            if s[:n] == word:
                tmp = self.wordBreak(s[n:], wordDict)
                if tmp:
                    for r in tmp:
                        r = ' ' + r if r else r
                        res.append(word + r)
        return res

# 方法二：记忆化回溯(方法一上进行改进，剪枝)
class Solution2(object):
    def __init__(self):
        self.dic = {} # key:i 记录索引i开始的字符串的所有结果
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self._helper(0, s, wordDict)
        
    def _helper(self, index, s, wordDict):
        if index in self.dic:
            return self.dic[index]
        
        if not s[index:]:
            return ['']
        res = []
        for word in wordDict:
            n = len(word)
            if s[index:index+n] == word:
                tmp = self._helper(index+n, s, wordDict)
                if tmp:
                    for r in tmp:
                        r = ' ' + r if r else r
                        res.append(word + r)
        self.dic[index] = res
        return res

# 方法三：动态规划(leetcode超内存)
class Solution3(object):  
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [[] for _ in range(len(s)+1)]
        dp[0].append('')
        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict:
                    if dp[j]:
                        for r in dp[j]:
                            r = r + ' ' if r else r
                            dp[i].append(r + s[j:i])
        return dp[len(s)]

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(Solution3().wordBreak(s, wordDict))