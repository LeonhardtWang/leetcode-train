# 方法一：递归（超时，因为是深度优先遍历所以太慢）
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        res = self._helper(beginWord, endWord, wordList)
        return res if res != False else 0
            
    def _helper(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return False
        if self._is_dis_one_word(beginWord, endWord):
            return 2
        if not wordList:
            return False
        
        min_res = float('inf')
        for i, w in enumerate(wordList):
            if self._is_dis_one_word(beginWord, w):
                res = self._helper(w, endWord, wordList[:i]+wordList[i+1:])
                if res is not False:
                    min_res = min(res+1, min_res)
        return False if min_res == float('inf') else min_res

    def _is_dis_one_word(self, s1, s2):
        n = len(s1)
        dic_con = 0
        for i in range(n):
            if s1[i] != s2[i]:
                dic_con += 1
        return True if dic_con == 1 else False


# 方法二：广度优先遍历
class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import deque
        
        if endWord not in wordList or not wordList:
            return 0
        match_word_dic = {}
        l = len(beginWord)
        for word in wordList:
            for i in range(l):
                intermediate_word = word[:i] + '*' + word[i+1:]
                match_word_dic.setdefault(intermediate_word, []).append(word)
        
        queue = deque([(beginWord, 1)])
        while queue:
            curr_word, curr_level = queue.pop()
            for i in range(l):
                intermediate_word = curr_word[:i] + '*' + curr_word[i+1:]
                match_word_lis = match_word_dic.get(intermediate_word, [])
                for word in match_word_lis:
                    if word == endWord:
                        return curr_level + 1
                    queue.appendleft((word, curr_level+1))
                match_word_dic[intermediate_word] = []
        return 0
        
        
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log", "cog"]

print(Solution2().ladderLength(beginWord, endWord, wordList))
