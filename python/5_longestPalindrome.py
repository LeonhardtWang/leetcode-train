class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        dp = [[False for _ in range(length)] for _ in range(length)]
        max_len_str = ''
        
        for l in range(length-1, -1, -1):
            for r in range(l, length):
                dp [l][r] = dp[l+1][r-1] if (r - l >= 2 and s[l] == s[r]) else s[l] == s[r]
                if dp[l][r]:
                    curr_length = r - l + 1
                    if curr_length > len(max_len_str):
                        max_len_str = s[l:r+1]
        return max_len_str
                    
                
if __name__ == "__main__":
    print(Solution().longestPalindrome('zzzzzzzzzz'))