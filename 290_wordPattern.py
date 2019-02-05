class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split(' ')):
            return False
        else:
            pat_to_str = ''
            s_map_dict = {}
            for i in range(len(pattern)):
                if pattern[i] not in s_map_dict:
                    if str.split(' ')[i] in s_map_dict.values():return False
                    s_map_dict[pattern[i]] = str.split(' ')[i]
                    pat_to_str = pat_to_str + s_map_dict[pattern[i]] + ' '
                else:
                    pat_to_str = pat_to_str + s_map_dict[pattern[i]] +  ' '
            return pat_to_str.rstrip() == str