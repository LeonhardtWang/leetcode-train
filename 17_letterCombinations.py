class Solution:
    def __init__(self):
        self.num_chr_map = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        
    def letterCombinations(self, digits: str) -> list:
        res = []
        self.letterCombinationsCore(res, digits)
        return res
    
    def letterCombinationsCore(self, res, digits):
        if not digits:
            return
        next_digit = digits[0]
        chr_list = list(self.num_chr_map[int(next_digit)])
        if not res:
            res.extend(chr_list)
        else:
            for _ in range(len(res)):
                res.extend([res[0]+ch for ch in chr_list])
                del res[0]
        self.letterCombinationsCore(res, digits[1:])


if __name__ == "__main__":
    print(Solution().letterCombinations(''))