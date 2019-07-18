class Solution:
    def minWindow(self, s: str, t: str) -> str:
        filter_s = [(s, i) for i, s in enumerate(s) if s in t]
        left = 0
        right = 0
        
        min_len = 2 ** 31 - 1
        res = ''
        tmp_dict = {}
        t_dict = {}
        for ch in t:
            if ch in t_dict:
                t_dict[ch] += 1
            else:
                t_dict[ch] = 1

        while right < len(filter_s):
            curr = filter_s[right][0]
            if curr in t_dict.keys():
                if curr in tmp_dict:
                    tmp_dict[curr] += 1
                else:
                    tmp_dict[curr] = 1
            if  self.is_contain(t_dict, tmp_dict):
                while left <= right:
                    left_s = filter_s[left][0]
                    if left_s in t_dict.keys():
                        tmp_dict[left_s] -= 1
                        if not self.is_contain(t_dict, tmp_dict):
                            left_i = filter_s[left][1]
                            right_i = filter_s[right][1]
                            min_len_tmp = right_i - left_i + 1
                            if min_len_tmp < min_len:
                                min_len = min_len_tmp
                                res = s[left_i:right_i+1]
                            left += 1
                            break
                    left += 1
            right += 1
        return res

    def is_contain(self, dict_1, dict_2):
        """判断dict_2的所有键的值是否大于dict_1对应键的值"""
        res = True
        for k in dict_1:
            if k not in dict_2:
                return False
            else:
                res &= dict_2[k] >= dict_1[k]
        return res

print(Solution().minWindow("a", "a"))