class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        is_pos = (True if (numerator >= 0 and denominator > 0) or 
                          (numerator < 0 and denominator < 0) else False)
        a = abs(numerator)
        b = abs(denominator)
        res = ''
        div = a // b
        res += str(div)
        mod = a - div * b
        res_aft = ''
        mod_index_dic = {}
        while mod != 0:
            tmp = ''
            if mod in mod_index_dic:
                idx = mod_index_dic[mod]
                res_aft = res_aft[:idx] + '(' + res_aft[idx:] + ')'
                break
            mod_index_dic[mod] = len(res_aft)
            mod *= 10
            while mod < b:
                tmp += '0'
                mod_index_dic[mod] = len(tmp) + len(res_aft)
                mod *= 10
            res_aft += tmp
            div = mod // b
            mod = mod - div * b
            res_aft += str(div)
        fin_res = res + '.' + res_aft if res_aft else res
        return fin_res if is_pos or fin_res == '0' else '-'+fin_res
                
                
print(Solution().fractionToDecimal(0, -7))