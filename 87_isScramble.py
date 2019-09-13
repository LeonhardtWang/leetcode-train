class Solution:
    def __init__(self):
        self.dic = {}
        
    def isScramble(self, s1: str, s2: str) -> bool:
        print(s1, s2)
        if len(s1) != len(s2):
            return False
        
        if (s1, s2) in self.dic:
            return self.dic[(s1,s2)]
        if (s2, s1) in self.dic:
            return self.dic[(s2, s1)]
        
        if len(s1) == 0 or len(s1) == 1 and s1 == s2:
            self.dic[(s1,s2)] = True
            return True
        for i in range(1, len(s1)):
            r1_l = self.helper(s1[:i], s2[:i])
            if r1_l:
                r1_r = self.helper(s1[i:], s2[i:])
                if r1_r:
                    self.dic[(s1, s2)] = True
                    self.dic[(s2, s1)] = True
                    return True
            r2_l = self.helper(s1[:i], s2[-i:])
            if r2_l:
                r2_r = self.helper(s1[i:], s2[:-i])
                if r2_r:
                    self.dic[(s1, s2)] = True
                    self.dic[(s2, s1)] = True
                    return True               
        self.dic[(s1, s2)] = False
        self.dic[(s2, s1)] = False
        return False
    
    def helper(self, s1, s2):
        if (s1, s2) in self.dic:
            return self.dic[(s1, s2)]
        elif (s2, s1) in self.dic:
            return self.dic[(s2 ,s1)]
        else:
            res = self.isScramble(s1, s2)
            self.dic[(s1, s2)] = res
            self.dic[(s2, s1)] = res
            return res
        