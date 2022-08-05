class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return 0
        dp = [0 for _ in range(length)] # dp[i]表示以s[i]结尾的最长有效括号的长度
        max_len = 0
        for i in range(1, length):
            if s[i] == ')' and s[i-1] == '(':
                dp[i] = dp[i-2] + 2
            if s[i] == ')' and s[i-1] == ')' and i - dp[i-1] - 1 >= 0 and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2
            if dp[i] > max_len:
                max_len = dp[i]
        return max_len
        
print(Solution().longestValidParentheses("(()))())("))