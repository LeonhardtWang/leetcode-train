# 方法一：暴力法
class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        start = 0
        def helper(s, wordDict, start):
            if start == len(s):
                return True
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict and helper(s, wordDict, end):
                    return True
            return False
        return helper(s, wordDict, start)


# 方法二：记忆化搜索（暴力法基础上）
class Solution2:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        memo = [None for _ in range(len(s))]
        def helper(s, wordDict, start, memo):
            if start == len(s):
                return True
            if memo[start] is not None:
                return memo[start]

            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict and helper(s, wordDict, end, memo):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        return helper(s, wordDict, 0, memo)


# 方法三：宽度优先搜索
class Solution3:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        queue = [0]
        visited = [0] * len(s)
        while queue:
            start = queue.pop()
            if start == len(s):
                return True
            if visited[start] == 0:
                for end in range(start+1, len(s)+1):
                    if s[start:end] in wordDict:
                        queue.insert(0, end)
                visited[start] = 1
        return False


# 方法四：动态规划
class Solution4:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]


print(Solution4().wordBreak("aaaaaaa", ["aaaa","aaa"]))