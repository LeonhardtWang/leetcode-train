class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict = {}
        for s in strs:
            map_chr_lis = [0] * 26
            for ch in s:
                map_chr_lis[ord(ch)-97] += 1
            map_dict.setdefault(tuple(map_chr_lis), []).append(s)
        return list(map_dict.values())