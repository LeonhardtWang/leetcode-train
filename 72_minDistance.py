class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_1 = len(word1)
        len_2 = len(word2)
        
        dp = [[0 for _ in range(len_2+1)] for _ in range(len_1+1)]
        for i in range(len_1+1):
            for j in range(len_2+1):
                if i == 0 or j == 0:
                    dp[i][j] = max(i, j)
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
                    else:
                        dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[-1][-1]
        

print(Solution().minDistance(word1 = "horse", word2 = "ros"))