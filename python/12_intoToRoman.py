class Solution:
    def __init__(self):
        self.map = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    def intToRoman(self, num: int) -> str:
        res = ''
        bit = 0
        while num:
            num, cur, bit = self.get_num(num, bit)
            res = self.tran_to_roman(cur, bit-1) + res
        return res
        
    def get_num(self, num, bit):
        while num % 10 == 0:
            bit += 1
            num //= 10
        return num // 10, num % 10, bit + 1
    
    def tran_to_roman(self, sim_num, bit):
        if sim_num <= 3 or bit == 3:
            return self.map[10**bit] * sim_num
        elif sim_num == 4 or sim_num == 9:
            return self.map[10**bit] + self.map[(sim_num+1)*10**bit]
        else:
            return self.map[5*10**bit] + self.map[10**bit] * (sim_num-5)

print(Solution().intToRoman(67))