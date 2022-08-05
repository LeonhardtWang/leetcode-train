class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n = len(str)
        index = 0
        res = 0
        
        if not str:
            return res

        # 过滤空格
        while index < n: 
            if str[index] == ' ':
                index += 1
            else:
                break
        if index >= n:
            return res
        
        # 确定正负号
        if str[index] == '-' and self.is_num(str[index+1:index+2]):
            sign = -1
            index += 1
        elif str[index] == '+' and self.is_num(str[index+1:index+2]):
            sign = 1
            index += 1
        elif self.is_num(str[index]):
            sign = 1
        else:
            return res 
        
        # 转换成数字
        while index < n:
            tmp = str[index]
            if self.is_num(tmp):
                res *= 10
                res += self.tran_num(tmp)
                index += 1
            else:
                break
        res *= sign # 加上符号

        if res < -2 ** 31:
            return -2 ** 31
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return res
                        
    def is_num(self, s, is_contain_0=True):
        if not s:
            return False
        if is_contain_0:
            return 48 <= ord(s) <= 57
        else:
            return 49 <= ord(s) <= 57
        
    def tran_num(self, s):
        return ord(s) - 48


print(Solution().myAtoi("-"))