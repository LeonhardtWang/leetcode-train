class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        words_set = sorted(words)
        word_num = len(words)
        word_len = len(words[0])
        total_len = word_num * word_len
        res = []
        for i, ch in enumerate(s):
            if i + total_len > len(s):
                break
            cur_words = [s[j:j+word_len] for j in range(i, i+total_len, word_len)]
            if sorted(cur_words) == words_set:
                res.append(i)
        return res
            
            