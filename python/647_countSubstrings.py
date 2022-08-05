# 方法一：动态规划
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(set(s)) == 1: # 防止字符串字符都一样导致复杂度过高
            return (1 + len(s)) * len(s) // 2
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            tmp = 0
            for j in range(i, -1, -1):
                tmp += self.is_pal_str(s[j:i+1])
            dp[i] = dp[i-1] + tmp
        return dp[-1]       
        
    def is_pal_str(self, s):
        if len(s) <= 1:
            return True
        if s[0] == s[-1]:
            return self.is_pal_str(s[1:-1])
        else:
            return False

# 方法二：中心扩展法
class Solution2(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res += self._helper(s, i, i)
            res += self._helper(s, i, i+1)
        return res 
        
    def _helper(self, s, start, end):
        count = 0
        while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
            start -= 1
            end += 1
            count += 1
        return count       

print(Solution().countSubstrings('abcba'))